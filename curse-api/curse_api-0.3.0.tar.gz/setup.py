# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['curse_api']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'curse-api',
    'version': '0.3.0',
    'description': 'A simple curseforge api wrapper',
    'long_description': 'None',
    'author': 'Stinky-c',
    'author_email': '60587749+Stinky-c@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
