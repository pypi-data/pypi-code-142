# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edubot']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0', 'sqlalchemy[mypy]>=1.4.44,<1.5.0']

setup_kwargs = {
    'name': 'edubot',
    'version': '0.3.0',
    'description': '',
    'long_description': '# Edubot\n\nAn AI-based bot (currently using GPT-3) designed to be used in various environment (Matrix, Mastodon, etc).\n\nThe Edubot, as the name suggests, focussed on use in educational environments:\n  1. It is intended to be educational, with a customisable personality for your context.\n  1. It can learn from interaction with users.\n  \nEdubot is the first project from Open EdTech  https://openedtech.global \n\n\n## Dev environment quickstart\n1. Install [Poetry](https://python-poetry.org/docs/)\n1. Install dependencies: `poetry install`\n1. Activate the env: `poetry shell`\n1. Install pre-commit hooks: `pre-commit install`\n1. Copy SAMPLE_CONFIG.ini and put your information in\n1. Set the `EDUBOT_CONFIG` env variable to wherever you put your config.\n',
    'author': 'exciteabletom',
    'author_email': 'tom@digitalnook.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
