# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py2of', 'py2of.domain', 'py2of.service']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'coloredlogs>=15.0.1,<16.0.0']

entry_points = \
{'console_scripts': ['py2of = py2of.__main__:main']}

setup_kwargs = {
    'name': 'py2of',
    'version': '0.1.1',
    'description': 'Ultimate PyFoam',
    'long_description': "# Ultimate PyFoam\n\nhttps://doc.cfd.direct/openfoam/user-guide-v8/basic-file-format\n\n[![PyPI](https://img.shields.io/pypi/v/py2of.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/py2of.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/py2of)][pypi status]\n[![License](https://img.shields.io/pypi/l/py2of)][license]\n\n[![Read the documentation at https://py2of.readthedocs.io/](https://img.shields.io/readthedocs/py2of/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/ARostekMU/py2of/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/ARostekMU/py2of/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/py2of/\n[read the docs]: https://py2of.readthedocs.io/\n[tests]: https://github.com/ARostekMU/py2of/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/ARostekMU/py2of\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Ultimate PyFoam_ via [pip] from [PyPI]:\n\n```console\n$ pip install py2of\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Ultimate PyFoam_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/ARostekMU/py2of/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/ARostekMU/py2of/blob/main/LICENSE\n[contributor guide]: https://github.com/ARostekMU/py2of/blob/main/CONTRIBUTING.md\n[command-line reference]: https://py2of.readthedocs.io/en/latest/usage.html\n\n## Python virtual environment cheatsheet\n\nWhich **python**/**pip** am I using?\n\n```\nwhich python\nwhich pip\n```\n\nList python packages installed using **pip**\n\n```\npip list\n```\n\nUse **venv** to create new virtual environment called for example test_env in the current working directory\n\n```\npython -m venv test_env\n```\n\nStart using test_env virtual environment\n\n```\nsource test_env/bin/activate\n```\n\n`which python` should now show you the path to /something/test_env/bin/python\n\nIf you now do for example `pip install numpy`, **numpy** will be installed only into the test_env virtual environment. `pip list` will show that only **pip**, **setuptools** and **numpy** are installed.\n\nStop working in the current virtual environment\n\n```\ndeactivate\n```\n\nInstall another python version, for example 3.11.0\n\n```\npyenv install 3.11.0\n```\n\nList installed python versions\n\n```\npyenv versions\n```\n\nStart using python 3.11.0\n\n```\npyenv local 3.11.0\n```\n\nCommand `python` should now open a **python shell** on version 3.11.0\n\nNow you should be able to create a virtual environment with this new python version :)\n\n<br></br>\n\n**Poetry** is a tool for dependency management and packaging in Python. Moreover, it can create it's own virtual environments, which makes your life easier.\nIf you're in a folder of a project which uses **Poetry** (for example the Claudio's template we're using is such a project), you can find out\nwhich virtual environment this project is using by\n\n```\npoetry env info\n```\n\nIf you want to start using this environment in your terminal, you don't have to do the whole `source /something/activate` thing anymore, you can just type\n\n```\npoetry shell\n```\n\nand the environment will be activated.\n\nIf you want to update a package, or a python version, you can do so manually in a file _pyproject.toml_. For example, you might rewrite python version from ^3.7 to ^3.8.\nIf you update the _pyproject.toml_ like this, you must update _poetry.lock_ by doing\n\n```\npoetry lock\n```\n\nIn _poetry.lock_ you can find all the packages and versions which your project is using. In order to add a new package, for example **numpy**, type\n\n```\npoetry add numpy\n```\n\nIf you don't know which command to use, or what all the possibilities offered by the tool you are using are, there are multiple sources where to look.\n\nYou can always try to run the tool with no arguments like this (not just **poetry**):\n\n```\npoetry\n```\n\nwhich usually outputs some information about usage and a list of available commands.\n\nIf that is not enough, there is usually some kind of official documentation which is only one google search away: https://python-poetry.org/docs/basic-usage/\n\nIn case of desperation, you might want to try going to Stack Overflow https://stackoverflow.com/.\n",
    'author': 'Petr Zikan',
    'author_email': 'zikan.p@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ziky5/py2of',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
