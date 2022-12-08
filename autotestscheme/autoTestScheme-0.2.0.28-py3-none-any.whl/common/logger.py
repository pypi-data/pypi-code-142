import gevent.monkey
gevent.monkey.patch_all()
from .._version import __version__
from loguru import logger

is_close = False


def close_logger(*args, **kwargs):
    ...


class Logger(object):

    @classmethod
    def debug(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.debug(*args, **kwargs)

    @classmethod
    def info(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.info(*args, **kwargs)

    @classmethod
    def error(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.error(*args, **kwargs)

    @classmethod
    def warning(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.warning(*args, **kwargs)

    @classmethod
    def exception(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.exception(*args, **kwargs)

    @classmethod
    def catch(cls, *args, **kwargs):
        if is_close is True:
            close_logger(*args, **kwargs)
        else:
            logger.catch(*args, **kwargs)


debug = Logger.debug
info = Logger.info
error = Logger.error
warning = Logger.warning
exception = Logger.exception
catch = Logger.catch
info("autoScheme Version:{}".format(__version__))


