from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

import grpc.aio as async_grpc
from grpc import StatusCode
from grpc.aio import ServicerContext

# gRPC definitions
from isolate.server import definitions as worker_definitions

from isolate_controller import auth
from isolate_controller import definitions as controller_definitions
from isolate_controller import flags
from isolate_controller.layers import ServiceLayers, service_layers
from isolate_controller.resources import (
    InvalidMachineRequirements,
    parse_machine_requirements,
)
from isolate_controller.scheduler import JobScheduler, SchedulerError

if TYPE_CHECKING:
    from typing import AsyncIterator, List

# Maximum of seconds to wait for a worker to start up.
_WORKER_STARTUP_TIMEOUT = 15
_PROJECT_ID = os.environ.get("PROJECT_ID", "isolate-dev-gorgeous-swine")
_CRON_INPUT_BUCKET_NAME = f"{_PROJECT_ID}_scheduled_jobs"
_CRON_OUTPUT_BUCKET_NAME = f"{_PROJECT_ID}_logs"


@dataclass
class ControllerService(controller_definitions.IsolateControllerServicer):
    scheduler: JobScheduler
    layers: ServiceLayers

    async def Schedule(
        self,
        request: controller_definitions.HostedRunCron,
        context: ServicerContext,
    ) -> controller_definitions.ScheduleInfo:
        authenticated_user = self.layers.auth.get_user(context)
        machine_requirements = parse_machine_requirements(request.machine_requirements)

        try:
            async with self.scheduler.create_new_cron_job(
                request.cron, machine_requirements
            ) as cron_job:
                isolate_request = worker_definitions.BoundFunction(
                    environments=request.environments,
                    function=request.function,
                )

                await self.layers.storage.save(
                    _CRON_INPUT_BUCKET_NAME,
                    cron_job.id,
                    isolate_request.SerializeToString(),
                )
        except SchedulerError as exc:
            self.abort_with_msg(f"Unschedulable job: {str(exc)}", context)
            return
        else:
            await self.layers.db.start_job(
                cron_job, user=authenticated_user, status="SCHEDULED"
            )

        run_state = controller_definitions.ScheduleInfo.State
        return controller_definitions.ScheduleInfo(
            run_id=cron_job.id, state=run_state.Value("SCHEDULED")
        )

    async def ListScheduledRuns(
        self,
        request: controller_definitions.ListScheduledRunsRequest,
        context: ServicerContext,
    ) -> controller_definitions.ListScheduledRunsResponse:
        run_state = controller_definitions.ScheduleInfo.State

        authenticated_user = self.layers.auth.get_user(context)
        scheduled_run_ids = await self.layers.db.list_jobs_by_user(
            user=authenticated_user,
            status="SCHEDULED",
        )
        scheduled_runs = []
        for run_id in scheduled_run_ids:
            try:
                cron_job = await self.scheduler.get_cron(run_id)
            except SchedulerError:
                # If the cron job is not found, that means DB has been out of sync
                # we have to pick which one is the source of truth.
                raise NotImplementedError

            scheduled_runs.append(
                controller_definitions.ScheduleInfo(
                    run_id=run_id,
                    state=run_state.Value("SCHEDULED"),
                    cron=cron_job.cron,
                )
            )

        return controller_definitions.ListScheduledRunsResponse(
            scheduled_runs=scheduled_runs
        )

    async def ListScheduledRunActivations(
        self,
        request: controller_definitions.ListScheduledRunActivationsRequest,
        context: ServicerContext,
    ) -> controller_definitions.ListScheduledRunActivationsResponse:
        authenticated_user = self.layers.auth.get_user(context)
        job_user = await self.layers.db.get_job_user(request.run_id)
        if job_user != authenticated_user:
            self.abort_with_msg(
                "Unauthorized",
                context,
                code=StatusCode.UNAUTHENTICATED,
            )
            return

        try:
            cron_job = await self.scheduler.get_cron(request.run_id)
        except SchedulerError as exc:
            self.abort_with_msg(str(exc), context)
            return

        activation_ids = []
        for entry in await self.layers.storage.list_dir(
            _CRON_OUTPUT_BUCKET_NAME, cron_job.id
        ):
            _, _, timestamp = entry.rpartition("/")
            activation_ids.append(timestamp)

        return controller_definitions.ListScheduledRunActivationsResponse(
            activation_ids=activation_ids
        )

    async def CancelScheduledRun(
        self,
        request: controller_definitions.CancelScheduledRunRequest,
        context: ServicerContext,
    ) -> controller_definitions.CancelScheduledRunResponse:
        authenticated_user = self.layers.auth.get_user(context)
        job_user = await self.layers.db.get_job_user(request.run_id)
        if job_user != authenticated_user:
            self.abort_with_msg(
                "Unauthorized",
                context,
                code=StatusCode.UNAUTHENTICATED,
            )
            return

        try:
            cron_job = await self.scheduler.get_cron(request.run_id)
        except SchedulerError as exc:
            self.abort_with_msg(str(exc), context)
            return

        await self.scheduler.cancel_cron(cron_job.id)
        await self.layers.db.update_job(cron_job, status="CANCELLED")
        return controller_definitions.CancelScheduledRunResponse()

    async def Run(
        self,
        request: controller_definitions.HostedRun,
        context: ServicerContext,
    ) -> AsyncIterator[controller_definitions.HostedRunResult]:
        start_time = time.perf_counter()
        try:
            machine_configuration = parse_machine_requirements(
                request.machine_requirements
            )
        except InvalidMachineRequirements as exc:
            self.abort_with_msg(
                f"Invalid machine requirements: {str(exc)}",
                context,
                code=StatusCode.INVALID_ARGUMENT,
            )
            return

        async with self.scheduler.spawn_job(machine_configuration) as job:
            authenticated_user = self.layers.auth.get_user(context)
            await self.layers.db.start_job(
                job, user=authenticated_user, status="PENDING"
            )
            async with async_grpc.insecure_channel(
                job.hostname + ":" + job.port
            ) as channel:
                channel_status = channel.channel_ready()
                try:
                    await asyncio.wait_for(
                        channel_status, timeout=_WORKER_STARTUP_TIMEOUT
                    )
                except asyncio.TimeoutError:
                    self.abort_with_msg("Timeout connecting to isolate worker", context)
                    return

                end_time = time.perf_counter()
                print("Startup took:", end_time - start_time)

                isolate = worker_definitions.IsolateStub(channel)
                isolate_request = worker_definitions.BoundFunction(
                    environments=request.environments,
                    function=request.function,
                )

                # TODO: this can be done as a client interceptor to attach metadata to all worker calls
                call_metadata = async_grpc.Metadata()
                call_metadata.add(
                    *auth.worker_call_credentials_metadata(job.controller_auth_key)
                )

                run = isolate.Run(isolate_request, metadata=call_metadata)
                async for partial_run_result in run:
                    run_state = controller_definitions.HostedRunStatus.State
                    if partial_run_result.is_complete:
                        state = run_state.Value("SUCCESS")
                    else:
                        state = run_state.Value("IN_PROGRESS")

                    # TODO: This is quite expensive, we should only do it when we now the
                    # state has been changed (e.g. record the previous state)
                    status = controller_definitions.HostedRunStatus(state=state)
                    await self.layers.db.update_job(job, status=run_state.Name(state))

                    yield controller_definitions.HostedRunResult(
                        run_id=job.id,
                        status=status,
                        logs=partial_run_result.logs,
                        return_value=partial_run_result.result,
                    )

    def abort_with_msg(
        self,
        message: str,
        context: ServicerContext,
        *,
        code: StatusCode = StatusCode.INVALID_ARGUMENT,
    ) -> None:
        context.set_code(code)
        context.set_details(message)


def prepare_interceptors(
    layers: ServiceLayers,
) -> List[async_grpc.ServerInterceptor]:
    return [
        *layers.auth.server_interceptors(),
    ]


async def run_server(layers: ServiceLayers, *, port: str = "6005") -> None:
    server = async_grpc.server(interceptors=prepare_interceptors(layers))

    async with layers.scheduler as scheduler:
        controller_service = ControllerService(scheduler, layers)
        controller_definitions.register_controller(controller_service, server)

        server.add_secure_port(f"[::]:{port}", layers.auth.server_credentials())
        print(f"Started listening at localhost:{port}")

        await server.start()
        try:
            await server.wait_for_termination()
        finally:
            # Await for the coroutines to finish
            await server.stop(1)


async def main() -> None:
    layers: ServiceLayers = service_layers(is_test_mode=flags.TEST_MODE)
    await run_server(layers)


if __name__ == "__main__":
    asyncio.run(main())
