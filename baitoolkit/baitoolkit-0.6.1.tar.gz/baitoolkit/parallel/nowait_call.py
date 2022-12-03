# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from baitoolkit.common import logger_factory
from baitoolkit.parallel.mutex import create_rlock


class NoWaitCall(object):
    """
        Run functions in thread or process in no-wait mode.
    """

    __logger = logger_factory.get_logger(__name__)

    def __init__(self, max_workers, process=False):
        if process:
            self._pool = ProcessPoolExecutor(max_workers)
        else:
            self._pool = ThreadPoolExecutor(max_workers)
        self._process = process
        self._max_workers = max_workers
        self._lock = create_rlock(self._process)

    def shutdown(self, wait=True):
        """
        Shuts down this executor.
        :param bool wait: ``True`` to wait until all submitted functions
            have been executed
        """
        self._pool.shutdown(wait)

    def submit(self, fn, success_cb, fail_cb, *args, **kwargs):
        """
        Submits function for execution.
        :param function fn: function to execute
        :param function success_cb: function to call while success
        :param function fail_cb: function to call while fail
        :raises MaxInstancesReachedError: if the maximum number of
            allowed instances for this job has been reached
        """

        def callback(f):
            exc, tb = f.exception_info() if hasattr(f, 'exception_info') else (
                f.exception(), getattr(f.exception(), '__traceback__', None))
            exc_info = exc.__class__, exc, tb
            if exc:
                self.__logger.exception("failed to execute function due to %s." % str(exc))
                if fail_cb is not None:
                    fail_cb(exc_info)
            else:
                if success_cb is not None:
                    success_cb(f.result())

        with self._lock:
            func = self._pool.submit(fn, *args, **kwargs)
            func.add_done_callback(callback)
