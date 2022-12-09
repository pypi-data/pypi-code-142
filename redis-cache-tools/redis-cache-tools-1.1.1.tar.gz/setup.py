# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redis_cache']

package_data = \
{'': ['*']}

install_requires = \
['redis>=4.0.0']

setup_kwargs = {
    'name': 'redis-cache-tools',
    'version': '1.1.1',
    'description': 'redis-cache-tools is a pythonic interface for creating a cache over redis.',
    'long_description': '# redis-cache-tools\nIt provides simple decorators that can be added to any function to cache its return values.\n\nRequirements:\n-------------\nredis 4.0.0\n\nInstallation:\n-------------\n\n    pip install redis-cache-tools\n\nUsage:\n------\n\n    from redis_cache import cache_it_json\n\n    @cache_it_json(limit=1000, expire=60 * 60 * 24)\n    def fib(n):\n        if n == 0:\n            return 0\n        elif n == 1:\n            return 1\n        else:\n            return fib(n-1) + fib(n-2)\n\n`limit` is the maximum number of keys, `expire` is the expire time in seconds.  \nIt is always recommended to specify a expire time, since by default redis-server will only remove keys with an expire time set in a event of full memory. But if you wish your keys to never expire, set `expire` to `None`.  \n**Note that function arguments and result must be pickleable, since cache_it uses the pickle module.**\n\nIt is also possible to use redis-cache-tools as a object-oriented cache:\n        \n    >> from redis_cache import SimpleCache\n    >> c = SimpleCache(10)  # cache that has a maximum limit of 10 keys\n    >> c.store("foo", "bar")\n    >> c.get("foo")\n    \'bar\'\n    >> "foo" in c  # efficient membership test, time-complexity O(1)\n    True\n    >> len(c)  # efficient cardinality calculation, time-complexity O(1)\n    1\n    >> c.keys()  # returns all keys, time-complexity O(N) with N being the cache c cardinality\n    set([\'foo\'])\n    >> c.flush()  # flushes the cache, time-complexity O(N) with N being the cache c cardinality\n    >> "foo" in c\n    False\n    >> len(c)\n    0\n\nCheck out more examples in the test_rediscache.py file.\n\nAdvanced:\n---------\nAdvanced users can customize the decorators even more by passing a SimpleCache object. For example:\n\n    using env variables.\n\n    export REDIS_HOST=localhost\n    export REDIS_PORT=6379\n    export REDIS_PORT=3\n    \n    my_cache = SimpleCache(limit=100, expire=60 * 60, hashkeys=True, host=\'localhost\', port=6379, db=1, namespace=\'Fibonacci\')\n    @cache_it(cache=my_cache)\n    def fib(n):\n        # ...\n\n`hashkeys` parameter makes the SimpleCache to store keys in md5 hash. It is `True` by default in decorators, but `False` by default in a new SimpleCache object.  \n`host`, `port` and `db` are the same redis config params used in StrictRedis class of redis-py.\nBy default, the `namespace` is the name of the module from which the decorated function is called, but it can be overridden with the `namespace` parameter. ',
    'author': 'It provides simple decorators that can be added to any function to cache its return values.',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://500apps.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
