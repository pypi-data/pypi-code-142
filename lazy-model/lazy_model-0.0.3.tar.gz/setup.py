# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lazy_model']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0']

setup_kwargs = {
    'name': 'lazy-model',
    'version': '0.0.3',
    'description': '',
    'long_description': 'Lazy parsing for Pydantic models',
    'author': 'Roman',
    'author_email': 'roman-right@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
