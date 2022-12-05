# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['upgrade_knausj']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.1.29,<4.0.0',
 'pre-commit>=2.20.0,<3.0.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['upgrade-knausj = upgrade_knausj.main:app']}

setup_kwargs = {
    'name': 'upgrade-knausj',
    'version': '0.3.14',
    'description': '',
    'long_description': "# Upgrade `knausj`\n\nHelper for performing `knausj` upgrades.\n\n## Assumptions\n\n- You have a fork of `knausj`\n- You haven't altered your pre-commit config. If you don't know what that means, then you are fine 😊\n\n## Installation\n\n1. Install [`pipx`](https://pypa.github.io/pipx/)\n2. Run `pipx install pre-commit`\n3. Run `pipx install upgrade-knausj`\n\n## How to run\n\n1. Push your changes to your fork\n2. Run `upgrade-knausj`\n3. If necessary, resolve any merge conflicts, commit, then re-run `upgrade-knausj`\n4. Repeat steps 2-3 until it says you're done\n5. Do a pull from your main Talon user directory\n6. Restart Talon and look in the log file for errors\n",
    'author': 'Pokey Rule',
    'author_email': '755842+pokey@users.noreply.github.com',
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
