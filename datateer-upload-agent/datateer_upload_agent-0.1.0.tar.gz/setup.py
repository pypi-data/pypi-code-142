# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datateer_upload_agent']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'boto3>=1.20.49,<2.0.0',
 'click>=8.0.3,<9.0.0',
 'coverage>=6.5.0,<7.0.0']

entry_points = \
{'console_scripts': ['datateer = datateer_upload_agent.main:cli']}

setup_kwargs = {
    'name': 'datateer-upload-agent',
    'version': '0.1.0',
    'description': 'An agent that can be installed inside a firewall or VPN and used to push data to Datateer',
    'long_description': 'None',
    'author': 'Datateer',
    'author_email': 'dev@datateer.com',
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
