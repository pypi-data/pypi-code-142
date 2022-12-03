# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tgen']

package_data = \
{'': ['*']}

install_requires = \
['u-msgpack-python>=2.7.2,<3.0.0']

setup_kwargs = {
    'name': 'tgen',
    'version': '0.1.0',
    'description': 'A pretty simple text generation library',
    'long_description': '',
    'author': 'arslee07',
    'author_email': 'mail@arslee.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
