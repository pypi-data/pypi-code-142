try:
    import aioredis

    from .cache import SimpleRedisCache, HashRedisCache
    from .engine import EngineConfig, RedisEngineBackend, RedisEngine
    from .model import RedisCacheType, RedisModel
    from .repositories import RedisModelRepository, RedisProxyRepository
    from .settings import RedisSettings

    USE_REDIS = True

except ImportError:
    USE_REDIS = False
