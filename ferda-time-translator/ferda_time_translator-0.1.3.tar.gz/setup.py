# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ferda_time_translator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ferda-time-translator',
    'version': '0.1.3',
    'description': 'Simple program that will translate the current time into ferda standard time (FST)',
    'long_description': None,
    'author': 'Will Lavalliere',
    'author_email': 'willlavalliere@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
