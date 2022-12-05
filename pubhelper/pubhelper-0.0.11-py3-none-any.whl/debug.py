import functools
import logging
import time
from retry_wraps import retry_wraps as r


def timethis(fn=None, *, logger=None):
    """统计代码执行时间"""

    def inner(f):
        @functools.wraps(f)
        def _inner(*args, **kwargs):
            start = time.perf_counter()
            data = f(*args, **kwargs)
            end = time.perf_counter()
            logger.debug(f'func({f.__name__}): {(end - start) * 1000} ms')
            return data

        return _inner

    if not logger:
        logger = logging.getLogger('__time_count__')
    logger.setLevel(logging.DEBUG)
    return callable(fn) and inner(fn) or inner


def with_log(fn=None, *, logger=None, is_debug=True):
    """打印日志"""

    def inner(f):
        @functools.wraps(f)
        def _inner(*args, **kwargs):
            is_debug and logger.debug(
                f'func({f.__name__}) running(args={args}, kwargs={kwargs})')
            result = r(f)(*args, **kwargs)
            is_debug and logger.debug(f'func({f.__name__}) result: {result}')
            return result

        return _inner

    if not logger:
        logger = logging.getLogger('__debug__')
    logger.setLevel(logging.DEBUG)
    return callable(fn) and inner(fn) or inner


__all__ = ('with_log', 'timethis')
