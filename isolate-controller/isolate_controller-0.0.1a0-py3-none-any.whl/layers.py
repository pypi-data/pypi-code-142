from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

import grpc
import grpc.aio as async_grpc
from google.cloud import storage

from isolate_controller import auth as auth0
from isolate_controller.pg_db import get_pg_client
from isolate_controller.scheduler import (
    CronJob,
    Job,
    JobScheduler,
    KubernetesJobScheduler,
    LocalJobScheduler,
)


@dataclass
class ServiceLayers:
    auth: AuthenticationLayer
    db: DatabaseLayer
    scheduler: JobScheduler
    storage: StorageLayer


@dataclass
class AuthUser:
    id: str


@dataclass
class AuthenticationLayer:
    def server_credentials(self) -> grpc.ServerCredentials:
        """Server side SSL credentials."""
        raise NotImplementedError

    def server_interceptors(self) -> List[async_grpc.ServerInterceptor]:
        raise NotImplementedError

    def get_user(self, context: grpc.ServerCredentials) -> AuthUser:
        raise NotImplementedError


@dataclass
class StorageLayer:
    async def save(self, bucket_name: str, key: str, value: bytes) -> None:
        raise NotImplementedError

    async def load(self, bucket_name: str, key: str) -> bytes:
        raise NotImplementedError

    async def list_dir(self, bucket_name: str, key: str) -> List[str]:
        raise NotImplementedError


@dataclass
class DatabaseLayer:
    async def start_job(
        self,
        job: Job | CronJob,
        user: AuthUser,
        status: str,
    ) -> None:
        raise NotImplementedError

    # TODO: I think it would be amazing if we could represent whether a job
    # is cron or not directly in the DB.
    async def update_job(self, job: Job | CronJob, status: str) -> None:
        raise NotImplementedError

    async def get_job_status(self, job_id: str) -> str:
        raise NotImplementedError

    async def get_job_user(self, job_id: str) -> AuthUser | None:
        raise NotImplementedError

    async def list_jobs_by_user(self, user: AuthUser, status: str) -> List[str]:
        raise NotImplementedError


@dataclass
class LocalAuthenticationLayer(AuthenticationLayer):
    def get_user(self, context: grpc.ServerCredentials) -> AuthUser:
        return AuthUser("local_user")

    def server_credentials(self) -> grpc.ServerCredentials:
        return grpc.local_server_credentials()

    def server_interceptors(self) -> List[async_grpc.ServerInterceptor]:
        return []


@dataclass
class LocalStorageLayer:
    storage: Dict[str, bytes] = field(default_factory=dict)

    async def save(self, bucket_name: str, key: str, value: bytes) -> None:
        self.storage[f"{bucket_name}/{key}"] = value

    async def load(self, bucket_name: str, key: str) -> bytes:
        return self.storage[f"{bucket_name}/{key}"]

    async def list_dir(self, bucket_name: str, key: str) -> List[str]:
        prefix = f"{bucket_name}/{key}"
        return [
            key
            for key in self.storage.keys()
            if key.startswith(prefix) and key != prefix
        ]


@dataclass
class LocalDatabaseLayer(DatabaseLayer):
    local_db: Dict[str, Tuple[AuthUser, str]] = field(default_factory=dict)

    async def start_job(
        self,
        job: Job | CronJob,
        user: AuthUser,
        status: str,
    ) -> None:
        self.local_db[job.id] = (user, status)

    async def update_job(self, job: Job | CronJob, status: str) -> None:
        self.local_db[job.id] = (self.local_db[job.id][0], status)

    async def get_job_status(self, job_id: str) -> str:
        return self.local_db[job_id][1]

    async def get_job_user(self, job_id: str) -> AuthUser:
        try:
            return self.local_db[job_id][0]
        except KeyError:
            return None

    async def list_jobs_by_user(self, user: AuthUser, status: str) -> List[str]:
        return [
            job
            for job, (job_user, job_status) in self.local_db.items()
            if job_user == user and job_status == status
        ]


