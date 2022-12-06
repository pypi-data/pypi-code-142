from .ratelimit.models import RateLimitManager
from .ratelimit.utils import ForUser, ForIp, RateTime, Block
from functools import wraps
from .utils import get_ip
from .serializer import JsonSerializer as Js


def rate_limit(model: ForUser or ForIp, rate_time: RateTime, block: Block):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if model.model == "user":
                user_or_ip = args[0].user
            if model.model == "ip":
                user_or_ip = get_ip(args[0])
            if RateLimitManager(model).check(user_or_ip, rate_time, block):
                return func(*args, **kwargs)
            return Js.http_403_forbidden()
        return wrapper
    return decorator
