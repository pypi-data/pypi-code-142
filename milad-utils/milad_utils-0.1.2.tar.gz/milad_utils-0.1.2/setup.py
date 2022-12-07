# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['milad']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'milad-utils',
    'version': '0.1.2',
    'description': '',
    'long_description': '',
    'author': 'Milad Alizadeh',
    'author_email': 'milad@cohere.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
