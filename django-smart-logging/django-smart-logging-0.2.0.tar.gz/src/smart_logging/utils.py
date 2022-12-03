import socket
import types
from functools import lru_cache
from inspect import isclass

import redis


@lru_cache(None)
def get_redis_connection() -> redis.client.Redis:
    from . import conf

    return redis.from_url(conf.SMART_LOG_REDIS)


@lru_cache(100)
def fqn(o, silent=False, from_module=None):
    """Returns the fully qualified class name of an object or a class

    :param o: object or class
    :return: class name
    """
    parts = []
    if isinstance(o, (str, bytes)):
        return o
    if not hasattr(o, "__module__"):
        if silent:
            return
        raise ValueError("Invalid argument `%s` %s" % (type(o), o))
    parts.append(o.__module__)
    if isclass(o):
        parts.append(o.__name__)
    elif isinstance(o, types.FunctionType):
        parts.append(o.__name__)
    else:
        parts.append(o.__class__.__name__)
    return ".".join(parts)


@lru_cache(maxsize=None)
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(("10.254.254.254", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP
