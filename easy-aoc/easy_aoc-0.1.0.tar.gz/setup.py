# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['easy_aoc']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0']

setup_kwargs = {
    'name': 'easy-aoc',
    'version': '0.1.0',
    'description': 'Tools for the Advent of Code',
    'long_description': 'None',
    'author': 'Sebastiaan Zeeff',
    'author_email': 'sebastiaan.zeeff@gmail.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
