import asyncio
from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional, Sequence, Set, TYPE_CHECKING, Tuple, TypeVar, Union

from pydantic.main import BaseModel as PydanticModel

from .base import AbstractModel
from .fields import ModelFieldsMixin
from ...util import is_awaitable

if TYPE_CHECKING:
    from ..repositories import ModelRepository, SqlModelRepository

CreateSchemaType = TypeVar('CreateSchemaType', bound=PydanticModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=PydanticModel)


class Model(AbstractModel, ModelFieldsMixin, ABC):
    class Meta(ModelFieldsMixin.Meta):
        repo: 'ModelRepository'

    @classmethod
    def bind(cls, repository: 'ModelRepository'):
        cls.Meta.repo = repository

    @classmethod
    async def construct(cls, data: Mapping[str, Any], **kwargs) -> 'Model':
        result = cls.Meta.repo(**data, **kwargs)
        if is_awaitable(result):
            return await result
        return result

    @classmethod
    async def construct_all(cls, objects: Sequence[Optional[Mapping[str, Any]]], **kwargs) \
            -> Sequence[Optional['Model']]:
        loop = asyncio.get_event_loop()
        awaitables = list()

        for data in objects:
            if data is None:
                future = loop.create_future()
                future.set_result(None)
                awaitables.append(future)
            else:
                awaitables.append(cls.construct(data, **kwargs))

        return await asyncio.gather(*awaitables)

    @classmethod
    def prepare_for_create(cls, data: Mapping[str, Any]) -> Mapping[str, Any]:
        return data

    @classmethod
    def prepare_for_update(cls, data: Mapping[str, Any]) -> Mapping[str, Any]:
        return data

    @classmethod
    def prepare_for_delete(cls, obj: 'Model') -> 'Model':
        return obj

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['Model']:
        return await cls.Meta.repo.get(id_value, **kwargs)

    @classmethod
    async def get_any(cls, indices: Sequence[Any], **kwargs) -> Sequence[Optional['Model']]:
        return await cls.Meta.repo.get_any(indices, **kwargs)

    @classmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        return await cls.Meta.repo.exists(id_value, **kwargs)

    async def load(self, only: Sequence[str] = None) -> bool:
        return await self.Meta.repo.load(self, only)

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Mapping[str, Any]], **kwargs) -> Optional['Model']:
        if isinstance(data, Mapping):
            create_data = data
        else:
            create_data = data.dict(exclude_unset=True)

        if create_data:
            create_data = cls.prepare_for_create(create_data)

        return await cls.Meta.repo.create(create_data, **kwargs)

    @classmethod
    async def get_or_create(
        cls, id_value: Any, data: Union[CreateSchemaType, Mapping[str, Any]], **kwargs) \
            -> Tuple[Optional['Model'], bool]:
        if instance := await cls.get(id_value, **kwargs):
            return instance, False
        else:
            return await cls.create(data, **kwargs), True

    async def update(self, data: Union[UpdateSchemaType, Mapping[str, Any]], **kwargs) -> bool:
        if isinstance(data, Mapping):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = self.prepare_for_update(update_data)

        return await self.Meta.repo.update_by_id(self.get_id_value(), update_data, **kwargs)

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Mapping[str, Any]], **kwargs) -> bool:
        if isinstance(data, Mapping):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        return await cls.Meta.repo.update_by_id(id_value, update_data, **kwargs)

    async def save(self, **kwargs) -> bool:
        return await self.Meta.repo.save(self, **kwargs)

    @classmethod
    async def save_all(cls, objects: Sequence['Model'], **kwargs) -> bool:
        return await cls.Meta.repo.save_all(objects, **kwargs)

    async def delete(self) -> bool:
        return await self.Meta.repo.delete(self)

    @classmethod
    async def delete_all(cls, indices: Sequence[Any] = None) -> bool:
        return await cls.Meta.repo.delete_all(indices)

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        return await cls.Meta.repo.delete_by_id(id_value)


class SqlModel(Model):
    class Meta(Model.Meta):
        repo: 'SqlModelRepository'

    @classmethod
    def bind(cls, repository: 'SqlModelRepository'):
        cls.Meta.repo = repository

    @classmethod
    @abstractmethod
    def query_for_select(cls, include_rela: Optional[Set[str]] = None,
                         exclude_rela: Optional[Set[str]] = None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_for_update(cls, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_for_delete(cls, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def get_columns(cls) -> Mapping[str, Any]:
        ...

    @classmethod
    @abstractmethod
    def get_relationships(cls) -> Mapping[str, Any]:
        ...

    @classmethod
    @abstractmethod
    def query_options(cls, include: Optional[Set[str]] = None, exclude: Optional[Set[str]] = None):
        ...

    #
    # Retrieve operations
    #

    @classmethod
    async def list(
        cls, filters: Optional[Sequence[Any]] = None, sorting: Optional[Sequence[Any]] = None,
            skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs) -> Sequence['SqlModel']:
        return await cls.Meta.repo.list(filters, sorting, skip, limit, params, **kwargs)

    @classmethod
    async def count(cls, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs) -> int:
        return await cls.Meta.repo.count(filters, params, **kwargs)

    @classmethod
    async def exists_by(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs) -> bool:
        return await cls.Meta.repo.exists_by(filters, params, **kwargs)

    #
    # Modification operations
    #

    @classmethod
    async def update_by(cls, filters: Sequence[Any],
                        data: Union[UpdateSchemaType, Mapping[str, Any]],
                        /, params: Mapping[str, Any] = None, **kwargs) -> int:
        if isinstance(data, Mapping):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        if update_data:
            update_data = cls.prepare_for_update(update_data)

        return await cls.Meta.repo.update_by(filters, update_data, params=params, **kwargs)

    @classmethod
    async def delete_by(cls, filters: Sequence[Any], /, params: Mapping[str, Any] = None, **kwargs) -> int:
        return await cls.Meta.repo.delete_by(filters, params=params, **kwargs)

    #
    # Query operations
    #

    @classmethod
    @abstractmethod
    def query_get(cls, id_value: Any, query=None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_any(cls, indices: Sequence[Any], query=None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_list(cls, filters: Sequence[Any], sorting: Sequence[Any],
                   skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_count(cls, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_exists(cls, id_value: Any, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_exists_by(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_update(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        ...

    @classmethod
    @abstractmethod
    def query_delete(cls, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs):
        ...
