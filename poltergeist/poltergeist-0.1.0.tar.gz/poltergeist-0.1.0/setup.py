# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poltergeist']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poltergeist',
    'version': '0.1.0',
    'description': '',
    'long_description': '# poltergeist',
    'author': 'Alexander Malyga',
    'author_email': 'alexander@malyga.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexandermalyga/poltergeist',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
