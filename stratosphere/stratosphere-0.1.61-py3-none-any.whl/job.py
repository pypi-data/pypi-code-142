import logging
import multiprocessing

import joblib

try:
    # We expect this import to work out if we want to use Dask.
    # Otherwise, not necessary.
    from distributed import get_client
except ImportError:
    pass

from typing import Callable, List

from stratosphere import config
from stratosphere.run import Run
from stratosphere.utils.progress import progress


class ProgressParallel(joblib.Parallel):
    """This class managed a progress bar monitoring the parallel execution of tasks."""

    def __init__(self, use_tqdm: bool = True, total: int = None, *args, **kwargs):
        """Create a new progress bar.

        Args:
            use_tqdm (bool, optional): If True, will use tqdm. IF False,
            the tasks will be executed with no progress bar. Defaults to True.
            total (int, optional): Total number of tasks planned for execution.
            Defaults to None.
            args: Additional args to pass to the joblib.Parallel constructor.
            kwargs: Additional kwargs pass to the joblib.Parallel constructor.
        """
        self._use_tqdm = use_tqdm
        self._total = total
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        with progress(disable=not self._use_tqdm, total=self._total) as self._pbar:
            return joblib.Parallel.__call__(self, *args, **kwargs)

    def print_progress(self) -> None:
        if self._total is None:
            self._pbar.total = self.n_dispatched_tasks
        self._pbar.n = self.n_completed_tasks
        self._pbar.refresh()


def parallel(funcs: List[Callable], n_jobs: int = -1) -> List[object]:
    """Execute a list of functions in parallel, returning their return values as a list.

    Args:
        funcs (List[Callable]): Functions to execute, no parameters. You can
        use functools.partial to build suitable functions.
        n_jobs (int, optional): Level of parallelization, passed to Joblib. Defaults to -1.

    Returns:
        List[object]: List of return values of the executed functions.
    """

    # We leave -1 as default value for n_jobs, so that Joblib will figure out a reasonable value.
    logging.info(f"Executing {len(funcs)} tasks on {n_jobs} parallel workers")

    # Instantiate the parallel executor
    p = ProgressParallel(n_jobs=n_jobs, use_tqdm=config.tqdm.enable, total=len(funcs))

    # Get the reeturn values, and return them as a lsit.
    # This function completes once all tasks return.
    rets = p(joblib.delayed(func)() for func in funcs)
    return rets


class Job:
    """This class is the entry point for all things execution."""

    def __init__(
        self,
        tasks: List[Callable] = None,
        n_jobs: int = -1,
        backend: str = joblib.parallel.DEFAULT_BACKEND,
    ):
        """Prepare a new job to execute.

        Args:
            tasks (List[Callable], optional): List of functions to be executed. Defaults to None.
            n_jobs (int, optional): Number of tasks to execute in parallel, same meaning as in
            Joblib. Defaults to -1.
            backend (str, optional): Backend to use, same meaning as in Joblib.
            Defaults to joblib.parallel.DEFAULT_BACKEND.
        """

        self.tasks = tasks
        self.n_jobs = n_jobs
        self.backend = backend

    def execute(self) -> List[Run]:
        """Execute the plan.

        Returns:
            List[Run]: List of runs, after being passed as
            input to the functions.
        """

        logging.info(f"Using backend: {self.backend}")

        n_jobs = self.n_jobs

        if self.backend == "dask":
            client = get_client()
            logging.info(f"Dashboard: {client.dashboard_link}")
            logging.info(f"Scheduler: {client.scheduler.address}")
            if self.n_jobs == -1:
                n_jobs = len(client.scheduler_info()["workers"])
        elif self.backend == joblib.parallel.DEFAULT_BACKEND:
            if self.n_jobs == -1:
                n_jobs = multiprocessing.cpu_count()

        with joblib.parallel_backend(self.backend):
            runs = parallel(self.tasks, n_jobs=n_jobs)

            # make sure that we have all the runs expect.
            assert len(runs) == len(self.tasks)  # noqa

            return runs
