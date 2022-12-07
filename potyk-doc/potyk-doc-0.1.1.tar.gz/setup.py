# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['potyk_doc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'potyk-doc',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'potykion',
    'author_email': 'potykion@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
