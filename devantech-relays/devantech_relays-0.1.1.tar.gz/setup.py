# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devantech_relays']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'devantech-relays',
    'version': '0.1.1',
    'description': "Tool for controlling Devantech's ETH-series of relays",
    'long_description': None,
    'author': 'Karl Fredrik Haugland',
    'author_email': 'kfh@tla.wtf',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
