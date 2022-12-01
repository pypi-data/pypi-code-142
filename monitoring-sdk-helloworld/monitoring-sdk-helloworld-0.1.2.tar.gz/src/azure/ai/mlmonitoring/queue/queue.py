# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ..logger import logger
from threading import Condition

# A blocking queue
class MdcQueue:
    def __init__(self, capacity):
        self._max_length = capacity
        self._count = 0
        self._queue = []
        self._closed = False
        self._condition = Condition()

    def capacity(self):
        return self._max_length

    def length(self):
        return self._count

    def close(self):
        self._condition.acquire()
        self._closed = True
        self._condition.notify_all()
        self._condition.release()
        logger.info("data collector queue closed")

    def enqueue(self, payload):
        if payload is None:
            return False, "payload is None"

        self._condition.acquire()
        if self._closed:
            self._condition.release()
            return False, "queue closed"

        if self._count < self._max_length:
            self._queue.append(payload)
            self._count = self._count + 1
            self._condition.notify_all()
            self._condition.release()
            return True, "accepted"
        else:
            self._condition.release()
            return False, "queue full"

    def dequeue(self):
        self._condition.acquire()
        while(True):
            if self._count > 0:
                payload = self._queue.pop(0)
                length = len(self._queue)
                self._count = self._count - 1
                self._condition.release()
                return payload, length
            if self._closed:
                self._condition.release()
                return None, 0
            # wait for new item enqueue or queue closed
            self._condition.wait()

mdc_queue = None

def init_queue(capacity):
    global mdc_queue
    logger.debug("init data collector queue, capacity: %d", capacity)
    mdc_queue = MdcQueue(capacity)

def teardown_queue():
    global mdc_queue
    logger.debug("tear down data collector queue")
    mdc_queue = None

def get_queue():
    global mdc_queue
    return mdc_queue