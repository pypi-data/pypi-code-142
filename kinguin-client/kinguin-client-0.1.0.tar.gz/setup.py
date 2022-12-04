# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kinguin_client', 'kinguin_client.clients']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kinguin-client',
    'version': '0.1.0',
    'description': 'Python API wrapper for Kinguin',
    'long_description': None,
    'author': 'rr00bbiinn',
    'author_email': 'robin@itlandslaget.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
