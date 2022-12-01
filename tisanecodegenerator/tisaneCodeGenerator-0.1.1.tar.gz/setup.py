# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tisanecodegenerator']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'tisanecodegenerator',
    'version': '0.1.1',
    'description': 'Code generator for Tisane',
    'long_description': None,
    'author': 'Eunice Jun',
    'author_email': 'eunice.m.jun@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
