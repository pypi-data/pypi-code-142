# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['merkleproof']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'merkleproof',
    'version': '0.0.1',
    'description': '',
    'long_description': '# `merkleproof`\n\n[![Python package](https://github.com/kalaspuff/merkleproof/workflows/Python%20package/badge.svg)](https://github.com/kalaspuff/merkleproof/actions/workflows/pythonpackage.yml)\n[![pypi](https://badge.fury.io/py/merkleproof.svg)](https://pypi.python.org/pypi/merkleproof/)\n[![Made with Python](https://img.shields.io/pypi/pyversions/merkleproof)](https://www.python.org/)\n[![MIT License](https://img.shields.io/github/license/kalaspuff/merkleproof.svg)](https://github.com/kalaspuff/merkleproof/blob/master/LICENSE)\n[![Code coverage](https://codecov.io/gh/kalaspuff/merkleproof/branch/master/graph/badge.svg)](https://codecov.io/gh/kalaspuff/merkleproof/tree/master/merkleproof)\n\n*Build merkle trees, create merkle proofs, verify that the merkle root (hash root) can be reconstructed. The typical things you would do with a merkle tree.*\n\n### Creating merkle trees, merkle proofs and verifying their consistency\n\n* Simple package aimed at learning to work with merkle trees, produce proofs, etc.\n* Built to be able to generate proofs that can be used in tandem with Solidity contracts.\n* Follows OpenZeppelin\'s practices regarding produced merkle trees and proof output.\n\n```pycon\n>>> tree = MerkleTree(["a", "b"])\n>>> tree.root\n\'fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603\'\n```\n\n### Work in progress\n\nNote that this is under development and should not be used outside of a developer setting.\n',
    'author': 'Carl Oscar Aaro',
    'author_email': 'hello@carloscar.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
