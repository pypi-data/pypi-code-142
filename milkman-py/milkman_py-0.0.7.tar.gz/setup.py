# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['milkman_py']

package_data = \
{'': ['*']}

install_requires = \
['eth_abi==2.2.0']

setup_kwargs = {
    'name': 'milkman-py',
    'version': '0.0.7',
    'description': '',
    'long_description': '',
    'author': 'charlesndalton',
    'author_email': 'charles.n.dalton@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
