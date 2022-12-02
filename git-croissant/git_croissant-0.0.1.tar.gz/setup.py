# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_croissant', 'git_croissant.commands']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['abruti = git_croissant.cli:app']}

setup_kwargs = {
    'name': 'git-croissant',
    'version': '0.0.1',
    'description': 'French Git CLI to respect the Toubon Law in France.',
    'long_description': '# Git croissant\n\nFrench Git CLI to respect the Toubon Law in France.\n\n## Installation\n\n```bash\npipx install git-croissant\n```\n\n## Usage\n\nGit commands and their options and arguments are translated into French.\n\nFor now the coverage is far from being exhaustive, and there is no documentation so please read the source code.\n\nSome examples:\n\n```bash\nabruti clone --profondeur 3 https://github.com/x/y.git\nabruti tire\nabruti pousse\n```\n\n## Development\n\nInstall [Poetry](https://python-poetry.org/) then:\n\n```bash\npoetry install\npoetry shell\n\nabruti ...\n```\n',
    'author': 'Christophe Benz',
    'author_email': 'christophe.benz@gmail.com',
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
