# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assmblr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'assmblr',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Alyce',
    'author_email': 'Alyceosbourne@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
