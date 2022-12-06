# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fast-json-pointer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fast-json-pointer',
    'version': '0.1.0',
    'description': 'Implements RFC 6901 JSON pointers, and json-schema draft relative pointer resolution.',
    'long_description': '# py-json-pointer\nImplements RFC 6901 JSON pointers, and json-schema draft relative pointer resolution.\n\n[![Documentation Status](https://readthedocs.org/projects/py-json-pointer/badge/?version=latest)](https://py-json-pointer.readthedocs.io/en/latest/?badge=latest)\n![PyPI - Downloads](https://img.shields.io/pypi/dw/fast-json-pointer)\n![PyPI - License](https://img.shields.io/pypi/l/fast-json-pointer)',
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
