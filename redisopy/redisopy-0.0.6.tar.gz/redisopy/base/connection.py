"""Use to connect redis."""
from redis.client import StrictRedis

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 6379
DEFAULT_DB = 0

DEFAULT_CONNECTION: list[StrictRedis] = []


def connect(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, db: int = DEFAULT_DB):
    """
    Use to connect redis.
    Exist a default link, can be overide.
    """
    if not DEFAULT_CONNECTION:
        redis = StrictRedis(host=host, port=port, db=db, decode_responses=True)
        DEFAULT_CONNECTION.append(redis)
    return DEFAULT_CONNECTION[0]
