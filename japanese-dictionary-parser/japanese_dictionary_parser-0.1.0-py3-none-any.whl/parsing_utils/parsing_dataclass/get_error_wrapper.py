from functools import wraps
from dataclasses import dataclass


def get_empty_error(func=None) -> (dataclass, str | None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        datacls = func(*args, **kwargs)
        if datacls.is_empty:
            return (datacls, type(datacls).__name__)
        return (datacls, None)
    return wrapper
