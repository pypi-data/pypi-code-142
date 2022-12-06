# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_dydb']

package_data = \
{'': ['*']}

install_requires = \
['minimal-dydb>=0.1.13,<0.2.0', 'pydantic>=1.9.1,<2.0.0']

extras_require = \
{'all': ['orjson>=3.7.8,<4.0.0', 'cysimdjson>=21.11,<22.0'],
 'cysimdjson': ['cysimdjson>=21.11,<22.0'],
 'orjson': ['orjson>=3.7.8,<4.0.0']}

setup_kwargs = {
    'name': 'pydantic-dydb',
    'version': '0.1.21',
    'description': '',
    'long_description': None,
    'author': 'bobby',
    'author_email': 'bobby.heyer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
