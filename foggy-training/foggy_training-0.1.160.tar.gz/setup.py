# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foggy_training',
 'foggy_training.addons',
 'foggy_training.base',
 'foggy_training.datasets',
 'foggy_training.models',
 'foggy_training.wrapper']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0', 'torchinfo>=1.7.1,<2.0.0']

setup_kwargs = {
    'name': 'foggy-training',
    'version': '0.1.160',
    'description': '',
    'long_description': None,
    'author': 'JanDiers',
    'author_email': 'jan.diers@uni-jena.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
