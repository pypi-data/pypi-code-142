# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rubrical']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['rubrical = rubrical.main:app']}

setup_kwargs = {
    'name': 'rubrical',
    'version': '0.0.1',
    'description': 'A Python CLI to encourage (😅) people to update their dependencies!',
    'long_description': '# rubrical\nA Python CLI to encourage (😅) people to update their dependencies!\n',
    'author': 'Ivan Lee',
    'author_email': 'ivanklee86@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ivanklee86/rubrical',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
