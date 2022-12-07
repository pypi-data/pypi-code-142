# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fast_json_pointer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fast-json-pointer',
    'version': '0.2.0',
    'description': 'Implements RFC 6901 JSON pointers, and json-schema draft relative pointer resolution.',
    'long_description': '# py-json-pointer\nImplements RFC 6901 JSON pointers, and json-schema draft relative pointer resolution.\n\n<table>\n<tr>\n<td>Package</td>\n<td>\n\n![PyPI](https://img.shields.io/pypi/v/fast-json-pointer)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fast-json-pointer)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/fast-json-pointer)\n![PyPI - Implementation](https://img.shields.io/pypi/implementation/fast-json-pointer)\n![PyPI - Downloads](https://img.shields.io/pypi/dw/fast-json-pointer)\n![PyPI - License](https://img.shields.io/pypi/l/fast-json-pointer)\n</td>\n</tr>\n<tr>\n<td>\nBuild\n</td>\n<td>\n\n![GitHub commit checks state](https://img.shields.io/github/checks-status/slowAPI/fast-json-pointer/main?logo=github)\n[![Documentation Status](https://readthedocs.org/projects/fast-json-pointer/badge/?version=latest)](https://fast-json-pointer.readthedocs.io/en/latest/?badge=latest)\n[![Coverage Status](https://coveralls.io/repos/github/SlowAPI/fast-json-pointer/badge.svg?branch=main)](https://coveralls.io/github/SlowAPI/fast-json-pointer?branch=main)\n![Lines of code](https://img.shields.io/tokei/lines/github/slowAPI/fast-json-pointer)\n</td>\n</tr>\n<tr>\n<td>\nGit\n</td>\n<td>\n\n![GitHub last commit](https://img.shields.io/github/last-commit/slowAPI/fast-json-pointer)\n![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/slowAPI/fast-json-pointer/latest)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/m/slowAPI/fast-json-pointer)\n![GitHub issues](https://img.shields.io/github/issues/slowAPI/fast-json-pointer)\n![GitHub pull requests](https://img.shields.io/github/issues-pr/slowAPI/fast-json-pointer)\n</td>\n</tr>\n</table>\n',
    'author': 'Tristan Sweeney',
    'author_email': 'sweeneytri@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SlowAPI/py-json-pointer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
