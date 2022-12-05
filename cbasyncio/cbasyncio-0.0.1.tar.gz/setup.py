# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cbasyncio', 'cbasyncio.streamz']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.2.0,<5.0.0']

extras_require = \
{'uvloop': ['uvloop>=0.16.0,<0.17.0']}

setup_kwargs = {
    'name': 'cbasyncio',
    'version': '0.0.1',
    'description': '',
    'long_description': '## cbasyncio - Usefule async utilties\n\nA useful collection of asyncio tools\n\nFeatures\n--------\n\n* Async binary and file i/o\n* Taskgroups (backported from python 3.11)\n* Channels (`go` style)\n* Context groups\n* async `itertools` functions (`map`, `filter`, `chain`, etc.)',
    'author': 'Bryan Matteson',
    'author_email': 'bryan@matteson.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
