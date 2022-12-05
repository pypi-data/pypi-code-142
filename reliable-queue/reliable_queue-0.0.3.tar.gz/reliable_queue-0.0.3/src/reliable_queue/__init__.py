from typing import Optional
import redis


# This is the skeleton functionality.
class ReliableQueue:

    # For first version, just assume local redis
    def __init__(self, queue_name: str, redis_hostname: str = "localhost", redis_port: int = 6379):
        self._queue_name = queue_name
        self._redis = redis.Redis(host=redis_hostname, port=redis_port)

    def push(self, data: bytes):
        """
        Note: redis.exceptions.ResponseError: WRONGTYPE Operation against a key holding the wrong kind of value
           happens if key exists but is not a list.

        :param data:
        :return:
        """
        self._redis.rpush(self._queue_name, data)

    def blocking_pop(self, timeout=0) -> Optional[bytes]:
        """
        :param timeout: If 0, wait until data is available, if timeout>0, wait max timeout seconds else return None.
        :return: Optional[bytes]
        """
        result = self._redis.blpop(self._queue_name, timeout)
        if result is None:
            return None
        return result[1]

    def is_ram_empty(self):
        return not self._redis.exists(self._queue_name)
