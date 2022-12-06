#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import logging

from poppy.core.logger import logger
import sys


__all__ = ["DescriptorLoadError",
            "MissingArgument",
           "MissingProperty",
           "MissingInput",
           "TargetFileNotSaved",
            "print_exception",
            "exception_hook"]

def exception_hook(exctype, value, traceback):
    """Tailored version of the excepthook
    can be used to only print full traceback in DEBUG mode.
    To activate it, add the line sys.excepthook = exception_hook in the code.
    See https://stackoverflow.com/questions/6598053/python-global-exception-handling/6598286#6598286"""
    if logger.getEffectiveLevel() == logging.DEBUG:
        sys.__excepthook__(exctype, value, traceback)

class DescriptorLoadError(Exception):
    """Exception raised when a descriptor file cannot be loaded."""
    def __init__(self, message, *args, **kwargs):
        super(DescriptorLoadError, self).__init__(*args, **kwargs)
        logger.error(message)
        self.message = message

    pass

class MissingInput(Exception):
    """Exception raised if an input target is missing."""
    def __init__(self, message, *args, **kwargs):
        super(MissingInput, self).__init__(*args, **kwargs)
        logger.error(message)
        self.message = message

    pass


class MissingArgument(Exception):
    """
    Exception raised when input argument is missing
    """
    def __init__(self, message, *args, **kwargs):
        super(MissingArgument, self).__init__(*args, **kwargs)
        logger.error(message)
        self.message = message

    pass

class MissingProperty(Exception):
    """Exception raised if a pipeline property is missing."""

    def __init__(self, message, *args, **kwargs):
        super(MissingProperty, self).__init__(*args, **kwargs)
        logger.error(message)
        self.message = message

    pass


class TargetFileNotSaved(Exception):
    """Exception raised if target file not saved correctly."""
    def __init__(self, message, *args, **kwargs):
        super(TargetFileNotSaved, self).__init__(*args, **kwargs)
        logger.error(message)
        self.message = message

    pass

def print_exception(message=None, log_level='error', use_traceback=True):
    """
    To handle the printing of the exception message when one occurred. Particularly
    useful when catching errors and want to add debug information on the same
    time.
    """
    # set the available levels

    logging_function_dict = {'info': logger.info,
                             'warning': logger.warning,
                             'error': logger.error,
                             'critical': logger.critical,
                             'exception': logger.exception, }

    logging_function = logging_function_dict.get(log_level, logger.error)

    if use_traceback:
        # get the traceback
        trace = traceback.format_exc()
    else:
        trace=''

    # if not message provided, get the traceback of errors to be a little more
    # useful for the developer
    if message is not None:
        mess = "\n".join([trace, message])
    else:
        # else use message provided by developer
        mess = trace

    # show error in the logger
    logging_function(mess)

    # return the message
    return mess