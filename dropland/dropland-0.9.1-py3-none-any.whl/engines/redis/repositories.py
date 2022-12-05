from datetime import timedelta
from typing import Any, AsyncGenerator, Callable, Mapping, Optional, Sequence, Tuple, Type, TypeVar

from dropland.data.cache.base import CacheData
from dropland.data.repositories import ModelRepository
from .cache import HashRedisCache, SimpleRedisCache
from .engine import RedisEngine
from .model import RedisCacheType, RedisModel

RedisModelType = TypeVar('RedisModelType', bound=RedisModel, covariant=True)
RedisModelTypeFactory = Callable[..., RedisModelType]


class RedisModelRepository(ModelRepository[RedisModelType]):
    def __init__(self, model_class: Type[RedisModelType], engine: RedisEngine,
                 model_factory: Optional[RedisModelTypeFactory] = None):
        super(RedisModelRepository, self).__init__(model_class, model_factory)

        cache_type = model_class.Meta.cache_type
        protocol_class = SimpleRedisCache \
            if cache_type == RedisCacheType.SIMPLE \
            else HashRedisCache

        cache_protocol = protocol_class(
            engine, model_class.__name__,
            model_class.Meta.serializer,  model_class.Meta.deserializer,
            ttl_enabled=model_class.Meta.ttl_enabled
        )

        self._engine = engine
        self._cache_protocol = cache_protocol

    def get_engine(self) -> RedisEngine:
        return self._engine

    def get_model_cache_key(self) -> str:
        return self._cache_protocol.get_model_cache_key()

    def get_cache_id(self, id_value: Any) -> str:
        return self._cache_protocol.get_cache_id(id_value)

    def get_cache_key(self, id_value: Any) -> str:
        return self._cache_protocol.get_cache_key(id_value)

    #
    # Retrieve operations
    #

    async def get(self, id_value: Any, **kwargs) -> Optional[RedisModelType]:
        exists, data = await self._cache_protocol.load_one(
            self.get_cache_key(id_value), **kwargs
        )
        if exists:
            return await self.model_class.construct(data, **kwargs)
        return None

    async def get_any(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[RedisModelType]]:
        data = await self._cache_protocol.load_many(indices, **kwargs)
        objects = await self.model_class.construct_all(data, **kwargs)
        objects = {obj.get_id_value(): obj for obj in objects if obj is not None}
        return [objects[id_value] if id_value in objects else None for id_value in indices]

    async def exists(self, id_value: Any, **kwargs) -> bool:
        return await self._cache_protocol.exists(self.get_cache_key(id_value))

    async def load(self, instance: RedisModelType, only: Sequence[str] = None) -> bool:
        only = set(only) if only else None
        exists, data = await self._cache_protocol.load_one(self.get_cache_key(instance.get_id_value()))
        if exists:
            for k, v in data.items():
                if only is None or k in only:
                    setattr(instance, k, v)
        return exists

    async def scan(self, match: str, count: Optional[int] = None, **kwargs) \
            -> AsyncGenerator[Tuple[str, Optional[RedisModelType]], None]:
        async for k, data in self._cache_protocol.scan(self.get_model_cache_key(), match, count):
            if data is None:
                yield k, None
            else:
                yield k, await self.model_class.construct(data, **kwargs)

    #
    # Modification operations
    #

    async def create(self, data: Mapping[str, Any], **kwargs) -> Optional[RedisModelType]:
        instance = self(**data)
        await self.save(instance, **kwargs)
        return instance

    async def update_by_id(self, id_value: Any, data: Mapping[str, Any], ttl: Optional[timedelta] = None) -> bool:
        data = CacheData(cache_id=self.get_cache_id(id_value), data=data)
        return await self._cache_protocol.cache_one(data, ttl=ttl)

    async def save(self, instance: RedisModelType, ttl: Optional[timedelta] = None) -> bool:
        data = CacheData(
            cache_id=self.get_cache_id(instance.get_id_value()),
            data=instance.get_serializable_values()
        )
        return await self._cache_protocol.cache_one(data, ttl=ttl)

    async def save_all(self, objects: Sequence[RedisModelType], ttl: Optional[timedelta] = None) -> bool:
        objects_data = [
            CacheData(
                cache_id=self.get_cache_id(o.get_id_value()),
                data=o.get_serializable_values()
            ) for o in objects
        ]
        return await self._cache_protocol.cache_many(objects_data, ttl=ttl)

    async def delete(self, instance: RedisModelType) -> bool:
        return await self._cache_protocol.drop_one(self.get_cache_key(instance.get_id_value()))

    async def delete_all(self, indices: Sequence[Any] = None) -> int:
        return await self._cache_protocol.drop_many(indices)

    async def delete_by_id(self, id_value: Any) -> bool:
        return await self._cache_protocol.drop_one(self.get_cache_key(id_value))


