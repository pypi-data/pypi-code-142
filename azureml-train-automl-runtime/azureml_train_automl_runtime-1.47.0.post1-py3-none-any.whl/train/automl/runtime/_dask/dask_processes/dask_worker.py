# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
from azureml.train.automl.runtime._dask.constants import Constants
from azureml.train.automl.runtime._dask.dask_processes.dask_process_controller import DaskProcessController


class DaskWorker:
    """Handles Dask worker  operations."""

    def __init__(self):
        self._worker_process = DaskProcessController()

    def start(self,
              scheduler_ip: str,
              worker_per_core: bool = True) -> None:
        """Start the worker."""

        worker_count = 1
        if worker_per_core:
            # At most 16 workers per node gives us flexibility
            # For datasets needing more speed and less memory, use machines with 16 cores or less
            # For datasets needing more memory (ex large grains), use machines with cores greater than 16
            cpu_count = os.cpu_count()
            if cpu_count is not None:
                worker_count = min(16, cpu_count)

        memory_per_worker = float(1 / worker_count)

        self._worker_process.start_process(
            'dask-worker',
            ['tcp://{}:{}'.format(scheduler_ip, Constants.SCHEDULER_PORT)],
            {
                'nprocs': str(worker_count),
                'nthreads': '1',
                'memory-limit': str(memory_per_worker),
                'death-timeout': '30'
            }
        )

    def wait(self) -> None:
        """Wait for the worker to termminate."""
        self._worker_process.wait()
