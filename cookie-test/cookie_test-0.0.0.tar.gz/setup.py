# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cookie_test']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1']

entry_points = \
{'console_scripts': ['cookie-test = cookie_test.__main__:main']}

setup_kwargs = {
    'name': 'cookie-test',
    'version': '0.0.0',
    'description': 'Cookie Test',
    'long_description': "# Cookie Test\n\n[![PyPI](https://img.shields.io/pypi/v/cookie-test.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/cookie-test.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/cookie-test)][python version]\n[![License](https://img.shields.io/pypi/l/cookie-test)][license]\n\n[![Read the documentation at https://cookie-test.readthedocs.io/](https://img.shields.io/readthedocs/cookie-test/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/soshi117/cookie-test/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/soshi117/cookie-test/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/cookie-test/\n[status]: https://pypi.org/project/cookie-test/\n[python version]: https://pypi.org/project/cookie-test\n[read the docs]: https://cookie-test.readthedocs.io/\n[tests]: https://github.com/soshi117/cookie-test/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/soshi117/cookie-test\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Cookie Test_ via [pip] from [PyPI]:\n\n```console\n$ pip install cookie-test\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Cookie Test_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/soshi117/cookie-test/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/soshi117/cookie-test/blob/main/LICENSE\n[contributor guide]: https://github.com/soshi117/cookie-test/blob/main/CONTRIBUTING.md\n[command-line reference]: https://cookie-test.readthedocs.io/en/latest/usage.html\n",
    'author': 'Soshi Mizutani',
    'author_email': 'soshi.mizutani@oist.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/soshi117/cookie-test',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
