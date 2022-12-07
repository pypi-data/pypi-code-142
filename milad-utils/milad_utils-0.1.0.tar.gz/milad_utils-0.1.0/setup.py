# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['milad_utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'milad-utils',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Milad Alizadeh',
    'author_email': 'milad@cohere.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
