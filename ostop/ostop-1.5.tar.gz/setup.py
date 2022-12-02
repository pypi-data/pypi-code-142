# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ostop']

package_data = \
{'': ['*']}

install_requires = \
['datetime>=4.7,<5.0', 'hurry-filesize>=0.9,<0.10', 'psutil>=5.9.3,<6.0.0']

entry_points = \
{'console_scripts': ['ostop = ostop.main:main']}

setup_kwargs = {
    'name': 'ostop',
    'version': '1.5',
    'description': 'Cross-Compatible Python implementation of top command.',
    'long_description': "# top\n\n[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)\n[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)\n[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)\n\nA Cross-Platform Python implementation of 'top' command using Psutil.\n\n## What top Does\n\nTop is able to get most of the top information with the restrictions that\ncome with running it at the program level. Different statistics are shown\nbased on the operating system that this project is run on. top works on\nMacOS, Linux, and Windows operating systems.\n\n## How to Get Started With top\n\n### PYPI Installation\n\nYou can install top through running this command in your terminal:\n\n``` pipx install ostop ```\n\nOnce this command finishes running, you can then run commands in\nthese two different formats:\n\n``` ostop ```\n\nThe command with no extra parameters will make the program run\nin an infinite loop forever until you close your terminal or\nuse a Keyboard Interrupt.\n\n``` ostop <integer value> ```\n\nThe command with an integer value will make the program run\nfor the number of iterations/seconds you specify.\n\n### Local Installation\n\nYou can get started with top by cloning the repository and running this command:\n\n``` python src/top.py ```\n\nin the base directory. Like the top command, this will run forever.\nYou can exit out of the program by entering a Keyboard Interrupt or exiting\nyour terminal altogether. You can also specify the amount of times you want\nthe program to run by giving an integer input. For example, you can run the\nprogram for one iteration by writing this command:\n\n``` python src/top.py 1 ```\n\n## Running GatorGrade Checks\n\nThis repository is able to be automatically assessed using GatorGrade.\nThese checks can be run from the repository's base directory by running this command\nin the base directory if you already have GatorGrade installed:\n\n```gatorgrade --config config/gatorgrade.yml```\n\nIf you do not have GatorGrade installed yet on your local machine, you can install\nit by using this command:\n\n```pip install gatorgrade```\n\nThese checks ensure that files are formatted correctly with proficient levels of\npolish and also run without crashing. GatorGrade checks are useful both\nduring and after development.\n",
    'author': 'Katherine Burgess',
    'author_email': '20burgessk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/burgess01/top',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
