# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wasd3r', 'wasd3r.chains', 'wasd3r.chains.aptos']

package_data = \
{'': ['*']}

install_requires = \
['black==22.10.0', 'flake8>=6.0.0,<7.0.0', 'isort==5.10.1', 'pytest==7.2.0']

extras_require = \
{'aptos': ['aptos-sdk>=0.4.1,<0.5.0']}

setup_kwargs = {
    'name': 'wasd3r-sdk',
    'version': '0.0.2',
    'description': 'Wasd3r standard dev kit',
    'long_description': '# Wasd3r Python SDK\n\n# Installing SDK\n\n## Unix/macOS\n\n```sh\npython -m pip install wasd3r-sdk\n```\n\n## Windows\n\n```sh\npy -m pip install wasd3r-sdk\n```\n\n## Using specific blockchain locally (optional)\n\n### Supporting [APTOS](https://aptos.dev/)\n\nTo use APTOS without a wasd3r server, [aptos-sdk](https://aptos.dev/sdks/python-sdk) needs to be installed optionally.\n\n#### Unix/macOS\n\n```sh\npython -m pip install wasd3r-sdk[APTOS]\n```\n\n#### Windows\n\n```sh\npy -m pip install wasd3r-sdk[APTOS]\n```\n\n# Preparing DEV environment\n\n## Using `pyenv`\n\n[pyenv](https://github.com/pyenv/pyenv) could be installed via [this link](https://github.com/pyenv/pyenv#installation).\n\n### Initialize env\n\n```sh\npyenv install 3.8.13\npyenv global 3.8.13\ngit clone git@github.com:WASD3Rplay/wasd3r-sdk.git\ncd wasd3r-sdk\nPATH=$(pyenv root)/shims:$PATH; poetry env use python3.8; poetry install\n```\n\n### Start env\n\n```sh\ncd wasd3r-sdk\npoetry shell\n\npython --version\n# Python 3.8.13\n\nwhich python | xargs ls -al\n# /poetry/virtualenvs/wasd3r-sdk-xx-py3.8/bin/python -> /pyenv/versions/3.8.13/bin/python3.8\n```\n\n## Using `Miniconda`\n\n[Miniconda](https://docs.conda.io/projects/conda/en/stable/glossary.html#miniconda) could be install via [this link](https://docs.conda.io/en/latest/miniconda.html).\n\n### Initialize env\n\n```sh\nconda create -n wasd3r-sdk-py3.8 python=3.8\nconda activate wasd3r-sdk-py3.8\ngit clone git@github.com:WASD3Rplay/wasd3r-sdk.git\ncd wasd3r-sdk\npoetry env use python3.8; poetry install\n```\n\n### Start env\n\n```sh\ncd wasd3r-sdk\npoetry shell\n\npython --version\n# Python 3.8.x\n\nwhich python | xargs ls -al\n# /poetry/virtualenvs/wasd3r-sdk-xx-py3.8/bin/python -> /miniconda/envs/wasd3r-sdk-py3.8/bin/python3.8\n```\n',
    'author': 'Aaron',
    'author_email': 'aaron@wasd3r.xyz',
    'maintainer': 'Aaron',
    'maintainer_email': 'aaron@wasd3r.xyz',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
