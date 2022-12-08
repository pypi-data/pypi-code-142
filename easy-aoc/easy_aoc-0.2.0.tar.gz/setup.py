# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['easy_aoc', 'easy_aoc.db', 'easy_aoc.repository']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'attrs>=22.1.0,<23.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'sqlalchemy>=2.0.0b4,<3.0.0',
 'yarl>=1.8.2,<2.0.0']

setup_kwargs = {
    'name': 'easy-aoc',
    'version': '0.2.0',
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
