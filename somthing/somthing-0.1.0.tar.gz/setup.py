# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['somthing']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'somthing',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'sina',
    'author_email': 'khalili@sfu.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
