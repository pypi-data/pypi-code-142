# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quality_estimation']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp==3.6.2',
 'async-timeout==3.0.1',
 'transquest==1.1.1',
 'typing-extensions==3.7.4.3',
 'uvloop==0.14.0']

setup_kwargs = {
    'name': 'quality-estimation',
    'version': '0.1.0',
    'description': '',
    'long_description': '# quality-estimation',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
