# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wfdb', 'wfdb.io', 'wfdb.io.convert', 'wfdb.plot', 'wfdb.processing']

package_data = \
{'': ['*']}

install_requires = \
['SoundFile>=0.10.0,<0.12.0',
 'matplotlib>=3.2.2,<4.0.0',
 'numpy>=1.10.1,<2.0.0',
 'pandas>=1.0.0,<2.0.0',
 'requests>=2.8.1,<3.0.0',
 'scipy>=1.0.0,<2.0.0']

extras_require = \
{'dev': ['pytest>=7.1.1,<8.0.0',
         'pytest-xdist>=2.5.0,<3.0.0',
         'pylint>=2.13.7,<3.0.0',
         'black>=22.3.0,<23.0.0',
         'Sphinx>=4.5.0,<5.0.0']}

setup_kwargs = {
    'name': 'wfdb',
    'version': '4.1.0',
    'description': 'The WFDB Python package: tools for reading, writing, and processing physiologic signals and annotations.',
    'long_description': '# The WFDB Python Package\n\n![signals](https://raw.githubusercontent.com/MIT-LCP/wfdb-python/main/demo-img.png)\n\n[![tests workflow](https://github.com/MIT-LCP/wfdb-python/actions/workflows/run-tests.yml/badge.svg)](https://github.com/MIT-LCP/wfdb-python/actions?query=workflow%3Arun-tests+event%3Apush+branch%3Amain)\n[![PyPI Downloads](https://img.shields.io/pypi/dm/wfdb.svg?label=PyPI%20downloads)](https://pypi.org/project/wfdb/)\n[![PhysioNet Project](https://img.shields.io/badge/DOI-10.13026%2Fegpf--2788-blue)](https://doi.org/10.13026/egpf-2788)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/wfdb.svg)](https://pypi.org/project/wfdb)\n\n## Introduction\n\nA Python-native package for reading, writing, processing, and plotting physiologic signal and annotation data. The core I/O functionality is based on the Waveform Database (WFDB) [specifications](https://github.com/wfdb/wfdb-spec/).\n\nThis package is heavily inspired by the original [WFDB Software Package](https://www.physionet.org/content/wfdb/), and initially aimed to replicate many of its command-line APIs. However, the projects are independent, and there is no promise of consistency between the two, beyond each package adhering to the core specifications.\n\n## Documentation and Usage\n\nSee the [documentation site](http://wfdb.readthedocs.io) for the public APIs.\n\nSee the [demo.ipynb](https://github.com/MIT-LCP/wfdb-python/blob/main/demo.ipynb) notebook file for example use cases.\n\n## Installation\n\nThe distribution is hosted on PyPI at: <https://pypi.python.org/pypi/wfdb/>. The package can be directly installed from PyPI using either pip or poetry:\n\n```sh\npip install wfdb\npoetry add wfdb\n```\n\nOn Linux systems, accessing _compressed_ WFDB signal files requires installing `libsndfile`, by running `sudo apt-get install libsndfile1` or `sudo yum install libsndfile`. Support for Apple M1 systems is a work in progess (see <https://github.com/bastibe/python-soundfile/issues/310> and <https://github.com/bastibe/python-soundfile/issues/325>).\n\nThe development version is hosted at: <https://github.com/MIT-LCP/wfdb-python>. This repository also contains demo scripts and example data. To install the development version, clone or download the repository, navigate to the base directory, and run:\n\n```sh\n# Without dev dependencies\npip install .\npoetry install\n\n# With dev dependencies\npip install ".[dev]"\npoetry install -E dev\n\n# Install the dependencies only\npoetry install -E dev --no-root\n```\n\n**See the [note](https://github.com/MIT-LCP/wfdb-python/blob/main/DEVELOPING.md#package-and-dependency-management) about dev dependencies.**\n\n## Developing\n\nPlease see the [DEVELOPING.md](https://github.com/MIT-LCP/wfdb-python/blob/main/DEVELOPING.md) document for contribution/development instructions.\n\n## Citing\n\nWhen using this resource, please cite the software [publication](https://physionet.org/content/wfdb-python/) on PhysioNet.\n',
    'author': 'The Laboratory for Computational Physiology',
    'author_email': 'contact@physionet.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MIT-LCP/wfdb-python/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
