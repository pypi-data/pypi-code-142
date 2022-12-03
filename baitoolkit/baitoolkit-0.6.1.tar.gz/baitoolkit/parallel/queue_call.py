# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import itertools
import threading
import typing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from queue import Queue, Empty

from baitoolkit.common import logger_factory


class QueueCall(object):
    """
        Run functions in thread or process in queue mode.
        This class is generally used to speed restapi call via accumulating multiple requests to run in batch.
    """

    __logger = logger_factory.get_logger(__name__)

    class Future(threading.Event):
        def __init__(self):
            self._result = None

        def set_result(self, obj):
            self._result = obj

        def get_result(self, timeout=None):
            if self.wait(timeout):
                return self._result
            else:
                raise TimeoutError

    def __init__(self, queue: Queue, max_size: int, fn, process=False):
        """
        Usage:
            firstly, define a global queue "q", a function xxx(list_arg) and a global QueueCall,
            for example: qc = QueueCall(q, xxx, 5)
            secondly, call qc.run to run in a method,
            for example: qc.run([3,4])
        @param Queue queue:
        @param function fn: the function to be run when queue size exceeds max_size. only one List arguments is accepted.
        @param int max_size: the max length of accumulated argument of fn.
        """
        self._queue = queue
        self._fn = fn
        self._max_size = max_size
        if process:
            self._pool = ProcessPoolExecutor(1)
        else:
            self._pool = ThreadPoolExecutor(1)
        self._pool.submit(self._run)

    def run(self, arg: typing.List, timeout=None):
        future = QueueCall.Future()
        self._queue.put((arg, future))
        return future.get_result(timeout=timeout)

    def _run(self):
        args = list()
        futures = list()
        future_range = list()
        while True:
            arg_length = 0
            while len(args) < self._max_size:
                try:
                    if len(args) == 0:
                        arg, future = self._queue.get(block=True)
                    else:
                        arg, future = self._queue.get(block=False)

                    if arg_length == 0 or arg_length + len(arg) < self._max_size:
                        arg_length += len(arg)
                    else:
                        break
                    args.append(arg)
                    futures.append(future)
                    future_range.append((arg_length - len(arg), arg_length))
                except Empty as e:
                    self.__logger.info('queue is empty.')
                    break
            if len(arg) > 0:
                results = self._fn(itertools.chain(arg))
                for future, (result_start, result_end) in zip(futures, future_range):
                    future.set_result(results[result_start, result_end])
                args.clear()
                futures.clear()
                future_range.clear()
