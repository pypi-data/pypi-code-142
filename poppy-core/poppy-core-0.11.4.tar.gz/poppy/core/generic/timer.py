#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pipeline Timer
"""

import threading

from poppy.core.generic.signals import Signal

__all__ = ["Timer"]


class Timer(object):
    """
    A class timer to make periodic calls to a given function or single shot
    calls after a given amount of time.
    """
    def __init__(self):
        # the signal to emit when the time ended
        self.timeout = Signal()

        # initiate some variables
        self._timer = None
        self._timerSingle = None

    def _run(self):
        # create a new timer with the specified time
        self._timer = threading.Timer(self._time, self._run)
        self._timer.start()

        # emit the signal to inform connected slots
        self.timeout()

    def singleShot(self, time=None):
        """
        To run the timer just one time after a given delay.
        """
        self._timerSingle = threading.Timer(time, self.timeout)
        self._timerSingle.start()

    def start(self, time):
        """
        To start the periodic timer.
        """
        self._time = time
        self._timer = threading.Timer(self._time, self._run)
        self._timer.start()

    def stop(self):
        """
        To stop the timer, if it is periodic or single shot.
        """
        if self._timer:
            self._timer.cancel()
        if self._timerSingle:
            self._timerSingle.cancel()


# vim: set tw=79 :
