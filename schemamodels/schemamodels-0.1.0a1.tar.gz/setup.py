# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schemamodels']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'schemamodels',
    'version': '0.1.0a1',
    'description': 'Dynamically create useful data classes from JSON schemas',
    'long_description': None,
    'author': "'Jurnell Cockhren'",
    'author_email': 'jurnell@civichacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
