import gevent.monkey
gevent.monkey.patch_all()
from .._version import __version__
from loguru import logger


class Logger(object):

    is_close = False

    @classmethod
    def close_logger(cls, *args, **kwargs):
        ...

    @classmethod
    def debug(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.debug(*args, **kwargs)

    @classmethod
    def info(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.info(*args, **kwargs)

    @classmethod
    def error(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.error(*args, **kwargs)

    @classmethod
    def warning(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.warning(*args, **kwargs)

    @classmethod
    def exception(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.exception(*args, **kwargs)

    @classmethod
    def catch(cls, *args, **kwargs):
        if cls.is_close is True:
            cls.close_logger(*args, **kwargs)
        else:
            logger.catch(*args, **kwargs)

    @classmethod
    def start(cls):
        cls.is_close = False

    @classmethod
    def stop(cls):
        cls.is_close = True

    @classmethod
    def get_status(cls):
        return cls.is_close


debug = Logger.debug
info = Logger.info
error = Logger.error
warning = Logger.warning
exception = Logger.exception
catch = Logger.catch
start = Logger.start
stop = Logger.stop
get_status = Logger.get_status
info("autoScheme Version:{}".format(__version__))
