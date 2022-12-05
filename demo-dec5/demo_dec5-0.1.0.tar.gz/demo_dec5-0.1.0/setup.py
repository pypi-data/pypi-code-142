# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['demo_dec5']

package_data = \
{'': ['*']}

install_requires = \
['nano>=0.10.0,<0.11.0', 'pandas>=1.5.2,<2.0.0', 'streamlit>=1.15.2,<2.0.0']

setup_kwargs = {
    'name': 'demo-dec5',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'krushna Panchvishe',
    'author_email': 'krushnap@cdac.in',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
