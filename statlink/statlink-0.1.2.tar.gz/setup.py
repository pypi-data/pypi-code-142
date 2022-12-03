# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statlink']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'aiolimiter>=1.0.0,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'lxml>=4.9.1,<5.0.0',
 'playwright>=1.28.0,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['statlink = statlink.command:main']}

setup_kwargs = {
    'name': 'statlink',
    'version': '0.1.2',
    'description': 'An asyncio based multipurpose link checker.',
    'long_description': 'None',
    'author': 'Thibaut Frain',
    'author_email': 'thibaut.frain@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
