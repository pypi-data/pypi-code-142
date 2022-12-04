# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['volunor', 'volunor.core', 'volunor.test']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'volunor',
    'version': '0.0.1b0',
    'description': 'Command line tools, with ease',
    'long_description': '<div align="center">\n  <a href="https://github.com/othneildrew/Best-README-Template">\n    <img src="https://i.postimg.cc/15sX0dQZ/test.png" alt="Logo" width="125" height="125">\n  </a>\n\n  <h3><b>Völunðr</b></h3>\n  <i>Command Line Tools with ease</i>\n</div>\n\n## Run tests\n\n### Install dependencies\n\n```shell\nsudo apt install "^python3\\.(7|8|9|10|11)-venv$"\npip install poetry tox\n```\n',
    'author': 'Thomas Mahe',
    'author_email': 'contact@tmahe.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
