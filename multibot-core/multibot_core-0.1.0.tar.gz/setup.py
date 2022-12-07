# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multibot_core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'multibot-core',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'qvirus2',
    'author_email': 'qvirus2@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
