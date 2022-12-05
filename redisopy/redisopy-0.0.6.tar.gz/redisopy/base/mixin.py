from redis.client import StrictRedis

from redisopy.base.connection import DEFAULT_CONNECTION


class ConnMixin:
    """辅助数据库连接"""

    @property
    def conn(self) -> StrictRedis:
        """Get alive redis connection by connect"""
        return DEFAULT_CONNECTION[0]
