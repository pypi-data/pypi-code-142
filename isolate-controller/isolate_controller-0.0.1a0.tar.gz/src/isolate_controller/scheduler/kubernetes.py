from __future__ import annotations

import os
import uuid
from contextlib import AsyncExitStack, asynccontextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from kubernetes_asyncio import client, config, watch
from kubernetes_asyncio.client.api_client import ApiClient
from redis import asyncio as redis

from isolate_controller.resources import DEFAULT_MACHINE, Limits, MachineConfiguration
from isolate_controller.scheduler._base import (
    CronJob,
    Job,
    JobScheduler,
    SchedulerError,
)
from isolate_controller.shared_db import resource_lock

if TYPE_CHECKING:
    from typing import Any, AsyncIterator

# Google Cloud Project ID
PROJECT_ID = os.environ.get("PROJECT_ID", "isolate-dev-gorgeous-swine")

# Maximum wait time for a pod to be created
MAX_POD_CREATION_AWAIT_TIMEOUT_SECONDS = 20 * 60


async def load_kube_config() -> None:
    try:
        config.load_incluster_config()
    except config.ConfigException:
        try:
            await config.load_kube_config()
        except config.ConfigException:
            print("WARNING: Could not load kube config")


@dataclass
class KubernetesForger:
    """A template creation utility for dealing with
    kubernetes template objects in Python."""

    # Fixed settings for the time being
    SETTINGS = {
        "exposed_port": 50001,
        "nfs-name": "nfs-server-controller",
        "nfs-mount-path": "/root/.cache",
        "nfs-claim-name": "isolate-fileserver",
        "labels": {
            "app": "isolate-worker",
        },
        "worker_image": f"us-central1-docker.pkg.dev/{PROJECT_ID}/isolate-cloud/worker:latest",
    }

    def new_container(
        self,
        limits: Limits,
        environment: dict[str, Any],
    ) -> client.V1Container:
        return client.V1Container(
            name="isolate-worker",
            image=self.SETTINGS["worker_image"],
            ports=[
                client.V1ContainerPort(container_port=self.SETTINGS["exposed_port"]),
            ],
            resources=client.V1ResourceRequirements(
                limits=limits.to_kubernetes(),
            ),
            volume_mounts=[
                client.V1VolumeMount(
                    mount_path=self.SETTINGS["nfs-mount-path"],
                    name=self.SETTINGS["nfs-name"],
                )
            ],
            env=[
                client.V1EnvVar(variable, str(value))
                for variable, value in environment.items()
            ],
        )

    def new_job_template(
        self,
        limits: Limits,
        environment: dict[str, Any],
    ) -> client.V1PodTemplateSpec:
        return client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels=self.SETTINGS["labels"],
            ),
            spec=client.V1PodSpec(
                containers=[
                    self.new_container(
                        limits,
                        environment,
                    )
                ],
                restart_policy="Never",
                volumes=[
                    client.V1Volume(
                        name=self.SETTINGS["nfs-name"],
                        persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(
                            claim_name=self.SETTINGS["nfs-claim-name"]
                        ),
                    )
                ],
            ),
        )

    def new_job(
        self,
        job_id: str,
        machine: MachineConfiguration,
        controller_auth_key: str,
    ) -> client.V1Job:
        """Create a new job template."""
        environment = {
            "JOB_ID": job_id,
            "CONTROLLER_KEY": controller_auth_key,
        }

        return client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(name=job_id),
            spec=client.V1JobSpec(
                backoff_limit=1,
                template=self.new_job_template(machine.limits, environment=environment),
                ttl_seconds_after_finished=20,
            ),
        )

    def new_cron_job(
        self,
        cron: str,
        job_id: str,
        machine: MachineConfiguration,
        controller_auth_key: str,
    ) -> client.V1CronJob:
        environment = {
            "JOB_ID": job_id,
            "IS_CRON": True,
            "CONTROLLER_KEY": controller_auth_key,
        }

        return client.V1CronJob(
            api_version="batch/v1",
            kind="CronJob",
            metadata=client.V1ObjectMeta(name=job_id),
            spec=client.V1CronJobSpec(
                schedule=cron,
                job_template=client.V1JobTemplateSpec(
                    spec=client.V1JobSpec(
                        backoff_limit=1,
                        template=self.new_job_template(
                            machine.limits, environment=environment
                        ),
                        ttl_seconds_after_finished=20,
                    ),
                ),
            ),
        )


