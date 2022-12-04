# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alpinejswidget']

package_data = \
{'': ['*']}

install_requires = \
['soupwidget>=0.0.1,<0.0.2']

setup_kwargs = {
    'name': 'alpinejswidget',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Thiago Cesar',
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
