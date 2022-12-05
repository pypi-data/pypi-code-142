import enum
from typing import Any, TYPE_CHECKING

from dropland.data.models.serializable import SerializableModel

if TYPE_CHECKING:
    from .repositories import RedisModelRepository


class RedisCacheType(int, enum.Enum):
    SIMPLE = 0
    HASH = 1


class RedisModel(SerializableModel):
    class Meta(SerializableModel.Meta):
        cache_type: RedisCacheType = RedisCacheType.SIMPLE
        ttl_enabled: bool = True
        repo: 'RedisModelRepository'

    @classmethod
    def bind(cls, repository: 'RedisModelRepository'):
        cls.Meta.repo = repository

    def get_id_value(self) -> Any:
        raise NotImplementedError
