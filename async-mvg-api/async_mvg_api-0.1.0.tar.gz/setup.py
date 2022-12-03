# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mvg_api', 'mvg_api.api', 'mvg_api.models', 'mvg_api.tests']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'httpx>=0.23.1,<0.24.0',
 'levenshtein>=0.20.8,<0.21.0',
 'pydantic>=1.10.2,<2.0.0',
 'pylint>=2.15.7,<3.0.0',
 'pytest>=7.2.0,<8.0.0']

setup_kwargs = {
    'name': 'async-mvg-api',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Lukas Mahr',
    'author_email': 'lukas@yousuckatprogramming.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
