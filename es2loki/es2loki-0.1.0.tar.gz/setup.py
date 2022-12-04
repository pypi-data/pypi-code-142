# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['es2loki', 'es2loki.aio', 'es2loki.commands', 'es2loki.pos', 'es2loki.proto']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4',
 'elasticsearch>=8.5.2,<9',
 'frozendict',
 'protobuf',
 'python-snappy',
 'tortoise-orm[asyncpg]',
 'yarl']

setup_kwargs = {
    'name': 'es2loki',
    'version': '0.1.0',
    'description': '',
    'long_description': '# es2loki\n',
    'author': 'igorcoding',
    'author_email': 'igorcoding@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ktsstudio/es2loki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
