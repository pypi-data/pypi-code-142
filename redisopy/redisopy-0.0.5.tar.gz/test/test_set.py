from redisopy.base.connection import connect
from redisopy.containers.set import RedisSet

connect(db=3)


def test_set():
    s = RedisSet('abcd')
    s.add('a')
    s.add('b')
    s.add('a')
    print('a' in s, 'b' in s, 'c' in s)
