from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, Generic, Mapping, Optional, Sequence, Tuple, Type, TypeVar, Union, \
    cast

from .cache.method import MethodCache
from .entities import Entity
from .models.model import Model, SqlModel
from .models.serializable import SerializableModel

EntityType = TypeVar('EntityType', bound=Entity, covariant=True)
ModelType = TypeVar('ModelType', bound=Model, covariant=True)
SerializableModelType = TypeVar('SerializableModelType', bound=SerializableModel, covariant=True)
SqlModelType = TypeVar('SqlModelType', bound=SqlModel, covariant=True)
ModelTypeFactory = Callable[..., ModelType]
SerializableModelTypeFactory = Callable[..., SerializableModelType]
SqlModelTypeFactory = Callable[..., SqlModelType]


class Repository(Generic[EntityType], ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> Union[EntityType, Awaitable[EntityType]]:
        ...

    @abstractmethod
    async def get(self, id_value: Any, **kwargs) -> Optional[EntityType]:
        ...

    @abstractmethod
    async def get_any(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[EntityType]]:
        ...

    @abstractmethod
    async def exists(self, id_value: Any, **kwargs) -> bool:
        ...

    @abstractmethod
    async def load(self, instance: EntityType, only: Sequence[str] = None) -> bool:
        ...

    @abstractmethod
    async def create(self, data: Mapping[str, Any], **kwargs) -> Optional[EntityType]:
        ...

    async def get_or_create(self, id_value: Any, data: Mapping[str, Any], **kwargs) -> Tuple[Optional[EntityType], bool]:
        if instance := await self.get(id_value, **kwargs):
            return instance, False
        else:
            return await self.create(data, **kwargs), True

    @abstractmethod
    async def update_by_id(self, id_value: Any, data: Mapping[str, Any], **kwargs) -> bool:
        ...

    @abstractmethod
    async def save(self, instance: EntityType, **kwargs) -> bool:
        ...

    @abstractmethod
    async def save_all(self, objects: Sequence[EntityType], **kwargs) -> bool:
        ...

    @abstractmethod
    async def delete(self, instance: EntityType) -> bool:
        ...

    @abstractmethod
    async def delete_all(self, indices: Sequence[Any] = None) -> int:
        ...

    @abstractmethod
    async def delete_by_id(self, id_value: Any) -> bool:
        ...


class ModelRepository(Repository[ModelType], ABC):
    def __init__(self, model_class: Type[ModelType], model_factory: Optional[ModelTypeFactory] = None):
        self._model_class = model_class
        self._model_factory = model_factory or model_class
        model_class.bind(self)

    def __call__(self, *args, **kwargs) -> Union[ModelType, Awaitable[ModelType]]:
        return self._model_factory(*args, **kwargs)

    @property
    def model_class(self):
        return self._model_class


class SqlModelRepository(ModelRepository[SqlModelType], ABC):
    def __init__(self, model_class: Type[SqlModelType], model_factory: Optional[SqlModelTypeFactory] = None):
        super(SqlModelRepository, self).__init__(model_class, model_factory)

    @abstractmethod
    async def list(
        self, filters: Optional[Sequence[Any]] = None, sorting: Optional[Sequence[Any]] = None,
            skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs) -> Sequence[SqlModelType]:
        ...

    @abstractmethod
    async def count(self, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs) -> int:
        ...

    @abstractmethod
    async def exists_by(self, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs) -> bool:
        ...

    @abstractmethod
    async def update_by(self, filters: Sequence[Any], data: Mapping[str, Any],
                        /, params: Mapping[str, Any] = None, **kwargs) -> int:
        ...

    @abstractmethod
    async def delete_by(self, filters: Sequence[Any], /, params: Mapping[str, Any] = None, **kwargs) -> int:
        ...


class CachedRepository(Repository[SerializableModelType]):
    def __init__(self, repository: ModelRepository[SerializableModelType], cache: MethodCache):
        super(CachedRepository, self).__init__()
        self._repo = repository
        self._cache = cache

    def __call__(self, *args, **kwargs) -> Union[EntityType, Awaitable[EntityType]]:
        return self._repo(*args, **kwargs)

    #
    # Retrieve operations
    #

    async def get(self, id_value: Any, **kwargs) -> Optional[SerializableModelType]:
        if kwargs.pop('no_cache', False):
            return await self._repo.get(id_value, **kwargs)

        method_cache_key = MethodCache.cache_key_for('get', {'id': id_value, 'kw': kwargs})
        exists, data = await self._cache.get('get', cache_key=method_cache_key)
        if exists:
            return await self._repo.model_class.construct(data, _from_cache=True, **kwargs)

        result = cast(
            Optional[SerializableModelType],
            await self._repo.get(id_value, **kwargs)
        )
        serializable = result.get_serializable_values() if result is not None else None
        await self._cache.put('get', cache_key=method_cache_key, data=serializable)
        return result

    async def get_any(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[SerializableModelType]]:
        if kwargs.pop('no_cache', False):
            return await self._repo.get_any(indices, **kwargs)

        method_cache_key = MethodCache.cache_key_for('get_any', {'indices': indices, 'kw': kwargs})
        exists, data = await self._cache.get('get_any', cache_key=method_cache_key)
        if exists:
            return await self._repo.model_class.construct_all(data, _from_cache=True, **kwargs)

        result = cast(
            Sequence[Optional[SerializableModelType]],
            await self._repo.get_any(indices, **kwargs)
        )
        serializable = [i.get_serializable_values() if i is not None else None for i in result]
        await self._cache.put('get_any', cache_key=method_cache_key, data=serializable)
        return result

    async def exists(self, id_value: Any, **kwargs) -> bool:
        if kwargs.pop('no_cache', False):
            return await self._repo.exists(id_value, **kwargs)

        method_cache_key = MethodCache.cache_key_for('exists', {'id': id_value, 'kw': kwargs})
        exists, data = await self._cache.get('exists', cache_key=method_cache_key)
        if exists:
            return bool(data)

        result = await self._repo.exists(id_value, **kwargs)
        await self._cache.put('exists', cache_key=method_cache_key, data=result)
        return result

    async def load(self, instance: SerializableModelType, only: Sequence[str] = None) -> bool:
        if result := await self._repo.load(instance, only):
            serializable = instance.get_serializable_values()
            await self._cache.put(
                'get', cache_key={'id': instance.get_id_value(), 'kw': dict()},
                data=serializable)
        return result

    #
    # Modification operations
    #

    async def create(self, data: Mapping[str, Any], **kwargs) -> Optional[SerializableModelType]:
        if result := cast(Optional[SerializableModelType], await self._repo.create(data, **kwargs)):
            await self._drop_methods()
        return result

    async def update_by_id(self, id_value: Any, data: Mapping[str, Any], **kwargs) -> bool:
        if result := await self._repo.update_by_id(id_value, data, **kwargs):
            await self._drop_methods(['get', 'get_any', 'list'])
        return result

    async def save(self, instance: SerializableModelType, **kwargs) -> bool:
        if result := await self._repo.save(instance, **kwargs):
            serializable = instance.get_serializable_values()
            await self._cache.put(
                'get', cache_key={'id': instance.get_id_value(), 'kw': dict()},
                data=serializable)
        return result

    async def save_all(self, objects: Sequence[SerializableModelType], **kwargs) -> bool:
        if result := await self._repo.save_all(objects, **kwargs):
            await self._drop_methods()
        return result

    async def delete(self, instance: SerializableModelType) -> bool:
        if result := await self._repo.delete(instance):
            await self._drop_methods()
        return result

    async def delete_all(self, indices: Sequence[Any] = None) -> int:
        if result := await self._repo.delete_all(indices):
            await self._drop_methods()
        return result

    async def delete_by_id(self, id_value: Any) -> bool:
        if result := await self._repo.delete_by_id(id_value):
            await self._drop_methods()
        return result

    #
    # Private
    #

    async def _drop_methods(self, methods: Sequence[str] = None):
        method_names = ('get', 'get_any', 'list', 'count', 'exists', 'exists_by')
        methods = set(methods) if methods else set(method_names)
        await self._cache.drop_all([m for m in method_names if m in methods])

    @classmethod
    def _expr2string(cls, expr, params: dict = None):
        from sqlalchemy.sql import ClauseElement

        if expr is None:
            return None
        elif isinstance(expr, list):
            res = [cls._expr2string(i, params) for i in expr]
            return ','.join(res)
        elif isinstance(expr, ClauseElement):
            if params:
                expr = expr.params(params)
            compiled = expr.compile(compile_kwargs={'render_postcompile': True})
            res = [compiled.string]
            for k, v in compiled.params.items():
                if params and k in params:
                    res.append(str(params[k]))
                else:
                    res.append(str(v))
            return '$'.join(res)

        return str(expr)


class CachedSqlModelRepository(CachedRepository[SqlModelType]):
    def __init__(self, repository: SqlModelRepository, cache: MethodCache):
        super(CachedSqlModelRepository, self).__init__(repository, cache)
        self._repo = repository
        self._cache = cache

    #
    # Retrieve operations
    #

    async def list(
        self, filters: Optional[Sequence[Any]] = None, sorting: Optional[Sequence[Any]] = None,
            skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs) -> Sequence[SqlModelType]:
        if kwargs.pop('no_cache', False):
            return await self._repo.list(filters, sorting, skip, limit, params, **kwargs)

        method_cache_key = MethodCache.cache_key_for('list', {
            'filters': self._expr2string(filters, params),
            'sorting': self._expr2string(sorting),
            'skip': skip, 'limit': limit, 'kw': kwargs
        })
        exists, data = await self._cache.get('list', cache_key=method_cache_key)
        if exists:
            return await self._repo.model_class.construct_all(data, _from_cache=True, **kwargs)

        result = cast(
            Sequence[Optional[SqlModelType]],
            await self._repo.list(filters, sorting, skip, limit, params, **kwargs)
        )
        serializable = [i.get_serializable_values() for i in result]
        await self._cache.put('list', cache_key=method_cache_key, data=serializable)
        return result

    async def count(self, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs) -> int:
        if kwargs.pop('no_cache', False):
            return await self._repo.count(filters, params, **kwargs)

        method_cache_key = MethodCache.cache_key_for('count', {
            'filters': self._expr2string(filters, params), 'kw': kwargs
        })
        exists, data = await self._cache.get('count', cache_key=method_cache_key)
        if exists:
            return int(data)

        result = await self._repo.count(filters, params, **kwargs)
        await self._cache.put('count', cache_key=method_cache_key, data=result)
        return result

    async def exists_by(self, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs) -> bool:
        if kwargs.pop('no_cache', False):
            return await self._repo.exists_by(filters, params, **kwargs)

        method_cache_key = MethodCache.cache_key_for('exists_by', {
            'filters': self._expr2string(filters, params), 'kw': kwargs
        })
        exists, data = await self._cache.get('exists_by', cache_key=method_cache_key)
        if exists:
            return bool(data)

        result = await self._repo.exists_by(filters, params, **kwargs)
        await self._cache.put('exists_by', cache_key=method_cache_key, data=result)
        return result

    #
    # Modification operations
    #

    async def update_by(self, filters: Sequence[Any], data: Mapping[str, Any],
                        /, params: Mapping[str, Any] = None, **kwargs) -> int:
        if result := await self._repo.update_by(filters, data, params=params, **kwargs):
            await self._drop_methods(['get', 'get_any', 'list'])
        return result

    async def delete_by(self, filters: Sequence[Any], /, params: Mapping[str, Any] = None, **kwargs) -> int:
        if result := await self._repo.delete_by(filters, params=params, **kwargs):
            await self._drop_methods()
        return result
