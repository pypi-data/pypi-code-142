# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['funcenter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'funcenter',
    'version': '1.0',
    'description': 'Some random functions I made... includes color formatting, text formatting, basic math, and most of all... dumb algorithms. Enjoy.',
    'long_description': 'None',
    'author': 'uncenter',
    'author_email': 'uncenteristaken@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
