# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['milkman_py']

package_data = \
{'': ['*']}

install_requires = \
['eth_abi==2.1.1']

setup_kwargs = {
    'name': 'milkman-py',
    'version': '0.1.1',
    'description': 'Python SDK for interacting with Milkman, a smart contract system that allows smart contracts (incl. Gnosis Safes) to swap assets through the CoW protocol.',
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
