# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aoclib']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'python-aoclib',
    'version': '0.1.0',
    'description': 'A library for solving AdventOfCode problems using Python.',
    'long_description': '# aoclib\nA library for solving AdventOfCode problems using Python.\n',
    'author': 'Unknown15082',
    'author_email': 'trangiahuy15082006@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
