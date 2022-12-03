# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import logging
import os
from logging.config import dictConfig, fileConfig

from baitoolkit.parallel.mutex import RWLock

__LOGGERS = dict()

__lock = RWLock()

__ROOT_LOGGER_NAME = "None"


def get_logger(name):
    """Get Logger."""
    global __LOGGERS, __lock, __ROOT_LOGGER_NAME
    with __lock.reader():
        if name is None:
            name = __ROOT_LOGGER_NAME
        logger = __LOGGERS.get(name)
        if logger is None:
            logger = logging.getLogger(name)
            __LOGGERS[name] = logger
        return logger


def dict_config(configs, attach_pid=False):
    """Configure logging
    @param dict configs:
    @param bool attach_pid: Attach pid to the filename being logged to.
    """
    global __lock, __LOGGERS, __ROOT_LOGGER_NAME
    with __lock.reader():
        if attach_pid:
            handlers = configs.get('handlers')
            for handler in handlers.values():
                if 'filename' in handler:
                    handler['filename'] = attach_pid_to_filename(handler['filename'])
        dictConfig(configs)
        for key in __LOGGERS.keys():
            key = None if key == __ROOT_LOGGER_NAME else key
            logger = logging.getLogger(key)
            __LOGGERS[key].handlers = logger.handlers
    return True


def file_config(file_path):
    """Configure logging
    @param str file_path:
    """
    fileConfig(file_path)
    return True


def attach_pid_to_filename(filename):
    """Attach pid to filename."""
    i = filename.rfind('.')
    pid = str(os.getpid())
    if i == -1:
        filename = filename + '_' + pid
    else:
        filename = filename[:i] + '_' + pid + filename[i:]
    return filename
