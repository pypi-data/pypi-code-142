# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zonis', 'zonis.client', 'zonis.server']

package_data = \
{'': ['*']}

install_requires = \
['websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'zonis',
    'version': '0.3.1',
    'description': 'Agnostic IPC for Python programs ',
    'long_description': 'Zonis\n---\n\nA coro based callback system for many to one IPC setups.\n\n`pip install zonis`\n\nSee the [examples](https://github.com/Skelmis/Zonis/tree/master/exampleshttps://github.com/Skelmis/Zonis/tree/master/examples) for simple use cases.',
    'author': 'skelmis',
    'author_email': 'ethan@koldfusion.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
