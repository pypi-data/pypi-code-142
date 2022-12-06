#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Contains Lock class.
Can be used to generate a temporary file in the output directory.
This file is created at the beginning of the run and automatically deleted at the end.

This functionality can be used to preserve from processes overlapping, in order to indicate
current process is still running.
(e.g., moving files that are being written).
"""

import os
from pathlib import Path

from poppy.core.logger import logger

__all__ = ['LockFile']

class LockFile:

    def __init__(self,
                 lock_filename=None,
                 lock_dirpath=None):

        self._started = False

        self.dirpath = lock_dirpath
        self.filename = lock_filename

    @property
    def dirpath(self):
        return self._dirpath

    @dirpath.setter
    def dirpath(self, value):
        self._dirpath = value

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def start(self):

        filepath = self.path()
        if self._started:
            logger.debug('Locking has been already started')
        elif not filepath:
            logger.debug('Locking not started: lock filepath not fully defined!')
            self._started = False
        else:
            try:
                # Make sure that lock file directory exists
                os.makedirs(self.dirpath, exist_ok=True)
                Path(filepath).touch()
            except FileExistsError:
                logger.warning(f'{filepath} already exists and cannot be used as a lock file!')
            else:
                self._started = True
                logger.debug(f'Locking started ({filepath} created)')

    def stop(self):

        # If locking has been started (i.e., started = True)
        # and lock file exists
        # then delete it and stop the locking (i.e., started = False)
        if self._started:
            filepath = self.path()
            if filepath and os.path.isfile(filepath):
                os.remove(filepath)

            self._started = False
            logger.debug(f'Locking stopped ({filepath} removed)')

    def path(self):
        if self.dirpath and self.filename:
            return os.path.join(self.dirpath, self.filename)
        else:
            return None
