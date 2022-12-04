# -*- coding: utf-8 -*-

import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

# constants for logging levels
NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARN = logging.WARN
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


# Powershell and cmd are not supported
Colors = {
    'DEBUG':    ('\033[34m', '\033[0m',),
    'INFO':     ('\033[0m',  '\033[0m',),
    'WARNING':  ('\033[33m', '\033[0m',),
    'WARN':     ('\033[33m', '\033[0m',),
    'ERROR':    ('\033[31m', '\033[0m',),
    'CRITICAL': ('\033[31m', '\033[0m',),
}


# Constants for Zip file compression methods
ZIP_STORED = 0
ZIP_DEFLATED = 8
ZIP_BZIP2 = 12
ZIP_LZMA = 14
# Other ZIP compression methods not supported


ZipSuffixDict = {
    ZIP_STORED: '',
    ZIP_DEFLATED: 'zip',
    ZIP_BZIP2: 'bz2',
    ZIP_LZMA: 'lz',
}


def lookup_zip_format(comp):
    if comp in ZipSuffixDict:
        return ZipSuffixDict[comp]
    return ZIP_STORED


class ColoredPercentStyle(logging.PercentStyle):
    """
    Colored stream style for percent formatter.
    """
    def __init__(self, fmt: str, stream=False):
        super().__init__(fmt)
        self.stream = stream

    # Python 3.9 or newer
    def _format(self, record):
        filler = record.__dict__
        if self.stream:
            pre, sub = Colors[record.levelname]
            # Align left for levelname
            if 'levelname' in filler:
                filler['levelname'] = '{:8}'.format(filler['levelname'])
            return pre + self._fmt % filler + sub
        else:
            return self._fmt % filler

    # Python 3.8 or old
    def format(self, record):
        return self._format(record)


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, stream=False):
        # Need to be aware of differences in the logging of different Python versions
        args = [fmt, datefmt, style]
        if (sys.version_info.major == 3) and (sys.version_info.minor >= 9):
            args.append(validate)
        super(self.__class__, self).__init__(*args)
        # Use ColoredPercentStyle instead of logging.PercentStyle
        self._style = ColoredPercentStyle(fmt, stream)


class ColoredTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backup_count=0,
                 encoding=None, delay=False, utc=False, at_time=None,
                 errors=None, compression=None):
        # Need to be aware of differences in the logging of different Python versions
        args = [filename, when, interval, backup_count, encoding, delay, utc, at_time]
        if (sys.version_info.major == 3) and (sys.version_info.minor >= 9):
            args.append(errors)
        super(self.__class__, self).__init__(*args)
        # Whether to enable compression
        self.compression = compression

    @staticmethod
    def _compress(source, target, compression):
        _root = Path(__file__).parent
        cmds = [
            sys.executable,
            f"{_root.joinpath('compress.py')}",
            '-s',
            source,
            '-t',
            target,
            '-c',
            ZipSuffixDict[compression]
        ]
        os.popen(' '.join(cmds))

    def rotate(self, source, dest):
        compression = self.compression
        if compression:
            if os.path.exists(source):
                os.rename(source, dest)
            suffix = lookup_zip_format(compression)
            target = f'{dest}.{suffix}'
            self._compress(dest, target, self.compression)
        else:
            if not callable(self.rotator):
                if os.path.exists(source):
                    os.rename(source, dest)
            else:
                self.rotator(source, dest)


class ColoredManager(logging.Manager):
    __loggers = {}

    # Return ColoredLogger instead of logging.Logger
    def getLogger(self, name: str) -> 'ColoredLogger':
        return self.__loggers.setdefault(name, ColoredLogger(name))


class ColoredLogger(logging.Logger):
    formatter = "%(asctime)s | %(levelname)s | <%(threadName)s %(thread)d> " \
                "| %(filename)s:%(lineno)d - %(message)s"
    stream_handler = None
    file_handler = None

    def __init__(self, name: str, *, path='.', level: [int, str] = NOTSET, stream_handler=True,
                 file_handler=False, compression=ZIP_BZIP2):
        super(self.__class__, self).__init__(name, level)
        self.path = path
        if compression and compression not in ZipSuffixDict:
            raise ValueError(f'Unsupported compression method: {compression}')
        self.compression = compression
        if stream_handler:
            self.enable_stream_handler(level)
        if file_handler:
            self.enable_file_handler(level)

    def enable_stream_handler(self, level=None):
        if self.stream_handler:
            return
        lev = level or self.level
        fmt = ColoredFormatter(self.formatter, stream=True)
        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.stream_handler.setLevel(lev)
        self.stream_handler.setFormatter(fmt)
        super().addHandler(self.stream_handler)

    def enable_file_handler(self, level=None, when='D', interval=1, backup=10, encoding='utf-8'):
        if self.file_handler:
            return
        name = self.name if self.name.endswith('.log') else f'{self.name}.log'
        folder = Path(self.path)
        if not folder.exists():
            folder.mkdir(exist_ok=True)
        file = folder.joinpath(name)
        lev = level or self.level
        fmt = ColoredFormatter(self.formatter, stream=False)
        self.file_handler = ColoredTimedRotatingFileHandler(
            file,
            when=when,
            interval=interval,
            backup_count=backup,
            encoding=encoding,
            compression=self.compression,
        )
        self.file_handler.setLevel(lev)
        self.file_handler.setFormatter(fmt)
        super().addHandler(self.file_handler)


root = logging.RootLogger(WARNING)
ColoredLogger.root = root
ColoredLogger.manager = ColoredManager(ColoredLogger.root)


def get_logger(name=None, stream=True, to_file=True):
    _name = name or 'log'
    lg: ColoredLogger = ColoredLogger.manager.getLogger(_name)
    if stream:
        lg.enable_stream_handler()
    if to_file:
        lg.enable_file_handler()
    return lg
