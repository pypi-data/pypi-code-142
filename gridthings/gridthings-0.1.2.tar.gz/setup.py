# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gridthings']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.8.2,<5.0.0', 'pydantic>=1.8.2,<2.0.0']

extras_require = \
{'examples': ['jupyter>=1.0.0,<2.0.0', 'pandas>=1.3.4,<2.0.0']}

setup_kwargs = {
    'name': 'gridthings',
    'version': '0.1.2',
    'description': 'Python library for working with Grid-like structures (e.g. tic-tac-toe)',
    'long_description': 'None',
    'author': 'Matt Kafonek',
    'author_email': 'matt.kafonek@noteable.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kafonek/gridthings',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
