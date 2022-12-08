# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ansible_deployment',
 'ansible_deployment.inventory_plugins',
 'ansible_deployment.inventory_plugins.helpers',
 'ansible_deployment.inventory_plugins.inventory_sources',
 'ansible_deployment.inventory_plugins.inventory_writers']

package_data = \
{'': ['*'], 'ansible_deployment': ['templates/*']}

install_requires = \
['GitPython>=3.1.26',
 'Jinja2>=3.0.3',
 'PyYAML>=6.0',
 'click>=8.0.3',
 'cryptography>=36.0.1',
 'hvac>=0.11.2',
 'pygments>=2.13.0,<3.0.0']

entry_points = \
{'console_scripts': ['ansible-deployment = ansible_deployment.cli:cli']}

setup_kwargs = {
    'name': 'ansible-deployment',
    'version': '1.0.2',
    'description': 'Manage ansible deployments',
    'long_description': 'None',
    'author': 'torarg',
    'author_email': 'mw@1wilson.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://torarg.github.io/ansible-deployment/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
