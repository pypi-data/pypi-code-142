# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ergodiff']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ergodiff',
    'version': '0.2.0',
    'description': 'An ergonomic text-difference pattern generator.',
    'long_description': '',
    'author': 'Lingxi Li',
    'author_email': 'lilingxi01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
