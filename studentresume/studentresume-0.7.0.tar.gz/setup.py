# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studentresume']

package_data = \
{'': ['*'], 'studentresume': ['fonts/*', 'themes/*']}

install_requires = \
['jsonschema>=4.17.3,<5.0.0',
 'reportlab>=3.6.12,<4.0.0',
 'rich>=12.6.0,<13.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['studentresume = studentresume.run:main']}

setup_kwargs = {
    'name': 'studentresume',
    'version': '0.7.0',
    'description': '',
    'long_description': None,
    'author': 'curtiskennedy',
    'author_email': '52674197+curtiskennedy@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