@dataclass
class Auth0AuthenticationLayer(AuthenticationLayer):
    def server_credentials(self) -> grpc.ServerCredentials:
        return auth0.server_credentials()

    def server_interceptors(self) -> List[async_grpc.ServerInterceptor]:
        return [auth0.user_auth_intereceptor()]

    def get_user(self, context: grpc.ServerCredentials) -> AuthUser:
        metadata = dict(context.invocation_metadata() or {})
        user_id = auth0.auth0_check(metadata, auth0.USER_AUTH_TOKEN_KEY)
        return AuthUser(user_id)


# This is going to block the event loop unless we use
# async alternatives.
@dataclass
class PostgresDatabaseLayer(DatabaseLayer):
    async def start_job(
        self,
        job: Job | CronJob,
        user: AuthUser,
        status: str,
    ) -> None:
        with get_pg_client() as dbconn:
            with dbconn.cursor() as cur:
                # Fails if job_id already exists
                cur.execute(
                    """
                    INSERT INTO jobs (job_id, user_id, status)
                    VALUES (%s, %s, %s)
                    """,
                    (job.id, user.id, status),
                )
            dbconn.commit()

    async def get_job_user(self, job_id: str) -> AuthUser | None:
        with get_pg_client() as dbconn:
            with dbconn.cursor() as cur:
                cur.execute(
                    """
                    SELECT user_id FROM jobs WHERE job_id = %s
                    """,
                    (job_id,),
                )
                if cur.rowcount == 0:
                    return None

                [user_id] = cur.fetchone()
        return AuthUser(user_id)

    async def update_job(self, job: Job | CronJob, status: str) -> None:
        with get_pg_client() as dbconn:
            with dbconn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE jobs SET status = %s
                    WHERE job_id = %s
                    """,
                    (status, job.id),
                )
            dbconn.commit()

    async def list_jobs_by_user(self, user: AuthUser, status: str) -> List[str]:
        with get_pg_client() as dbconn:
            with dbconn.cursor() as cur:
                cur.execute(
                    """
                    SELECT job_id FROM jobs
                    WHERE user_id = %s AND status = %s
                    """,
                    (user.id, status),
                )
                return [job_id for job_id, in cur.fetchall()]


# This is currently blocking but ideally it must be
# async.
@dataclass
class GoogleCloudStorage(StorageLayer):
    client: storage.Client = field(default_factory=storage.Client)

    async def save(self, bucket_name: str, key: str, value: bytes) -> None:
        bucket = self.client.get_bucket(bucket_name)
        bucket.blob(key).upload_from_string(value)

    async def load(self, bucket_name: str, key: str) -> bytes:
        bucket = self.client.get_bucket(bucket_name)
        return bucket.blob(key).download_as_string()

    async def list_dir(self, bucket_name: str, key: str) -> List[str]:
        bucket = self.client.get_bucket(bucket_name)
        return [blob.name for blob in bucket.list_blobs(prefix=key) if blob.name != key]


def local_layers() -> ServiceLayers:
    """The services that are available during the
    development mode."""
    return ServiceLayers(
        auth=LocalAuthenticationLayer(),
        db=LocalDatabaseLayer(),
        scheduler=LocalJobScheduler(),
        storage=LocalStorageLayer(),
    )


def runtime_layers() -> ServiceLayers:
    """The services that are available during the
    runtime mode."""
    return ServiceLayers(
        auth=Auth0AuthenticationLayer(),
        db=PostgresDatabaseLayer(),
        scheduler=KubernetesJobScheduler(namespace="default"),
        storage=GoogleCloudStorage(),
    )


def service_layers(is_test_mode: bool) -> ServiceLayers:
    if is_test_mode:
        return local_layers()
    else:
        return runtime_layers()
