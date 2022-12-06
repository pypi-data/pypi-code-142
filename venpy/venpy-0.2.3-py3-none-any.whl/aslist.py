from __future__ import annotations

from wrapt import decorator


@decorator
def aslist(wrapped, _instance, args, kwargs):
    "Function decorator to transform a generator into a list"

    return list(wrapped(*args, **kwargs))
