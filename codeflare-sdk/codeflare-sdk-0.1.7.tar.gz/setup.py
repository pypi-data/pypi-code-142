# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['codeflare_sdk', 'codeflare_sdk.cluster', 'codeflare_sdk.utils']

package_data = \
{'': ['*'], 'codeflare_sdk': ['templates/*']}

install_requires = \
['openshift-client==1.0.18', 'rich>=12.5,<13.0']

setup_kwargs = {
    'name': 'codeflare-sdk',
    'version': '0.1.7',
    'description': 'Python SDK for codeflare client',
    'long_description': "# Codeflare-SDK\n\nAn intuitive, easy-to-use python interface for batch resource requesting, access, job submission, and observation. Simplifying the developer's life while enabling access to high-performance compute resources, either in the cloud or on-prem.\n\nTutorial and basics walkthrough coming soon!\n\nFull documentation can be found [here](https://project-codeflare.github.io/codeflare-sdk/)\n\n## Installation\n\nCan be installed via `pip`: `pip install codeflare-sdk`\n\n## Development\n\nFor testing, make sure to have installed:\n - `pytest`\n - The remaining dependencies located in `requirements.txt`\n\nNOTE: Self-contained unit/functional tests coming soon, will live in `tests` folder\n\nFor formatting:\n - Currently using black v22.3.0 for format checking\n - To install, run `pip install black==22.3.0`\n - To check file formatting, in top-level dir run `black --check .`\n   - To auto-reformat all files, remove the `--check` flag\n   - To reformat an individual file, run `black <filename>`\n\nTo build the python package:\n - If poetry is not installed: `pip install poetry`\n - `poetry build`\n",
    'author': 'Atin Sood',
    'author_email': 'asood@us.ibm.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/project-codeflare/codeflare-sdk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
