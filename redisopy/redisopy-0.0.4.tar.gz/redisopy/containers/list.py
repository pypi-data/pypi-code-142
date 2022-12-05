from collections import UserList

from redisopy.containers.base import RedisBaseContainer


class RedisList(RedisBaseContainer, UserList):
    """
    用于操作 redis list，重写其所有可变序列方法。
    不支持切片赋值
        - s[i:j] = t
        - del s[i:j]
        - s[i:j:k] = t
        - del s[i:j:k]
    """

    def init_redis_value(self):
        if self.is_init:
            self.data = self.lrange()
        else:
            self.data = []

    def __setitem__(self, key, value):
        self.conn.conn.lset(self.key, key, value)
        self.data[key] = value

    def append(self, value: str):
        self.conn.conn.rpush(self.key, value)
        self.data.append(value)

    def extend(self, *elements) -> None:
        self.conn.conn.rpush(self.key, *elements)
        self.data.extend(elements)

    def insert(self, index: int, value: str):
        self.conn.conn.linsert(self.key, 'BEFORE', self.data[index], value)
        self.data.insert(index, value)

    def pop(self, i: int = -1):
        """only can pop last element"""
        value = self.conn.conn.rpop(self.key)
        self.data.pop(-1)
        return value

    def remove(self, item) -> None:
        self.conn.conn.lrem(self.key, 1, item)
        self.data.remove(item)

    def clear(self):
        self.conn.conn.delete(self.key)
        self.data.clear()

    def lrange(self):
        return self.conn.conn.lrange(self.key, 0, -1)

    def __str__(self):
        return f"{self.__class__.__name__}:{self.key}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)
