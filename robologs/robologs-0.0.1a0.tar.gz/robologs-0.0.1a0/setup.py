# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['robologs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'robologs',
    'version': '0.0.1a0',
    'description': 'robologs is an open source library of containerized data transformations for the robotics and drone communities',
    'long_description': '',
    'author': 'roboto.ai',
    'author_email': 'info@roboto.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.2,<4.0.0',
}


setup(**setup_kwargs)
