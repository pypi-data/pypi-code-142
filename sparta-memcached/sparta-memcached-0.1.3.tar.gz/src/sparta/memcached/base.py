import abc
import functools
import inspect


class SpartaCache(abc.ABC):
    def __init__(
        self,
        key_prefix=None,
    ):
        self.key_prefix = key_prefix if isinstance(key_prefix, str) else str(key_prefix)

    def _map_key(self, key):
        return self.key_prefix + key if self.key_prefix else key

    @abc.abstractmethod
    def add(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def append(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def cas(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def decr(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def gets(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def incr(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def prepend(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def replace(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set(self, key, *args, **kwargs):
        pass

    @abc.abstractmethod
    def touch(self, key, *args, **kwargs):
        pass

    def func_decorator(
        self,
        key: str,
        time: int = None,
        expiration: int = None,  # TODO remove expiration on next release
    ):
        """
        Use to annotate any method to cache its result.
        @param key: the cache key
        @param time: the cache expiration for current key
        @param expiration: DEPRECATED: use `time` instead

        Example:
            ```
            @cache.func_decorator("my-key", time=3600):
            def do_stuff():
                ...
            ```
        The code here above will store in cache (with expiration 1h) the result of `do_stuff`. Any following
        invocation of `do_stuff`, withing the cache expiration time, will return the cached value.
        """

        def from_cache():
            return self.get(key)

        def to_cache(value):
            self.set(key, value, time if time is not None else expiration)

        def decorator(f):

            if inspect.iscoroutinefunction(f):

                async def async_wrapped_function(*args, **kwargs):
                    _result = from_cache()
                    if _result is None:
                        _result = await f(*args, **kwargs)
                        to_cache(_result)
                    return _result

                return functools.update_wrapper(async_wrapped_function, f)

            else:

                def wrapped_function(*args, **kwargs):
                    _result = from_cache()
                    if _result is None:
                        _result = f(*args, **kwargs)
                        to_cache(_result)
                    return _result

                return functools.update_wrapper(wrapped_function, f)

        return decorator

    def atomic_append(self, key, value, _retries=3, *args, **kwargs):
        """
        Required cas behavior!
        Assures atomic append to a list of objects (only tuple is supported, not list).
        Solution copied from https://stackoverflow.com/a/27468294/20230162
        """
        try:
            _values, cas_id = self.gets(key)
        except ValueError as e:
            raise RuntimeError("atomic_append requires cas behavior") from e
        if _values is None:
            self.set(key, (value,), *args, **kwargs)
        else:
            if value not in _values:
                ok = self.cas(key, _values + (value,), cas_id, *args, **kwargs)
                if not ok and _retries > 1:
                    self.atomic_append(key, value, _retries - 1, *args, **kwargs)
