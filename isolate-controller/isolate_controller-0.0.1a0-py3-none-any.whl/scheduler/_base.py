from __future__ import annotations

from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING

from isolate_controller.resources import MachineConfiguration

if TYPE_CHECKING:
    from typing import AsyncIterator


@dataclass
class Job:
    id: str
    hostname: str
    controller_auth_key: str
    port: str = "50001"


@dataclass
class CronJob:
    id: str
    cron: str
    controller_auth_key: str | None


class JobScheduler:
    """The job creation API for pluggable schedulers.

    Since the controller is an async application, the scheduler must be
    async as well. All the managed states (e.g. API clients, DB connections)
    must be initialized in the _initialize method and cleaned up in the
    _shutdown method. It is safe to assume that the _initialize method
    will be called before any other method."""

    async def _initialize(self) -> JobScheduler:
        return self

    async def _shutdown(self) -> None:
        return None

    async def __aenter__(self) -> JobScheduler:
        return await self._initialize()

    async def __aexit__(self, *args) -> None:
        await self._shutdown()

    @asynccontextmanager
    async def spawn_job(
        self,
        machine_configuration: MachineConfiguration | None = None,
    ) -> AsyncIterator[Job]:
        """Spawn a new job for the lifetime of this context."""
        job = await self.create_job(machine_configuration)
        try:
            yield job
        finally:
            await self.terminate_job(job)

    async def create_job(
        self, machine_configuration: MachineConfiguration | None
    ) -> Job:
        raise NotImplementedError

    async def terminate_job(self, job: Job) -> None:
        raise NotImplementedError

    @asynccontextmanager  # type: ignore
    async def create_new_cron_job(
        self,
        cron: str,
        machine_configuration: MachineConfiguration | None = None,
    ) -> AsyncIterator[CronJob]:
        raise NotImplementedError

    async def get_cron(self, cron_id: str) -> CronJob:
        raise NotImplementedError

    async def cancel_cron(self, cron_id: str) -> None:
        raise NotImplementedError


class SchedulerError(Exception):
    pass
