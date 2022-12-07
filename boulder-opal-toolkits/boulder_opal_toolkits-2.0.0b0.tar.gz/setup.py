# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boulderopaltoolkits',
 'boulderopaltoolkits.closed_loop',
 'boulderopaltoolkits.deprecated',
 'boulderopaltoolkits.ions',
 'boulderopaltoolkits.signals',
 'boulderopaltoolkits.superconducting',
 'boulderopaltoolkits.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21.5,<2.0.0',
 'numpydoc>=1.1.0,<2.0.0',
 'python-forge>=18.6.0,<19.0.0',
 'qctrl-commons>=17.6.0,<18.0.0',
 'scipy>=1.7.3,<2.0.0',
 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'boulder-opal-toolkits',
    'version': '2.0.0b0',
    'description': 'Q-CTRL Boulder Opal Toolkits',
    'long_description': '# Q-CTRL Boulder Opal Toolkits\n\nToolkit of convenience functions and classes for the Q-CTRL Python package.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
