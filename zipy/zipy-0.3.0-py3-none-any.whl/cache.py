import time
from zipy import inspect


def cache(*, ttl: float = 0):
    """
    Cache result of function. function can be either normal ,coroutine or asyncgen function

    :param ttl: time to live in seconds. ttl <= 0 means forever
    :raise ValueError: raises if func is neither normal, coroutine nor asyncgen function
    :return: decorator
    """

    def decorator(func):
        cached = None
        birthday = 0

        if inspect.iscoroutinefunction(func):

            async def wrapper(*args, **kwargs):
                nonlocal cached, birthday
                isforever = ttl <= 0
                isexpired = time.time() - birthday >= ttl
                if cached and (isforever or (not isexpired)):
                    return cached
                else:
                    res = await func(*args, **kwargs)
                    cached = res
                    birthday = time.time()
                    return res

            return wrapper
        elif inspect.isnormalfunc(func):

            def wrapper(*args, **kwargs):
                nonlocal cached, birthday
                isforever = ttl <= 0
                isexpired = time.time() - birthday >= ttl
                if cached and (isforever or (not isexpired)):
                    return cached
                else:
                    res = func(*args, **kwargs)
                    cached = res
                    birthday = time.time()
                    return res

            return wrapper
        elif inspect.isasyncgenfunction(func):

            async def wrapper(*args, **kwargs):
                nonlocal cached, birthday
                isforever = ttl <= 0
                isexpired = time.time() - birthday >= ttl
                if cached and (isforever or (not isexpired)):
                    for ele in cached:
                        yield ele
                else:
                    cached = []
                    birthday = time.time()
                    async for ele in func(*args, **kwargs):
                        cached.append(ele)
                        yield ele

            return wrapper
        else:
            raise ValueError(
                f"{func} is neither normal, coroutine nor asyncgen function"
            )

    return decorator
