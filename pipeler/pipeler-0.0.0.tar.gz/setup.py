# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pipeler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pipeler',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'João Pedro Areias de Moraes',
    'author_email': 'joaoareiasmoraes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
