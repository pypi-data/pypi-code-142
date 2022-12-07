# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mappi']

package_data = \
{'': ['*'], 'mappi': ['data/*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'fastapi>=0.87.0,<0.88.0',
 'rich>=12.6.0,<13.0.0',
 'uvicorn>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['mappi = mappi.cli:cli']}

setup_kwargs = {
    'name': 'mappi',
    'version': '0.5.0',
    'description': 'Spin up webserver from a yaml config file',
    'long_description': '# mappi\n\n![Tests](https://github.com/bmwant/mappi/actions/workflows/tests.yml/badge.svg)\n[![PyPI](https://img.shields.io/pypi/v/mappi)](https://pypi.org/project/mappi/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mappi)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![EditorConfig](https://img.shields.io/badge/-EditorConfig-grey?logo=editorconfig)](https://editorconfig.org/)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\n### Installation\n\n```bash\n$ pip install mappi\n$ mappi  # run server with example configuration\n```\n\n### Usage\n\n```bash\n# generate minimal config file\n$ mappi config > mappi.yml\n\n# adjust routes as needed or create your own config\n$ vim mappi.yml\n\n# dump configuration with all the options available to a file\n$ mappi config --full > mappi.yml\n\n# start your webserver\n$ mappi\n\n# start server with configuration stored in different filename\n$ mappi --config my-config-file.yml\n```\n\n### Development\n\n```bash\n$ poetry install\n$ poetry run python -m mappi\n\n$ poetry run mappi\n\n$ pre-commit install\n$ pre-commit autoupdate\n```\n',
    'author': 'Misha Behersky',
    'author_email': 'bmwant@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
