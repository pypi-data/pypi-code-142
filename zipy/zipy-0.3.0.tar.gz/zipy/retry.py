import asyncio
import time
from typing import Iterable
from zipy import inspect


__all__ = ["retry"]


def retry(*, times: int = 1, wait: float = 0, exceptions: Iterable = [Exception]):
    """
    Decorator that retry function when specfic exception occurs
    The Function can be normal or coroutine function

    :param times: how much times to retry
    :param wait: time interval in seconds between two retries
    :param exceptions: Only exception occured is instance of any of these exceptions, it would retry
    :return: decorator
    :raises ValueError: raises if times or wait if negative number
    :raises ValueError: raises if object be decorated is neither coroutine nor normal function
    :raises TypeError: raises if type of exceptions is not iterable
    """
    if times < 0:
        raise ValueError("times must not be negative")
    if wait < 0:
        raise ValueError("wait must not be negative")
    if not hasattr(exceptions, "__iter__"):
        raise TypeError("exceptions is not iterable")

    def decorator(func):
        if asyncio.iscoroutinefunction(func):

            async def wrapper(*args, **kwargs):
                for ntry in range(times):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as exc:
                        if ntry == times - 1:
                            raise exc
                        if any(
                            map(lambda c: isinstance(exc, c), exceptions)  # noqa: F821
                        ):
                            await asyncio.sleep(wait)
                        else:
                            raise exc

            return wrapper
        elif inspect.isnormalfunc(func):

            def wrapper(*args, **kwargs):
                for ntry in range(times):
                    try:
                        return func(*args, **kwargs)
                    except Exception as exc:
                        if ntry == times - 1:
                            raise exc
                        if any(
                            map(lambda c: isinstance(exc, c), exceptions)  # noqa: F821
                        ):
                            time.sleep(wait)
                        else:
                            raise exc

            return wrapper
        else:
            raise ValueError(f"{func} is neither coroutine nor normal function")

    return decorator
