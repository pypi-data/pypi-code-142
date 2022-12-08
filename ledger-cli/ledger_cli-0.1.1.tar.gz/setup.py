# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ledgercli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'numpy>=1.23.5,<2.0.0', 'pandas>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['ledgercli = ledgercli.cli:cli']}

setup_kwargs = {
    'name': 'ledger-cli',
    'version': '0.1.1',
    'description': 'ledger-cli',
    'long_description': "# ledger-cli\n\n[![PyPI](https://img.shields.io/pypi/v/ledger-cli.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/ledger-cli.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/ledger-cli)][python version]\n[![License](https://img.shields.io/pypi/l/ledger-cli)][license]\n\n[![Read the documentation at https://ledger-cli.readthedocs.io/](https://img.shields.io/readthedocs/ledger-cli/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/tilschuenemann/ledger-cli/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/tilschuenemann/ledger-cli/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/ledger-cli/\n[status]: https://pypi.org/project/ledger-cli/\n[python version]: https://pypi.org/project/ledger-cli\n[read the docs]: https://ledger-cli.readthedocs.io/\n[tests]: https://github.com/tilschuenemann/ledger-cli/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/tilschuenemann/ledger-cli\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\nledger-cli strives to achieve two goals regarding your personal finance:\n\n1. Providing you with an easy format for fine-tuning your transactions.\n2. Serving a local dashboard for easy analysis and interpration.\n\n[For a more in-depth view, take a look at the features here.]()\n\n## Installation\n\nYou can install _ledger-cli_ via [pip] from [PyPI]:\n\n```console\n$ pip install ledger-cli\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_ledger-cli_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/tilschuenemann/ledger-cli/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/tilschuenemann/ledger-cli/blob/main/LICENSE\n[contributor guide]: https://github.com/tilschuenemann/ledger-cli/blob/main/CONTRIBUTING.md\n[command-line reference]: https://ledger-cli.readthedocs.io/en/latest/usage.html\n",
    'author': 'Til Schünemann',
    'author_email': 'til.schuenemann@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tilschuenemann/ledger-cli',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