class RedisProxyRepository(RedisModelRepository):
    def __init__(self, model_class: Type[RedisModelType], engine: RedisEngine,
                 repository: ModelRepository,
                 model_factory: Optional[RedisModelTypeFactory] = None):
        super(RedisProxyRepository, self).__init__(model_class, engine, model_factory)
        self._repository = repository

    #
    # Retrieve operations
    #

    async def get(self, id_value: Any, **kwargs) -> Optional[RedisModelType]:
        if not kwargs.pop('no_cache', False):
            if instance := await super().get(id_value, **kwargs):
                return instance
        if instance := await self._repository.get(id_value, **kwargs):
            instance = await self.model_class.construct(instance.get_values(), **kwargs)
            await super().save(instance, **kwargs)
        return instance

    async def get_any(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[RedisModelType]]:
        if not kwargs.pop('no_cache', False):
            return await super().get_any(indices, **kwargs)
        if objects := await self._repository.get_any(indices, **kwargs):
            values = [o.get_values() for o in objects if o is not None]
            objects_to_save = await self.model_class.construct_all(values, **kwargs)
            await super().save_all(objects_to_save, **kwargs)
        return objects

    async def exists(self, id_value: Any, **kwargs) -> bool:
        if not kwargs.pop('no_cache', False):
            return await super().exists(id_value, **kwargs)
        return await self._repository.exists(id_value, **kwargs)

    async def load(self, instance: RedisModelType, only: Sequence[str] = None) -> bool:
        if res := await super().load(instance, only):
            return res
        new_instance = await self._repository.model_class.construct(instance.get_values())
        if res := await self._repository.load(new_instance, only):
            for k, v in new_instance.get_values().items():
                if only is None or k in only:
                    setattr(instance, k, v)
        return res

    #
    # Modification operations
    #

    async def update_by_id(self, id_value: Any, data: Mapping[str, Any], ttl: Optional[timedelta] = None) -> bool:
        if res := await super().update_by_id(id_value, data, ttl=ttl):
            return await self._repository.update_by_id(id_value, data, ttl=ttl)
        return res

    async def save(self, instance: RedisModelType, ttl: Optional[timedelta] = None) -> bool:
        if res := await super().save(instance, ttl=ttl):
            instance = await self._repository.model_class.construct(instance.get_values())
            return await self._repository.save(instance, ttl=ttl)
        return res

    async def save_all(self, objects: Sequence[RedisModelType], ttl: Optional[timedelta] = None) -> bool:
        if res := await super().save_all(objects, ttl=ttl):
            values = [o.get_values() for o in objects]
            objects = await self.model_class.construct_all(values)
            return await self._repository.save_all(objects, ttl=ttl)
        return res

    async def delete(self, instance: RedisModelType) -> bool:
        if res := await super().delete(instance):
            return await self._repository.delete_by_id(instance.get_id_value())
        return res

    async def delete_all(self, indices: Sequence[Any] = None) -> int:
        if res := await super().delete_all(indices):
            return await self._repository.delete_all(indices)
        return res

    async def delete_by_id(self, id_value: Any) -> bool:
        if res := await super().delete_by_id(id_value):
            return await self._repository.delete_by_id(id_value)
        return res
