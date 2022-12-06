from __future__ import annotations

import uuid
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from isolate_controller.scheduler._base import (
    CronJob,
    Job,
    JobScheduler,
    SchedulerError,
)

if TYPE_CHECKING:
    from typing import AsyncIterator

    from isolate_controller.resources import MachineConfiguration


# NOTE: hard-coded for local testing
_LOCAL_CONTROLLER_AUTH_KEY = "local_secret"


@dataclass
class LocalJobScheduler(JobScheduler):
    server_host: str = "localhost"
    server_port: str = "50001"
    in_use: bool = False
    jobs: set[str] = field(default_factory=set)
    cron_jobs: set[tuple[str, str]] = field(default_factory=set)

    async def _initialize(self) -> LocalJobScheduler:
        self.in_use = True
        return self

    async def _shutdown(self) -> None:
        self.in_use = False

    async def create_job(
        self,
        machine_configuration: MachineConfiguration | None = None,
    ) -> Job:
        if machine_configuration is not None:
            print(
                "WARNING: LocalJobScheduler can't create machines with different"
                f" sizes: {machine_configuration}"
            )

        if not self.in_use:
            raise RuntimeError(
                "LocalJobScheduler must be activated first (async with)!"
            )

        job = Job(
            id=f"worker-{uuid.uuid4()}",
            hostname=self.server_host,
            port=self.server_port,
            controller_auth_key=_LOCAL_CONTROLLER_AUTH_KEY,
        )
        self.jobs.add(job.id)
        return job

    async def terminate_job(self, job: Job) -> None:
        self.jobs.remove(job.id)

    @asynccontextmanager  # type: ignore
    async def create_new_cron_job(
        self,
        cron: str,
        machine_configuration: MachineConfiguration | None = None,
    ) -> AsyncIterator[CronJob]:
        if machine_configuration is not None:
            print(
                "WARNING: LocalJobScheduler can't create machines with different"
                f" sizes: {machine_configuration}"
            )

        cron_job = CronJob(
            id=f"worker-{uuid.uuid4()}",
            cron=cron,
            controller_auth_key=_LOCAL_CONTROLLER_AUTH_KEY,
        )
        try:
            yield cron_job
        finally:
            self.cron_jobs.add((cron, cron_job.id))

    async def get_cron(self, cron_id: str) -> CronJob:
        for cron, cron_job_id in self.cron_jobs:
            if cron_job_id == cron_id:
                return CronJob(id=cron_job_id, cron=cron, controller_auth_key=None)
        raise SchedulerError(f"cron job {cron_id} not found")

    async def cancel_cron(self, cron_id: str) -> None:
        for cron, cron_job_id in self.cron_jobs:
            if cron_job_id == cron_id:
                self.cron_jobs.remove((cron, cron_job_id))
                return
        raise SchedulerError(f"cron job {cron_id} not found")
