# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

from baitoolkit.common import logger_factory


class WaitCall(object):
    """
        Run functions in thread or process in blocking mode.
    """
    __logger = logger_factory.get_logger(__name__)

    def __init__(self, max_workers, process=False):
        if process:
            self._pool = ProcessPoolExecutor(max_workers)
        else:
            self._pool = ThreadPoolExecutor(max_workers)
        self._process = process
        self._max_workers = max_workers
        self._functions = {}

    def submit(self, fn_id, timeout, fn, *args, **kwargs):
        """
        Submits function for execution.
        :param st fn_id: the identification of fn.
        :param int timeout: the number of seconds to wait the fn execution. return None if timeout.
                            if None, then there is no limit on the wait time.
        :param function fn: function to execute
        :param tuple args: parameters of fn
        :param dict kwargs: parameters of fn
        :return void
        """
        if (len(self._functions)) == self._max_workers:
            raise RuntimeError("this call has exceeds the max workers functions , new function can't be added.")
        if fn_id in self._functions:
            raise ValueError("the function %s has been added." % fn_id)
        self._functions[fn_id] = (fn, timeout, args, kwargs)

    def run(self, timeout=None):
        """
        run the multiple functions in thread pool or process pool.
        :param int timeout: The maximum number of seconds to wait. If None, then there
                            is no limit on the wait time.
        :return tuple(data dict, error dict): error error dict is None if no error is raised.
                     the key of data dict is func_id. the key of error dict is func_id.
                     the value of error dict is sys.exc_info tuple (exc_type, exc_value, exc_traceback).
        """

        def wrap_func(fn1, args1, kwargs1):
            try:
                return None, fn1(*args1, **kwargs1)
            except BaseException as e1:
                return e1, sys.exc_info()

        try:
            if len(self._functions) == 1:
                key, (fn, timeout, args, kwargs) = self._functions.popitem()
                try:
                    data = fn(*args, **kwargs)
                    return {key: data}, None
                except Exception as e:
                    self.__logger.exception("failed to execute function <%s> due to %s." % (key, str(e)))
                    return None, {key: sys.exc_info()}
            else:
                tasks = []
                for id1, func in self._functions.items():
                    fn, to, args, kwargs = func
                    f = self._pool.submit(wrap_func, fn, args, kwargs)
                    f.timeout = to
                    f.fn_id = id1
                    tasks.append(f)
                datas = {}
                errors = {}
                for future in as_completed(tasks, timeout=timeout):
                    try:
                        future.exception(future.timeout)
                        data = future.result()
                        if data[0] is None:
                            datas[future.fn_id] = data[1]
                        else:
                            errors[future.fn_id] = data[1]
                    except Exception as e:
                        self.__logger.exception("failed to execute function <%s> due to %s." % (future.fn_id, str(e)))
                        errors[future.fn_id] = sys.exc_info()
                return datas, None if len(errors) == 0 else errors
        finally:
            self._pool = None
