# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['movieparse']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'click>=8.0.1',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.1,<2.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['movieparse = movieparse.cli:cli']}

setup_kwargs = {
    'name': 'movieparse',
    'version': '0.4.0',
    'description': 'Movieparse',
    'long_description': '# Movieparse\n\n[![PyPI](https://img.shields.io/pypi/v/movieparse.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/movieparse.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/movieparse)][python version]\n[![License](https://img.shields.io/pypi/l/movieparse)][license]\n\n[![Read the documentation at https://movieparse.readthedocs.io/](https://img.shields.io/readthedocs/movieparse/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/tilschuenemann/movieparse/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/tilschuenemann/movieparse/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/movieparse/\n[status]: https://pypi.org/project/movieparse/\n[python version]: https://pypi.org/project/movieparse\n[read the docs]: https://movieparse.readthedocs.io/\n[tests]: https://github.com/tilschuenemann/movieparse/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/tilschuenemann/movieparse\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n`movieparse` is an asynchronous utility for fetching bulk movie data from [TMDB](https://www.themoviedb.org/) using movie title and optionally release year. It has both a Python API and a CLI.\n\nDistinction from other packages, `movieparse`:\n\n- focuses on fetching movies only.\n- can write metadata as CSV files, but is also keeps them within the movieparse object.\n- makes all API requests asynchronously and is therefore very fast.\n- casts all metadata dtypes so you don\'t have to.\n- can uses multiple sources of input and is easily extendable, as long as the input features movie title and release year.\n\n## Requirements\n\nYou\'ll need to have a TMDB API key in order to make API requests. Either specify it on initialization of Movieparse or add it as environment variable:\n\n```bash\n$ export TMDB_API_KEY="your_api_key_here"\n```\n\n## Installation\n\nYou can install _Movieparse_ via [pip] from [PyPI]:\n\n```console\n$ pip install movieparse\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Movieparse_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/tilschuenemann/movieparse/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/tilschuenemann/movieparse/blob/main/LICENSE\n[contributor guide]: https://github.com/tilschuenemann/movieparse/blob/main/CONTRIBUTING.md\n[command-line reference]: https://movieparse.readthedocs.io/en/latest/usage.html\n',
    'author': 'Til Schünemann',
    'author_email': 'til.schuenemann@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tilschuenemann/movieparse',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.7,<4.0.0',
}


setup(**setup_kwargs)
