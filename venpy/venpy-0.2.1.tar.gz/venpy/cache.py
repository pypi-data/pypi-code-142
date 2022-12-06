from __future__ import annotations

import inspect

import wrapt

CACHE_KEY = "__justcache"
SIG_KEY = "__sig"


def get_cache_data(wrapped, instance) -> dict:
    if instance is None:
        return vars(wrapped).setdefault(CACHE_KEY, {})
    else:
        # https://github.com/openstack-archive/deb-python-wrapt/blob/master/blog/07-the-missing-synchronized-decorator.md#storing-a-meta-lock-on-the-decorator
        instance_dict = vars(instance)
        # NOTE that this is no longer thread-safe - we can use the locking
        # technique in the blog post above to fix it if we want
        if CACHE_KEY not in instance_dict:
            setattr(instance, CACHE_KEY, {})
        return instance_dict[CACHE_KEY].setdefault(wrapped.__name__, {})


def cache_key(cache_data, wrapped, args, kwargs) -> int:
    # Also see: https://github.com/tkem/cachetools/blob/master/src/cachetools/keys.py
    #
    # Note that `args` already does not contain instance, in the case of bound methods

    if SIG_KEY not in cache_data:
        cache_data[SIG_KEY] = inspect.signature(wrapped)

    ba = cache_data[SIG_KEY].bind(*args, **kwargs)
    return hash(tuple(ba.arguments.items()))


@wrapt.decorator
def cache(wrapped, instance, args, kwargs):
    cache_data = get_cache_data(wrapped, instance)
    key = cache_key(cache_data, wrapped, args, kwargs)

    if key not in cache_data:
        cache_data[key] = wrapped(*args, **kwargs)
    return cache_data[key]
