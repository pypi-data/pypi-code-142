# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xcodelocalize']

package_data = \
{'': ['*']}

install_requires = \
['mtranslate>=1.8,<2.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['xcodelocalize = xcodelocalize.main:run']}

setup_kwargs = {
    'name': 'xcodelocalize',
    'version': '0.1.1',
    'description': 'Tool for automatic search and localization of .strings files',
    'long_description': '# XCodeLocalize\n\n# Requirments\nPython3.9+\n\n## Installation\n> pip install xcodelocalize \n\n## Usage\n> xcodelocalize --help',
    'author': 'MarkParker5',
    'author_email': 'markparker.it@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MarkParker5/XCodeLocalize',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
