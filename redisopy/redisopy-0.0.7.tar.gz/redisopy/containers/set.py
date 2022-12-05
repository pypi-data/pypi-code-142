from collections.abc import MutableSet

from redisopy.containers.base import RedisBaseContainer


class RedisSet(RedisBaseContainer, MutableSet):
    data = set()
    """
    用于操作 redis set，重写其所有可变序列方法。
    """

    def init_redis_value(self):
        if self.is_init:
            self.data = self.smembers()
        else:
            self.data = set()

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def add(self, item):
        self.conn.conn.sadd(self.key, item)
        self.data.add(item)

    def discard(self, item):
        self.conn.conn.srem(self.key, item)
        self.data.discard(item)

    def clear(self):
        self.conn.conn.delete(self.key)
        self.data.clear()

    def smembers(self):
        return self.conn.conn.smembers(self.key)

    def __str__(self):
        return f"{self.__class__.__name__}:{self.key}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __or__(self, other):
        return self.data | other.data

    def __and__(self, other):
        return self.data & other.data

    def __sub__(self, other):
        return self.data - other.data

    def __xor__(self, other):
        return self.data ^ other.data

    def __ior__(self, other):
        self.conn.conn.sunionstore(self.key, self.key, other.key)
        self.data |= other.data
        return self

    def __iand__(self, other):
        self.conn.conn.sinterstore(self.key, self.key, other.key)
        self.data &= other.data
        return self

    def __isub__(self, other):
        self.conn.conn.sdiffstore(self.key, self.key, other.key)
        self.data -= other.data
        return self

    def __ixor__(self, other):
        self.conn.conn.sunionstore(self.key, self.key, other.key)
        self.conn.conn.sinterstore(self.key, self.key, other.key)
        self.data ^= other.data
        return self

    def __le__(self, other):
        return self.data <= other.data

    def __lt__(self, other):
        return self.data < other.data

    def __ge__(self, other):
        return self.data >= other.data
