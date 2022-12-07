# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cosmotile']

package_data = \
{'': ['*']}

install_requires = \
['astropy-healpix>=0.7,<0.8',
 'astropy>=5.1.1,<6.0.0',
 'click>=8.0.1',
 'numpy>=1.23.4,<2.0.0',
 'scipy>=1.9.3,<2.0.0']

entry_points = \
{'console_scripts': ['cosmotile = cosmotile.__main__:main']}

setup_kwargs = {
    'name': 'cosmotile',
    'version': '0.1.1',
    'description': 'Cosmotile',
    'long_description': "# Cosmotile\n\n[![PyPI](https://img.shields.io/pypi/v/cosmotile.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/cosmotile.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/cosmotile)][python version]\n[![License](https://img.shields.io/pypi/l/cosmotile)][license]\n\n[![Read the documentation at https://cosmotile.readthedocs.io/](https://img.shields.io/readthedocs/cosmotile/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/steven-murray/cosmotile/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/steven-murray/cosmotile/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/cosmotile/\n[status]: https://pypi.org/project/cosmotile/\n[python version]: https://pypi.org/project/cosmotile\n[read the docs]: https://cosmotile.readthedocs.io/\n[tests]: https://github.com/steven-murray/cosmotile/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/steven-murray/cosmotile\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n_Create cosmological lightcones from coeval simulations._\n\nThis algorithm is taken from the code in https://github.com/piyanatk/cosmotile, but\nis repackaged and re-tooled.\n\n## Features\n\n- Fast tiling of finite, periodic cosmic simulations onto arbitrary angular coordinates.\n- Generate different realizations by translation and rotation.\n\n## Installation\n\nYou can install _Cosmotile_ via [pip] from [PyPI]:\n\n```console\n$ pip install cosmotile\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Cosmotile_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\nThe algorithm used in this repository is derived from the `cosmotile` module in\nhttps://github.com/nithyanandan/AstruUtils, which was later modularised in\nhttps://github.com/piyanatk/cosmotile.\n\n## Acknowledgments\n\nIf you find `cosmotile` useful in your project, please star this repository and, if\napplicable, cite https://arxiv.org/abs/1708.00036.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/steven-murray/cosmotile/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/steven-murray/cosmotile/blob/main/LICENSE\n[contributor guide]: https://github.com/steven-murray/cosmotile/blob/main/CONTRIBUTING.md\n[command-line reference]: https://cosmotile.readthedocs.io/en/latest/usage.html\n",
    'author': 'Steven Murray',
    'author_email': 'steven.g.murray@asu.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/steven-murray/cosmotile',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
