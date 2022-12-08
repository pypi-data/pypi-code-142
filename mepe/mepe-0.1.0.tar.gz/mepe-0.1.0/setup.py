# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mepe']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'mepe',
    'version': '0.1.0',
    'description': '',
    'long_description': '# metrics-explorer\nCli Prometheus metrics viewer.\n',
    'author': 'laixintao',
    'author_email': 'laixintaoo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
