import atexit
import json
import logging
import os
import threading
import time
from functools import cached_property, lru_cache

import redis as redis
from django.utils import timezone

from . import conf
from .processor import Processor
from .signals import message_received
from .utils import get_ip, get_redis_connection

logger = logging.getLogger(__name__)
STOPWORD = "STOP"


@lru_cache(maxsize=None)
class Subscriber:
    _terminator = object()

    def __init__(self, shutdown_timeout=10):
        self._lock = threading.Lock()
        self._thread = None
        self._thread_for_pid = None
        self._running = False
        self.options = {
            "shutdown_timeout": shutdown_timeout,
        }
        self.server: redis.client.Redis = get_redis_connection()
        self.pubsub = None  # type: typing.Optional[redis.client.PubSub]
        self.processor = Processor()  # type: Processor
        self.register()

    def notify_status(self):
        data = json.loads(self.server.hget(conf.REGISTRY, str(id(self))))
        data["timestamp"] = str(timezone.now())
        data["status"] = {True: "Running", False: "Stopped"}[self._running]
        self.server.hset(conf.REGISTRY, str(id(self)), json.dumps(data))

    def register(self):
        self.server.hset(conf.REGISTRY, str(id(self)), "{}")

    @cached_property
    def channel(self):
        return conf.EVENTS

    def is_alive(self):
        if self._thread_for_pid != os.getpid():
            return False
        return self._thread and self._thread.is_alive()

    def main_thread_terminated(self):
        self._lock.acquire()
        logger.info("Listener stopping")
        try:
            if not self.is_alive():  # pragma: no cover
                # thread not started or already stopped - nothing to do
                return
            self._thread = None
        finally:
            self._lock.release()

    def start(self):
        logger.info("Listener is trying to start")
        self._lock.acquire()
        try:
            if not self.is_alive():
                self._running = True
                self._thread = threading.Thread(target=self._target)
                self._thread.setDaemon(True)
                self._thread.start()
                self._thread_for_pid = os.getpid()
                atexit.register(self.main_thread_terminated)
                self.notify_status()
                logger.info("Listener started")
            else:
                logger.info("Listener already started")
        finally:
            self._lock.release()

    def stop(self, timeout=None):
        logger.info("Listener stopping")
        self._lock.acquire()
        try:
            if self._thread:
                self._running = False
                self._thread.join(timeout=timeout)
                self._thread = None
                self._thread_for_pid = None
                self.notify_status()
            logger.info("Listener stopped")
        finally:
            self._lock.release()
            atexit.unregister(self.main_thread_terminated)

    def _target(self):
        self.pubsub = self.server.pubsub()
        self.pubsub.subscribe(self.channel)
        while self._running:
            message = self.pubsub.get_message(ignore_subscribe_messages=True)
            if message and message["data"]:
                try:
                    message_received.send(sender=self, message=message)
                    self.processor.process(message)
                except Exception as e:  # pragma: no cache
                    logger.exception(e)
            time.sleep(5)

    def build_message(self, payload) -> str:
        return json.dumps({"sender": id(self), "from": get_ip(), "config": payload})

    def notify(self, info):
        self.server.publish(self.channel, self.build_message(info))


subscriber = Subscriber()
