from redisopy.base.connection import connect
from redisopy.containers.list import RedisList

connect(db=3)


def test_list():
    redis_list = RedisList('abc')
    # redis_list.clear()
    for i in 'abcde':
        redis_list.append(i)
    redis_list[0] = 'e'
    print(redis_list.data)

    redis_list.extend('f', 'g', 'h')
    redis_list.insert(0, 'a')
    var = redis_list.pop()
    print(var)
