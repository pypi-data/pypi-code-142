# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gh_star_count', 'gh_star_count.cli']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'graphqlclient>=0.2.4,<0.3.0',
 'pygithub>=1.56,<2.0',
 'python-graphql-client>=0.4.3,<0.5.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0',
 'typer[all]>=0.6.1,<0.7.0',
 'types-requests>=2.28.11.2,<3.0.0.0']

setup_kwargs = {
    'name': 'gh-star-count',
    'version': '1.1.0',
    'description': 'python program to interact with Github and retrieve data',
    'long_description': '# Starcount - GitHub CLI\n\nPython package to interact with GitHub and retrieve data.\n\n- commands:\n\nCount all stars of all repos of yourself, a specified user or an organization.\n\nAllow a nicely printed format as default.\n\nModify your user description by adding a tea emoji and a heart.\n\nSet your user status (top-right when clicking on username):\nemoji and status message.\n\n- Focus points:\n\nFocus on usability and clarity with Typer for end-user\n\nIntegrate best practices about linting, CI/CD, documentation, package management\nand pypi deployment.\n\n- TODO :\n\nPrint out details about yourself, a user or organization. \n\nAllow for output in JSON.\n\n- project infos:\n\nSource Code: https://github.com/adnene-guessoum/Github_cli\n\nDocumentation: https://adnene-guessoum.github.io/Github_cli/\n',
    'author': 'Adnene_wsl',
    'author_email': 'adnen.guessoum@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