@dataclass
class KubernetesJobScheduler(JobScheduler):
    namespace: str
    forger: KubernetesForger = field(
        repr=False,
        default_factory=KubernetesForger,
    )
    _core_api: client.CoreV1Api | None = field(repr=False, default=None)
    _batch_api: client.BatchV1Api | None = field(repr=False, default=None)
    _redis_client: redis.Redis | None = field(repr=False, default=None)
    _stack: AsyncExitStack | None = field(repr=False, default=None)

    async def _initialize(self) -> KubernetesJobScheduler:
        from isolate_controller.shared_db import get_redis_client

        # Already initialized.
        if self._stack is not None:
            return self

        try:
            await load_kube_config()
        except config.ConfigException:
            print("WARNING: Could not load kube config.")

        self._stack = AsyncExitStack()

        api_client = await self._stack.enter_async_context(ApiClient())
        self._core_api = client.CoreV1Api(api_client)
        self._batch_api = client.BatchV1Api(api_client)
        self._redis_client = await self._stack.enter_async_context(get_redis_client())
        return self

    async def _shutdown(self, *args) -> None:
        if self._stack is None:
            return None

        try:
            await self._stack.aclose()
        finally:
            self._stack = None
            self._core_api = None
            self._batch_api = None
            self._redis_client = None

    @property
    def core_api(self) -> client.CoreV1Api:
        if self._core_api is None:
            raise RuntimeError("JobScheduler must be activated first (async with)!")
        return self._core_api

    @property
    def batch_api(self) -> client.BatchV1Api:
        if self._batch_api is None:
            raise RuntimeError("JobScheduler must be activated first (async with)!")
        return self._batch_api

    @property
    def redis_client(self) -> redis.Redis:
        if self._redis_client is None:
            raise RuntimeError("JobScheduler must be activated first (async with)!")
        return self._redis_client

    def _get_pod_ip(self, pod: client.V1Pod) -> str | None:
        pod_phase = pod.status.phase
        if pod_phase != "Pending":
            return pod.status.pod_ip

        # Try again
        if not pod.status.container_statuses:
            return None

        [container_status] = pod.status.container_statuses
        if (
            container_status.state.waiting
            and container_status.state.waiting.reason != "ContainerCreating"
        ):
            # The pod might stuck in the Pending state for other reasons,
            # which we are going to treat as an error for now.
            raise SchedulerError(f"Pod stuck in pending state: {pod}")

    async def create_job(
        self,
        machine_configuration: MachineConfiguration | None = None,
    ) -> Job:
        machine_configuration = machine_configuration or DEFAULT_MACHINE
        job_id = f"worker-{uuid.uuid4()}"
        controller_auth_key = str(uuid.uuid4())

        # Setup a watch for the pod for this job
        watcher = watch.Watch()
        list_watcher = watcher.stream(
            self.core_api.list_namespaced_pod,
            namespace=self.namespace,
            label_selector=f"job-name={job_id}",
            limit=1,
            resource_version="0",
            timeout_seconds=MAX_POD_CREATION_AWAIT_TIMEOUT_SECONDS,
        )

        async with resource_lock(self.redis_client, "job-creation"):
            await self.batch_api.create_namespaced_job(
                body=self.forger.new_job(
                    job_id,
                    machine_configuration,
                    controller_auth_key,
                ),
                namespace=self.namespace,
            )

        hostname: str | None = None
        pod: client.V1Pod | None = None

        async for event in list_watcher:
            pod = event["object"]  # type: ignore

            if pod:
                hostname = self._get_pod_ip(pod)
                if hostname:
                    break

        await list_watcher.close()

        # TODO: in case we take longer than the timeout, how can we raise nicer?
        assert hostname, (
            f"Job {job_id} should have IP assigned. This is unexpected, please report"
            " by reaching out to hello@fal.ai"
        )
        return Job(job_id, hostname, controller_auth_key)

    async def terminate_job(self, job: Job) -> None:
        await self.batch_api.delete_namespaced_job(
            name=job.id,
            namespace=self.namespace,
            body=client.V1DeleteOptions(
                grace_period_seconds=0,
                propagation_policy="Foreground",
            ),
        )

    @asynccontextmanager  # type: ignore
    async def create_new_cron_job(
        self,
        cron: str,
        machine_configuration: MachineConfiguration | None = None,
    ) -> AsyncIterator[CronJob]:
        job_id = f"worker-{uuid.uuid4()}"
        auth_key = str(uuid.uuid4())
        cron_job = self.forger.new_cron_job(
            cron,
            job_id=job_id,
            machine=machine_configuration or DEFAULT_MACHINE,
            controller_auth_key=auth_key,
        )

        yield CronJob(job_id, cron=cron, controller_auth_key=auth_key)
        await self.batch_api.create_namespaced_cron_job(
            namespace=self.namespace, body=cron_job
        )

    async def get_cron(self, cron_id: str) -> CronJob:
        try:
            cron_job = await self.batch_api.read_namespaced_cron_job(
                name=cron_id, namespace=self.namespace
            )
        except client.ApiException as e:
            if e.status == 404:
                raise SchedulerError(f"Cron job {cron_id} not found")
            raise

        return CronJob(
            cron_id,
            cron=cron_job.spec.schedule,
            controller_auth_key=None,
        )

    async def cancel_cron(self, cron_id: str) -> None:
        await self.batch_api.delete_namespaced_cron_job(
            name=cron_id,
            namespace=self.namespace,
            body=client.V1DeleteOptions(
                grace_period_seconds=0,
                propagation_policy="Foreground",
            ),
        )
