# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pjt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pip-jump-to',
    'version': '0.0.1',
    'description': 'pip-jump-to - a quick navigation tool for the PyPI packages.',
    'long_description': '<div align="center">\n    <a href="https://pypi.org/project/poetry-dotenv">\n        <img alt="logo" src="https://github.com/volopivoshenko/poetry-dotenv/blob/main/docs/static/assets/logo.svg?raw=True" height=200>\n    </a>\n</div>\n',
    'author': 'Volodymyr Pivoshenko',
    'author_email': 'volodymyr.pivoshenko@gmail.com',
    'maintainer': 'Volodymyr Pivoshenko',
    'maintainer_email': 'volodymyr.pivoshenko@gmail.com',
    'url': 'https://github.com/volopivoshenko/pip-jump-to',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
