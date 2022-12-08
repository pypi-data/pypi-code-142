from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional, Sequence, Tuple


class AbstractModel(ABC):
    @abstractmethod
    def get_id_value(self) -> Any:
        ...

    #
    # Retrieve operations
    #

    @classmethod
    @abstractmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['AbstractModel']:
        ...

    @classmethod
    @abstractmethod
    async def get_any(cls, indices: Sequence[Any], **kwargs) -> Sequence[Optional['AbstractModel']]:
        ...

    @classmethod
    @abstractmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        ...

    @abstractmethod
    async def load(self, only: Sequence[str] = None) -> bool:
        ...

    #
    # Modification operations
    #

    @classmethod
    @abstractmethod
    async def create(cls, data: Mapping[str, Any], **kwargs) -> Optional['AbstractModel']:
        ...

    @classmethod
    @abstractmethod
    async def get_or_create(cls, id_value: Any, data: Mapping[str, Any], **kwargs) \
            -> Tuple[Optional['AbstractModel'], bool]:
        ...

    @abstractmethod
    async def update(self, data: Mapping[str, Any], **kwargs) -> bool:
        ...

    @classmethod
    @abstractmethod
    async def update_by_id(cls, id_value: Any, data: Mapping[str, Any], **kwargs) -> bool:
        ...

    @abstractmethod
    async def save(self, **kwargs) -> bool:
        ...

    @classmethod
    @abstractmethod
    async def save_all(cls, objects: Sequence['AbstractModel'], **kwargs) -> bool:
        ...

    @abstractmethod
    async def delete(self) -> bool:
        ...

    @classmethod
    @abstractmethod
    async def delete_all(cls, indices: Sequence[Any] = None) -> bool:
        ...

    @classmethod
    @abstractmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        ...
