# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dezmq']

package_data = \
{'': ['*']}

install_requires = \
['ezbee>=0.1.2,<0.2.0',
 'logzero>=1.7.0,<2.0.0',
 'pyzmq>=25.0.0b1,<26.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'set-loglevel>=0.1.2,<0.2.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['dezmq = dezmq.__main__:app']}

setup_kwargs = {
    'name': 'dezmq',
    'version': '0.1.0a1',
    'description': 'dezmq',
    'long_description': '# dezbee-zmq\n[![pytest](https://github.com/ffreemt/dezbee-zmq/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-zmq/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezmq.svg)](https://badge.fury.io/py/dezmq)\n\n[de|ez|dz]bee via zmq (zmq.REP)\n\n## python 3.8 only\nSince some of dezmq\'s dependent packages (notably `fast-scores` etc) are `python 3.8` only.\n\n## Pre-install\n* fasttext\n  * `pip install fasttext` (linux) or `pip install fasttext*whl` (Windows)\n* pycld2, PyICU\n  * e.g. `poetry run pip install pycld2-0.41-cp38-cp38-win_amd64.wh PyICU-2.9-cp38-cp38-win_amd64.whl` \n* polyglot fix:\n  * `poetry run pip install -U git+https://github.com/aboSamoor/polyglot.git@master` or\n  *  `pip install artifects\\polyglot-16.7.4.tar.gz` (modified cloned polyglot: futures removed from requirements.txt)\n\nOr (excerpt from `routine-tests.yml`)\n```bash\n      - name: Pre-install fastext pycld2 pyicu\n        run: |\n          if [ "$RUNNER_OS" == "Windows" ]; then\n            poetry run pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/fasttext-0.9.2-cp38-cp38-win_amd64.whl\n            poetry run pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/pycld2-0.41-cp38-cp38-win_amd64.whl\n            poetry run pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/PyICU-2.8.1-cp38-cp38-win_amd64.whl\n            poetry run pip install pybind11\n          else\n            poetry run pip install fasttext pycld2 pyicu\n          fi\n          poetry run pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz\n        shell: bash\n```\n\nRefer to [workflows/actions](https://github.com/ffreemt/dezbee-zmq/blob/main/.github/workflows/routine-tests.yml) for detailed steps.\n\n## Install it\n\n```shell\npip install dezmq\n# pip install git+https://github.com/ffreemt/dezbee-zmq\n# poetry add git+https://github.com/ffreemt/dezbee-zmq\n# git clone https://github.com/ffreemt/dezbee-zmq && cd dezbee-zmq\n```\n\n## Use it\nDEZMQ_HOST (default local) and  DEZMQ_PORT (default 5555)\n```bash\npython -m dezmq\n\n# docs\npython -m dezmq --help\n```\n',
    'author': 'ffreemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/dezbee-zmq',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
