# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kal', 'kal.base', 'kal.commands', 'kal.utils']

package_data = \
{'': ['*']}

install_requires = \
['cleo>=0.8.1,<0.9.0', 'cookiecutter>=2.1.1,<3.0.0', 'pend>=1.0.2,<2.0.0']

entry_points = \
{'console_scripts': ['kal = kal.runner:main']}

setup_kwargs = {
    'name': 'kal',
    'version': '0.3.1',
    'description': 'Personal assistant cli tool',
    'long_description': 'None',
    'author': 'Jrog',
    'author_email': 'jrog612@gmail.com',
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
