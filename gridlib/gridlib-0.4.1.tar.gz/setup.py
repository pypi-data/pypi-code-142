# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gridlib', 'gridlib.io', 'gridlib.io.tests', 'gridlib.plot']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.0,<4.0.0',
 'psutil>=5.9.0,<6.0.0',
 'scipy>=1.6.0,<2.0.0',
 'tqdm>=4.63.0,<5.0.0']

setup_kwargs = {
    'name': 'gridlib',
    'version': '0.4.1',
    'description': 'Python package to perform GRID analysis on fluorescence survival time distributions.',
    'long_description': '\n# GRIDLib\n\n<div align="center">\n\n[![PyPI - Version](https://img.shields.io/pypi/v/gridlib.svg)](https://pypi.python.org/pypi/gridlib)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gridlib.svg)](https://pypi.python.org/pypi/gridlib)\n[![Tests](https://github.com/boydcpeters/gridlib/workflows/tests/badge.svg)](https://github.com/boydcpeters/gridlib/actions?workflow=tests)\n[![Codecov](https://codecov.io/gh/boydcpeters/gridlib/branch/main/graph/badge.svg)](https://codecov.io/gh/boydcpeters/gridlib)\n[![Read the Docs](https://readthedocs.org/projects/gridlib/badge/)](https://gridlib.readthedocs.io/)\n[![PyPI - License](https://img.shields.io/pypi/l/gridlib.svg)](https://pypi.python.org/pypi/gridlib)\n\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)\n\n</div>\n\nPython package to perform GRID analysis on fluorescence survival time distributions.\n\n* GitHub repo: <https://github.com/boydcpeters/gridlib.git>\n* Documentation: <https://gridlib.readthedocs.io>\n* Free software: GNU General Public License v3\n\n## Features\n\n* TODO\n\n## Quickstart\n\nTODO\n\n## References\n\nThe GRID fitting procedure implemented in this package is based on the following paper:\n\n```latex\n@article{reisser2020inferring,\n  title={Inferring quantity and qualities of superimposed reaction rates from single molecule survival time distributions},\n  author={Reisser, Matthias and Hettich, Johannes and Kuhn, Timo and Popp, Achim P and Gro{\\ss}e-Berkenbusch, Andreas and Gebhardt, J Christof M},\n  journal={Scientific reports},\n  volume={10},\n  number={1},\n  pages={1--13},\n  year={2020},\n  publisher={Nature Publishing Group}\n}\n```\n\n## Credits\n\nThis package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.\n\n[cookiecutter]: https://github.com/cookiecutter/cookiecutter\n[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage\n',
    'author': 'Boyd Christiaan Peters',
    'author_email': 'boyd.c.peters@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/boydcpeters/gridlib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
