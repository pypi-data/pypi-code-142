# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

"""
This module defines constant for events emitted by external services that work
with MBS together to complete a module build.

The event name is defined in general as much as possible, especially for the
events from Koji. Because some instance based on Koji, like Brew, might send
messages to different topics on different message bus. For example, when a
build is complete, Koji sends a message to topic buildsys.build.state.change,
however Brew sends to topic brew.build.complete, etc.
"""

from __future__ import absolute_import
from functools import wraps
import sched
import threading
import time

from module_build_service.common import log


KOJI_BUILD_CHANGE = "koji_build_change"
KOJI_TAG_CHANGE = "koji_tag_change"
KOJI_REPO_CHANGE = "koji_repo_change"
MBS_MODULE_STATE_CHANGE = "mbs_module_state_change"


class Scheduler(sched.scheduler):
    """
    Subclass of `sched.scheduler` allowing to schedule handlers calls.

    If one of the MBS handler functions need to call another handler, they need to do it in a safe
    way - such another handler call should not be done in the middle of another handler's
    execution.

    This class provides an solution for that. Handler can schedule run of other handler using
    the `add` method. The handlers should use `mbs_event_handler` decorator which ensures that
    the `run` method is called at the end of handler's execution and other scheduler handlers
    are executed.
    """

    def __init__(self, *args, **kwargs):
        sched.scheduler.__init__(self, *args, **kwargs)
        self.local = threading.local()

    def add(self, handler, arguments=()):
        """
        Schedule execution of `handler` with `arguments`.
        """
        self.enter(0, 0, handler.delay, arguments)

    def run(self):
        """
        Runs scheduled handlers.
        """
        if getattr(self.local, 'running', False):
            return

        try:
            self.local.running = True
            # Note that events that are added during the execution of the
            # handlers are executed as part of the .run() call without
            # further logging.
            log.debug("Running event scheduler with following events:")
            for event in self.queue:
                log.debug("    %r", event)
            sched.scheduler.run(self)
        finally:
            self.local.running = False

    def reset(self):
        """
        Resets the Scheduler to initial state.
        """
        while not self.empty():
            self.cancel(self.queue[0])


scheduler = Scheduler(time.time, delayfunc=lambda x: x)


class EventTrap():
    """
    A context handler that can be used to provide a place to store exceptions
    that occur in event handlers during a section of code. This is global rather
    than per-thread, because we we set up the trap in the main thread, but
    event event handlers are processed in the thread where moksha runs MBSConsumer.

    This is needed because @celery_app.task simply logs and ignores exceptions.
    """
    lock = threading.Lock()
    current = None

    def __init__(self):
        self.exception = None

    def __enter__(self):
        with EventTrap.lock:
            EventTrap.current = self
            return self

    def __exit__(self, type, value, tb):
        with EventTrap.lock:
            EventTrap.current = None

    @classmethod
    def set_exception(cls, exception):
        with cls.lock:
            if cls.current and not cls.current.exception:
                cls.current.exception = exception

    @classmethod
    def get_exception(cls):
        with cls.lock:
            if cls.current:
                return cls.current.exception
            else:
                return None


def mbs_event_handler(func):
    """
    A decorator for MBS event handlers. It implements common tasks which should otherwise
    be repeated in every MBS event handler, for example:

      - at the end of handler, call events.scheduler.run().
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            EventTrap.set_exception(e)
            raise e
        finally:
            scheduler.run()
    # save origin function as functools.wraps from python2 doesn't preserve the signature
    if not hasattr(wrapper, "__wrapped__"):
        wrapper.__wrapped__ = func
    return wrapper
