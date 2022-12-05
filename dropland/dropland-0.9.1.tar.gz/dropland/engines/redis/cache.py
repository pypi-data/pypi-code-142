from collections import OrderedDict
from datetime import timedelta
from typing import Any, AsyncGenerator, Dict, Optional, Sequence, Tuple

from dropland.data.cache.base import CacheData, ModelCache, ScanCacheMixin
from dropland.data.serializers import Deserializer, Serializer
from .engine import RedisEngine


class SimpleRedisCache(ScanCacheMixin, ModelCache):
    def __init__(self, engine: RedisEngine, class_key: str,
                 serializer: Serializer, deserializer: Deserializer, ttl_enabled: bool = True):
        self._engine = engine
        self._class_key = class_key
        self._serializer = serializer
        self._deserializer = deserializer
        self._ttl_enabled = ttl_enabled
        self._null_data = self._serializer.serialize(None)

    def get_model_cache_key(self) -> str:
        return f'{self._engine.name}.models.{self._class_key}'

    async def cache_one(self, data: CacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        cache_kwargs = dict()

        if self._ttl_enabled:
            expiration = ttl or self._engine.default_ttl
            total_seconds = expiration.total_seconds()

            if total_seconds > 1:
                cache_kwargs['expire'] = int(total_seconds)
            elif 0 < total_seconds < 1:
                cache_kwargs['pexpire'] = int(total_seconds * 1000)
            else:
                total_seconds = self._engine.default_ttl.total_seconds()
                cache_kwargs['expire'] = int(total_seconds) if total_seconds > 1 else 60

        serialized = self._serializer.serialize(data.data)

        async with self._engine.session() as session:
            return bool(await session.set(self.get_cache_key(data.cache_id), serialized, **cache_kwargs))

    async def cache_many(self, objects: Sequence[CacheData], ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if not objects:
            return False
        res = False

        async with self._engine.session() as session:
            tx = session.multi_exec()

            for instance in objects:
                cache_kwargs = dict()

                if self._ttl_enabled:
                    expiration = ttl or self._engine.default_ttl
                    total_seconds = expiration.total_seconds()

                    if total_seconds > 1:
                        cache_kwargs['expire'] = int(total_seconds)
                    elif 0 < total_seconds < 1:
                        cache_kwargs['pexpire'] = int(total_seconds * 1000)
                    else:
                        total_seconds = self._engine.default_ttl.total_seconds()
                        cache_kwargs['expire'] = int(total_seconds) if total_seconds > 1 else 60

                serialized = self._serializer.serialize(instance.data)
                tx.set(self.get_cache_key(instance.cache_id), serialized, **cache_kwargs)

            for r in await tx.execute():
                res |= r

        return bool(res)

    async def load_one(self, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        async with self._engine.session() as session:
            if res := await session.get(cache_key):
                return True, self._deserializer.deserialize(res)
        return False, None

    async def load_many(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[Dict[str, Any]]]:
        if not indices:
            return []

        cache_keys = [self.get_cache_key(id_value) for id_value in indices]

        async with self._engine.session() as session:
            res = await session.mget(*cache_keys)

        objects: Dict[Any, Any] = OrderedDict()

        for id_value, data in zip(indices, res):
            objects[id_value] = self._deserializer.deserialize(data) if data is not None else None

        return list(objects.values())

    async def drop_one(self, cache_key: str) -> bool:
        async with self._engine.session() as session:
            return bool(await session.delete(cache_key))

    async def drop_many(self, indices: Sequence[Any] = None) -> int:
        async with self._engine.session() as session:
            if indices and len(indices) > 0:
                cache_keys = [self.get_cache_key(id_value) for id_value in indices]
            else:
                model_cache_key = self.get_model_cache_key()
                cache_keys = await session.keys(f'{model_cache_key}:*')

            return int(await session.delete(*cache_keys)) if cache_keys else 0

    async def drop_all(self, prefix: Optional[str] = None) -> int:
        model_cache_key = self.get_model_cache_key()
        async with self._engine.session() as session:
            cache_key = f'{model_cache_key}:{prefix}*' if prefix else f'{model_cache_key}:*'
            keys_to_delete = await session.keys(cache_key)
            return int(await session.delete(*keys_to_delete)) if keys_to_delete else 0

    async def exists(self, cache_key: str) -> bool:
        async with self._engine.session() as session:
            if await session.exists(cache_key):
                return await session.get(cache_key) != self._null_data
        return False

    async def scan(self, cache_key: Optional[str] = None, match: Optional[str] = None, count: Optional[int] = None) \
            -> AsyncGenerator[Tuple[str, Optional[Any]], None]:
        match = f'{cache_key}:{match}' if cache_key and match else match
        async with self._engine.session() as session:
            async for k in session.iscan(match=match, count=count):
                cache_key = k.decode('utf-8')
                k = cache_key.split(':')[1] if ':' in cache_key else cache_key
                v = (await self.load_one(cache_key))[1]
                yield k, v


class HashRedisCache(ScanCacheMixin, ModelCache):
    def __init__(self, engine: RedisEngine, class_key: str,
                 serializer: Serializer, deserializer: Deserializer, ttl_enabled: bool = True):
        self._engine = engine
        self._class_key = class_key
        self._serializer = serializer
        self._deserializer = deserializer
        self._ttl_enabled = ttl_enabled
        self._null_data = self._serializer.serialize(None)

    def get_model_cache_key(self) -> str:
        return f'{self._engine.name}.models.{self._class_key}'

    async def cache_one(self, data: CacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        model_cache_key, cache_id = self.get_model_cache_key(), self.get_cache_id(data.cache_id)
        serialized = self._serializer.serialize(data.data)

        async with self._engine.session() as session:
            if not self._ttl_enabled:
                return bool(await session.hset(model_cache_key, cache_id, serialized))

            res = False
            tx = session.multi_exec()
            expiration = ttl or self._engine.default_ttl
            tx.hset(model_cache_key, cache_id, serialized)
            tx.expire(model_cache_key, int(expiration.total_seconds()))

            for r in await tx.execute():
                res |= r

        return bool(res)

    async def cache_many(self, objects: Sequence[CacheData], ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if not objects:
            return False

        model_cache_key = self.get_model_cache_key()
        obj_dict = {
            self.get_cache_id(instance.cache_id): self._serializer.serialize(instance.data)
            for instance in objects
        }

        async with self._engine.session() as session:
            if not self._ttl_enabled:
                return bool(await session.hmset_dict(model_cache_key, obj_dict))

            res = False
            tx = session.multi_exec()
            expiration = ttl or self._engine.default_ttl
            tx.hmset_dict(model_cache_key, obj_dict)
            tx.expire(model_cache_key, int(expiration.total_seconds()))

            for r in await tx.execute():
                res |= r

        return bool(res)

    async def load_one(self, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        async with self._engine.session() as session:
            if ':' in cache_key:
                model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
                if res := await session.hget(model_cache_key, cache_id):
                    return True, self._deserializer.deserialize(res)
                return False, None
            else:
                if res := await session.get(cache_key):
                    return True, self._deserializer.deserialize(res)
                return False, None

    async def load_many(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[Dict[str, Any]]]:
        if not indices:
            return []

        cache_keys = [self.get_cache_id(id_value) for id_value in indices]

        async with self._engine.session() as session:
            res = await session.hmget(self.get_model_cache_key(), *cache_keys)

        objects: Dict[Any, Any] = OrderedDict()

        for id_value, data in zip(indices, res):
            objects[id_value] = self._deserializer.deserialize(data) if data is not None else None

        return list(objects.values())

    async def drop_one(self, cache_key: str) -> bool:
        async with self._engine.session() as session:
            if ':' in cache_key:
                model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
                return bool(await session.hdel(model_cache_key, cache_id))
            else:
                return bool(await session.delete(cache_key))

    async def drop_many(self, indices: Sequence[Any] = None) -> int:
        model_cache_key = self.get_model_cache_key()

        async with self._engine.session() as session:
            if indices and len(indices) > 0:
                cache_keys = [self.get_cache_id(id_value) for id_value in indices]
            else:
                cache_keys = await session.hkeys(model_cache_key)

            return int(await session.hdel(model_cache_key, *cache_keys)) if cache_keys else 0

    async def drop_all(self, prefix: Optional[str] = None) -> int:
        model_cache_key = self.get_model_cache_key()
        async with self._engine.session() as session:
            if not prefix:
                keys_to_delete = await session.hkeys(model_cache_key)
            else:
                keys_to_delete = list()
                for cache_key in await session.hkeys(model_cache_key, encoding='ascii'):
                    if cache_key.startswith(prefix):
                        keys_to_delete.append(cache_key)

            return int(await session.hdel(model_cache_key, *keys_to_delete)) if keys_to_delete else 0

    async def exists(self, cache_key: str) -> bool:
        async with self._engine.session() as session:
            if ':' in cache_key:
                model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
                if await session.hexists(model_cache_key, cache_id):
                    return await session.hget(model_cache_key, cache_id) != self._null_data
            else:
                if await session.exists(cache_key):
                    return await session.get(cache_key) != self._null_data
        return False

    async def scan(self, cache_key: Optional[str] = None, match: Optional[str] = None, count: Optional[int] = None) \
            -> AsyncGenerator[Tuple[str, Optional[Any]], None]:
        async with self._engine.session() as session:
            async for k, data in session.ihscan(cache_key, match=match, count=count):
                yield k.decode('utf-8'), self._deserializer.deserialize(data)
