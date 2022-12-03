# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alpinejsstate']

package_data = \
{'': ['*']}

install_requires = \
['jsbeautifier>=1.14.7,<2.0.0', 'pscript>=0.7.7,<0.8.0']

setup_kwargs = {
    'name': 'alpinejsstate',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Thiago César',
    'author_email': 'k1mbl3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
