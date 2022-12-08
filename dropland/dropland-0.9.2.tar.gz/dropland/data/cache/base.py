from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, AsyncGenerator, Dict, Optional, Sequence, Tuple


@dataclass
class CacheData:
    cache_id: str
    data: Optional[Any] = None


class CacheGateway(ABC):
    def get_cache_id(self, id_value: Any) -> str:
        return str(id_value)

    @abstractmethod
    def get_cache_key(self, id_value: Any) -> str:
        ...

    @abstractmethod
    async def cache_one(self, data: CacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        ...

    @abstractmethod
    async def cache_many(self, objects: Sequence[CacheData], ttl: Optional[timedelta] = None, **kwargs) -> bool:
        ...

    @abstractmethod
    async def load_one(self, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        ...

    @abstractmethod
    async def load_many(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[Dict[str, Any]]]:
        ...

    @abstractmethod
    async def drop_one(self, cache_key: str) -> bool:
        ...

    @abstractmethod
    async def drop_many(self, indices: Sequence[Any] = None) -> int:
        ...

    @abstractmethod
    async def drop_all(self, prefix: Optional[str] = None) -> int:
        ...

    @abstractmethod
    async def exists(self, cache_key: str) -> bool:
        ...


class ModelCache(CacheGateway):
    @abstractmethod
    def get_model_cache_key(self) -> str:
        ...

    def get_cache_id(self, id_value: Any) -> str:
        return str(id_value)

    def get_cache_key(self, id_value: Any) -> str:
        return f'{self.get_model_cache_key()}:{self.get_cache_id(id_value)}'


class ScanCacheMixin(CacheGateway):
    @abstractmethod
    async def scan(
        self, cache_key: Optional[str] = None, match: Optional[str] = None, count: Optional[int] = None) \
            -> AsyncGenerator[Tuple[str, Optional[Any]], None]:
        ...
