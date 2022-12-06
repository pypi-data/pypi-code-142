# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minimal_dydb']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'minimal-dydb',
    'version': '0.1.16',
    'description': '',
    'long_description': None,
    'author': 'Robert Heyer',
    'author_email': 'bobby.heyer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
