# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mepe']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'prometheus-client>=0.15.0,<0.16.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['mepe = mepe.main:main']}

setup_kwargs = {
    'name': 'mepe',
    'version': '0.1.2',
    'description': '',
    'long_description': '# Prometheus Metrics Explorer\n\nCli Prometheus metrics viewer.\n',
    'author': 'laixintao',
    'author_email': 'laixintaoo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
