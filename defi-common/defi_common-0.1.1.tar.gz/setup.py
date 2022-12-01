# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['defi_common', 'defi_common.database']

package_data = \
{'': ['*']}

install_requires = \
['pre-commit>=2.20.0,<3.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'sqlalchemy>=1.4.44,<2.0.0']

setup_kwargs = {
    'name': 'defi-common',
    'version': '0.1.1',
    'description': '',
    'long_description': 'None',
    'author': 'Tomas Toth',
    'author_email': 'tomas.toth004@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
