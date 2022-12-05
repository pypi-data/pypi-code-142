# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openterrace',
 'openterrace.bed_substances',
 'openterrace.boundary_conditions',
 'openterrace.convection_schemes',
 'openterrace.diffusion_schemes',
 'openterrace.domains',
 'openterrace.fluid_substances',
 'openterrace.postprocessing',
 'openterrace.tutorials']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.1,<4.0.0',
 'numba>=0.56.3,<0.57.0',
 'numpy>=1.23.4,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pytest>=7.1.3,<8.0.0',
 'scipy>=1.9.3,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'openterrace',
    'version': '0.0.4',
    'description': 'OpenTerrace is a pure Python framework for thermal energy storage packed bed simulations',
    'long_description': '[![Logo](docs/_figures/logo-banner-paths-grey.svg)](#)\n\nOpenTerrace is a pure Python framework for thermal energy storage packed bed simulations. It is built from the ground up to be flexible and extendable on modern Python 3.x with speed in mind. It utilises Nvidia CUDA cores to harness the power of modern GPUs and has automatic fallback to CPU cores.\n\nOpenTerrace uses awesome open-source software such as\n[Numba](https://numba.pydata.org), [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/):grey_exclamation:\n\n### [Read the docs](https://openterrace.github.io/openterrace-python/)\n\n## Why OpenTerrace?\n- **FAST**  \nBy making use of modern compilers and optimised tri-diagonal matrix solvers, OpenTerrace approaches the speed of compiled C or FORTRAN code with the added convenience of easy-to-read Python language.\n\n- **FLEXIBLE**  \nOpenTerrace is built from the ground up to be flexible for easy integration in system models or optimisation loops.\n\n- **EXTENDABLE**  \nModules for new materials such as non-spherical rocks or exotic Phase Change Materials (PCM) can easily be plugged into the OpenTerrace framework.\n\n## Want to contribute?\nContributions are welcome :pray: Feel free to send pull requests or get in touch with me to discuss how to collaborate. More details in the [docs](https://openterrace.github.io/openterrace-python/).\n\n## Code contributors\n* Jakob Hærvig, Associate Professor, AAU Energy, Aalborg University, Denmark',
    'author': 'Jakob Hærvig',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OpenTerrace/openterrace-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
