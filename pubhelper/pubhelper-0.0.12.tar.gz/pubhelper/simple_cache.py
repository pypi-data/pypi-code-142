import threading
from typing import Any, Optional
from weakref import WeakValueDictionary


class CachedManager(WeakValueDictionary):
    """
    局部变量，新建缓存，当局部变量被销毁时，缓存也会被清除
    """
    thread_lock: threading.Lock = threading.Lock()

    def get(self, key: Any) -> Optional[Any]:
        with self.thread_lock:
            if not super(CachedManager, self).get(key):
                data = CacheItem()
                self.__setitem__(key, data)
            return super(CachedManager, self).get(key)


class CacheItem(dict):
    m: CachedManager = CachedManager()

    def set(self, **kwargs):
        [self.__setitem__(k, v) for k, v in kwargs.items()]


__all__ = ('CacheItem',)
