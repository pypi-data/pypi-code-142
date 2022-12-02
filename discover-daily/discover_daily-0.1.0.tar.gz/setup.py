# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['src']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['discover-daily = src.main:recommend_album']}

setup_kwargs = {
    'name': 'discover-daily',
    'version': '0.1.0',
    'description': 'discover-daily is a CLI tool for all the music nerds out there.',
    'long_description': 'None',
    'author': 'Robert Kossendey',
    'author_email': 'robert.kossendey@protonmail.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
