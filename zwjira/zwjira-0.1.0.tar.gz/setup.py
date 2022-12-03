# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zwjira']

package_data = \
{'': ['*']}

install_requires = \
['atlassian-python-api>=3.31.1,<4.0.0', 'jira>=3.4.1,<4.0.0']

entry_points = \
{'console_scripts': ['zwjira = zwjira.cli:main']}

setup_kwargs = {
    'name': 'zwjira',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'neothenil',
    'author_email': '727549953@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
