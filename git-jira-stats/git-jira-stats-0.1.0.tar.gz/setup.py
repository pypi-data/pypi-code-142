# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_jira_stats']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'jsonpickle>=3.0.0,<4.0.0']

entry_points = \
{'console_scripts': ['rtd = git_jira_stats.main:fire_main']}

setup_kwargs = {
    'name': 'git-jira-stats',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Mikhail Putilov',
    'author_email': 'Mikhail.Putilov@dimoco.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
