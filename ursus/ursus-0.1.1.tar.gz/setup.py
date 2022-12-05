# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ursus', 'ursus.powerdns']

package_data = \
{'': ['*'], 'ursus.powerdns': ['templates/*']}

install_requires = \
['quart>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'ursus',
    'version': '0.1.1',
    'description': 'PowerDNS control panel',
    'long_description': 'Ursus\n=====\n\nUrsus arctos - the brown bear\n\nA PowerDNS control panel\n\nInstallation\n-----\n\nUsage\n-----\n\nContributing\n-----\n\nSee the <CONTRIBUTING> file\n\nLicense\n-----\n\nThis code in this repository is licensed under the [BSD-3](https://opensource.org/licenses/BSD-3). See the <LICENSE> file in this repository for the full license.\n',
    'author': 'Quark',
    'author_email': 'quark@whiisker.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.sr.ht/~whiisker/ursus/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
