from abc import abstractmethod

from redis.exceptions import ResponseError

from redisopy.base.mixin import ConnMixin


class RedisBaseContainer:
    """"""
    conn = ConnMixin()

    def __init__(self, key: str, is_init: bool = False):
        """
        :param key:
        :param is_init: if not, not load data: Only update, not read
        """
        self.key = key
        self.is_init = is_init
        try:
            self.init_redis_value()
        except ResponseError as e:
            if "WRONGTYPE" in e.args[0]:
                raise TypeError(f"Key {self.key} is not a {self.__class__.__name__}")
            raise e

    @abstractmethod
    def init_redis_value(self):
        return NotImplemented
