# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_cover_letters',
 'py_cover_letters.cli_commands',
 'py_cover_letters.db',
 'tests',
 'tests.cli_commands',
 'tests.db',
 'tests.fixtures']

package_data = \
{'': ['*'],
 'py_cover_letters': ['templates/*'],
 'tests.fixtures': ['templates/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'docxtpl>=0.16.4,<0.17.0',
 'openpyxl>=3.0.10,<4.0.0',
 'sqlmodel>=0.0.8,<0.0.9',
 'toml>=0.10.2,<0.11.0',
 'twine>=4.0.2,<5.0.0']

entry_points = \
{'console_scripts': ['py-cover-letters = py_cover_letters.cli:main']}

setup_kwargs = {
    'name': 'py-cover-letters',
    'version': '0.3.0',
    'description': 'Project to create, manage and email cover letters.',
    'long_description': "# Py Cover Letters\n\n\n[![pypi](https://img.shields.io/pypi/v/py-cover-letters.svg)](https://pypi.org/project/py-cover-letters/)\n[![python](https://img.shields.io/pypi/pyversions/py-cover-letters.svg)](https://pypi.org/project/py-cover-letters/)\n[![Build Status](https://github.com/luiscberrocal/py-cover-letters/actions/workflows/dev.yml/badge.svg)](https://github.com/luiscberrocal/py-cover-letters/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/luiscberrocal/py-cover-letters/branch/main/graphs/badge.svg)](https://codecov.io/github/luiscberrocal/py-cover-letters)\n\n\n\nProject to create, manage and email cover letters.\n\nThis app will only run in linux and Mac OS. I'm not sure it will run in Windows.\n\n\n* Documentation: <https://luiscberrocal.github.io/py-cover-letters>\n* GitHub: <https://github.com/luiscberrocal/py-cover-letters>\n* PyPI: <https://pypi.org/project/py-cover-letters/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n",
    'author': 'Luis C. Berrocal',
    'author_email': 'luis.berrocal.1942@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luiscberrocal/py-cover-letters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
