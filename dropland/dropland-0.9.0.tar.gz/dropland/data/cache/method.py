import asyncio
import operator
from datetime import timedelta
from functools import reduce
from typing import Any, Dict, Optional, Sequence, Tuple

from dropland.data.cache.base import CacheData, ModelCache
from dropland.util import calculate_digest


class MethodCache:
    def __init__(self, gateway: ModelCache, ttl: Optional[timedelta] = None):
        self._gateway = gateway
        self._ttl = ttl

    @property
    def gateway(self) -> ModelCache:
        return self._gateway

    def get_model_cache_key(self) -> str:
        return self._gateway.get_model_cache_key()

    def get_cache_id(self, id_value: Any) -> str:
        return self._gateway.get_cache_id(id_value)

    def get_cache_key(self, id_value: Any) -> str:
        return self._gateway.get_cache_key(id_value)

    @staticmethod
    def cache_key_for(method: str, args: Optional[Dict[str, Any]] = None) -> str:
        id_data = [method]

        if args:
            id_data.append(calculate_digest(args))
        else:
            id_data.append('_')

        return ':'.join(id_data)

    async def put(self, method: str, args: Optional[Dict[str, Any]] = None,
                  data: Optional[Any] = None, cache_key: Optional[str] = None,
                  ttl: Optional[timedelta] = None, **kwargs) -> bool:
        cache_key = cache_key or self.cache_key_for(method, args)
        data = CacheData(cache_id=cache_key, data=data)
        return await self._gateway.cache_one(data, ttl=ttl or self._ttl, **kwargs)

    async def get(self, method: str, args: Optional[Dict[str, Any]] = None,
                  cache_key: Optional[str] = None, **kwargs) -> Tuple[bool, Optional[Any]]:
        cache_key = cache_key or self.cache_key_for(method, args)
        exists, data = await self._gateway.load_one(self.get_cache_key(cache_key), **kwargs)
        return exists, data

    async def drop(self, method: str, args: Optional[Dict[str, Any]] = None,
                   cache_key: Optional[str] = None) -> bool:
        cache_key = cache_key or self.cache_key_for(method, args)
        return await self._gateway.drop_one(self.get_cache_key(cache_key))

    async def drop_all(self, methods: Sequence[str] = None) -> int:
        methods = methods if methods else list()
        if not methods:
            return await self._gateway.drop_all()
        results = await asyncio.gather(
            *(self._gateway.drop_all(method) for method in methods)
        )
        return reduce(operator.add, results, 0)
