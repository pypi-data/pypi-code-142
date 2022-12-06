# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['asunder',
 'asunder.analyze',
 'asunder.command',
 'asunder.project',
 'asunder.rope_sdk',
 'asunder.rope_sdk.find',
 'asunder.rope_sdk.refactor',
 'asunder.rope_sdk.refactor.move',
 'asunder.rope_sdk.refactor.rename',
 'asunder.utils']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.6.0,<13.0.0', 'rope>=1.4.0,<2.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['asunder = asunder:app']}

setup_kwargs = {
    'name': 'asunder',
    'version': '0.1.0',
    'description': 'CLI for refactoring python projects',
    'long_description': '[![asunder](https://github.com/lalmei/asunder/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/lalmei/asunder/actions/workflows/main.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/67d0f7c0715d81bef5f9/maintainability)](https://codeclimate.com/github/lalmei/asunder/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/67d0f7c0715d81bef5f9/test_coverage)](https://codeclimate.com/github/lalmei/asunder/test_coverage)\n',
    'author': 'Leandro G. Almeida',
    'author_email': 'leandro.g.almeida@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
