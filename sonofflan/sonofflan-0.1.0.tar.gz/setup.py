# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sonofflan', 'sonofflan.devices']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.15.0,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'zeroconf>=0.39.4,<0.40.0']

setup_kwargs = {
    'name': 'sonofflan',
    'version': '0.1.0',
    'description': 'Library to interact with Sonoff devices through LAN mode (without eWeLink cloud)',
    'long_description': '# Sonoff LAN\n\nLibrary to interact with Sonoff devices through LAN mode (without eWeLink cloud) with firmware\nversion 3+ (tested up to version 3.5.1).\n\nAuthor: Danilo Treffiletti <urban82@gmail.com>\n\nLicense: BSD-3\n\nVersion: 0.1.0\n\n## Install\n\n### Requirements\n* Python 3.9+\n\n## Usage\nInstall with\n```pip install sonofflan```\n\nBasic utility\n```python -m sonofflan```\n\nIn your code:\nTODO (check __main__.py and tests)\n\n## Contributing\n\nPRs accepted.\n\n## License\n\nMIT (c) Danilo Treffiletti\n',
    'author': 'Danilo Treffiletti',
    'author_email': 'urban82@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
