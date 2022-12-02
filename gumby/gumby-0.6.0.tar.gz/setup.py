# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gumby']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'lacecore[obj]>=3.0.0a0',
 'meshlab-pickedpoints>=3.0,<5.0',
 'numpy',
 'pyyaml']

setup_kwargs = {
    'name': 'gumby',
    'version': '0.6.0',
    'description': 'Stretch polygonal meshes in segments along an axis',
    'long_description': 'None',
    'author': 'Paul Melnikow',
    'author_email': 'github@paulmelnikow.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lace/gumby',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
