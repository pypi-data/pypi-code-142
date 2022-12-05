#
#   Lightnet logger: Logging functionality used within the lightnet package
#   Copyright EAVISE
#
#   NOTE:
#       The contents here are mostly obsolete and deprecated.
#       It is not recommended to forcefully set logging handlers, which is what happened here.
#       The code below is here for compatibility reasons and is cleaned up, such that people who wish to keep using the lightnet logging functionality,
#       need to call `create_stream_handler()` and `create_file_handler()` manually.
#
import os
import sys
import logging
import copy
from enum import Enum

__all__ = ['create_file_handler', 'create_stream_handler']


# Formatter
class ColorCode(Enum):
    """ Color Codes """
    RESET = '\033[00m'
    BOLD = '\033[01m'

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'
    GRAY = '\033[1;30m'


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, color=True, **kwargs):
        logging.Formatter.__init__(self, msg, **kwargs)
        self.color = color
        self.color_codes = {
            'CRITICAL': ColorCode.RED,
            'ERROR': ColorCode.RED,
            'DEPRECATED': ColorCode.YELLOW,
            'EXPERIMENTAL': ColorCode.YELLOW,
            'WARNING': ColorCode.YELLOW,
            'INFO': ColorCode.WHITE,
            'DEBUG': ColorCode.GRAY,
        }

    def format(self, record):
        record = copy.copy(record)
        levelname = record.levelname
        if self.color:
            color = self.color_codes[levelname] if levelname in self.color_codes else ''
            record.levelname = f'{ColorCode.BOLD.value}{color.value}{levelname:10}{ColorCode.RESET.value}'
        else:
            record.levelname = f'{levelname:10}'
        return logging.Formatter.format(self, record)

    def setColor(self, value):
        self.color = value


# Filter
class LevelFilter(logging.Filter):
    def __init__(self, levels, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.levels = levels

    def filter(self, record):
        return self.levels is None or record.levelname in self.levels


# Logger
class LightnetLogger(logging.getLoggerClass()):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.error_msg = set()

    def error_once(self, msg, *args, **kwargs):
        if self.isEnabledFor(40) and msg not in self.error_msg:
            self.error_msg.add(msg)
            self._log(40, msg, args, **kwargs)


logging.setLoggerClass(LightnetLogger)


# Console Handler
def create_stream_handler():
    """
    Create a handler to write lightnet log messages to the console.

    The default LogLevel is INFO, but this can be changed with the `LN_LOGLVL` environment variable,
    or by calling the `setLevel()` method on the returned StreamHandler.
    """
    logger = logging.getLogger('lightnet')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(ColoredFormatter('{levelname} {message}', style='{'))

    if 'LN_LOGLVL' in os.environ:
        lvl = os.environ['LN_LOGLVL'].upper()
        try:
            ch.setLevel(int(lvl))
        except ValueError:
            ch.setLevel(lvl)

        if ch.level <= 10:
            ch.setFormatter(ColoredFormatter('{levelname} [{name}] {message}', style='{'))
    else:
        ch.setLevel(logging.INFO)

    # Disable color if ANSI not supported -> Code taken from django.core.management.color.supports_color
    # Note that if you use the colorama plugin, you can reenable the colors
    supported_platform = sys.platform != 'Pocket PC' and (sys.platform != 'win32' or 'ANSICON' in os.environ)
    is_a_tty = hasattr(ch.stream, 'isatty') and ch.stream.isatty()
    if not supported_platform or not is_a_tty:
        ch.formatter.setColor(False)

    logger.addHandler(ch)
    return ch


# File Handler
def create_file_handler(self, filename, levels=None, filemode='a'):
    """ Create a file to write lightnet log messages of certaing levels """
    logger = logging.getLogger('lightnet')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename=filename, mode=filemode)
    fh.setLevel(logging.NOTSET)
    fh.addFilter(LevelFilter(levels))
    fh.setFormatter(logging.Formatter('{levelname} [{name}] {message}', style='{'))
    logger.addHandler(fh)
    return fh
