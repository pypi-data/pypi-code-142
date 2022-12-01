# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repoup',
 'repoup.entrypoint',
 'repoup.lib',
 'repoup.repository',
 'repoup.storage']

package_data = \
{'': ['*']}

extras_require = \
{'aws': ['aioboto3'],
 'deb': ['python-debian'],
 'rpm': ['createrepo_c'],
 'speedups': ['uvloop']}

setup_kwargs = {
    'name': 'repoup',
    'version': '1.0.0b26',
    'description': 'Serverless package repository updater',
    'long_description': '[![tests](https://github.com/JGoutin/repoup/actions/workflows/tests.yml/badge.svg)](https://github.com/JGoutin/repoup/actions/workflows/tests.yml)\n[![codecov](https://codecov.io/gh/JGoutin/repoup/branch/main/graph/badge.svg?token=29y1Q2iVjo)](https://codecov.io/gh/JGoutin/repoup)\n[![PyPI](https://img.shields.io/pypi/v/repoup.svg)](https://pypi.org/project/repoup)\n\nRepoup is a utility to manage packages repositories stored on the cloud from serverless\nfunctions. For instance, it can manage an RPM repository stored on S3 from an AWS lambda\nfunction.\n\nFeatures:\n\n * Repository initialization.\n * Packages addition and deletion.\n * Packages signature.\n * Multiple repository management with a single instance.\n * Autodetection of the repository to update based on the package name information \n   (Architecture, OS version, package format).\n\nSupported repositories:\n\n * RPM: `.rpm` packages repositories used with DNF/YUM Linux package managers.\n * DEB: `.deb` packages repositories used with APT Linux package managers.\n\nSupported cloud:\n\n * AWS: AWS S3 (or compatible) as storage with optional Cloudfront CDN. \n   AWS Lambda as repository updater.\n\n# Installation\n\nThe package is available on PyPI and can be installed using Pip:\n\n```bash\npip install repoup\n```\n\nBy default, only the minimum dependencies are installed. It is possible to install\nmore dependencies using the following extras:\n\n* `speedups`: Optional libraries to improve performance.\n* `rpm`: RPM repositories support.\n* `deb`: DEB repositories support.\n* `aws`: AWS cloud provider support.\n\nFor instance:\n\n```bash\npip install repoup[rpm,speedups]\n```\n\nFor DEB repositories, the `python-apt` package is also recommended to improve \nperformance. The version of this package available on PyPI is really outdated, so it is\nrecommended to use the version packaged with your OS. Ensure the Python interpreter used\nis the system interpreter in this case or that it can import this package.\n\n## Packages and metadata signature extra requirements:\n\nThe `gnupg` (Version 2.1 or more) command is required.\n\nGPG keys with passwords also requires that the `gpg-agent` is not already started or is \nstarted with the `--allow-preset-passphrase` parameter.\n\n### RPM packages\n\nTo sign RPM package, the `rpm-sign` package is required.\n\n#### Signature verification\n\nIf the repository is called with `gpg_verify=True` to activate signature verification\nafter signing, the `rpm` command require to be run as Root. This is required to add \nand remove the public key to the keyring.\n\nIt is possible to set the `RPM_GPG_REQUIRE_SUDO=1` environment variable to \nautomatically use `sudo`. This requires that `sudo` does not require password.\n\n### DEB Packages.\n\nTo sign DEB package, the `debsigs` package is required.\n',
    'author': 'J.Goutin',
    'author_email': 'jgoutin@accelize.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JGoutin/repoup',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
