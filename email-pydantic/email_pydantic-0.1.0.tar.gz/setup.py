# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['email_pydantic']

package_data = \
{'': ['*']}

install_requires = \
['DateTime>=4.7,<5.0',
 'IMAPClient>=2.3.1,<3.0.0',
 'email-validator>=1.3.0,<2.0.0',
 'html2text>=2020.1.16,<2021.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pytz>=2022.6,<2023.0',
 'zope.interface>=5.5.2,<6.0.0']

entry_points = \
{'console_scripts': ['cli_command_name = package_name:function']}

setup_kwargs = {
    'name': 'email-pydantic',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'alexander.mescheryakov',
    'author_email': '.mescheryakov@semrush.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MattiooFR/package_name',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
