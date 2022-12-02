# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asian_mtl', 'asian_mtl.evaluation', 'asian_mtl.models']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.40,<2.0.0',
 'botocore>=1.24.43,<2.0.0',
 'dacite>=1.6.0,<2.0.0',
 'datasets>=2.1.0,<3.0.0',
 'gdown>=4.4.0,<5.0.0',
 'optimum>=1.1.0,<2.0.0',
 'psutil>=5.9.4,<6.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pyquery>=1.4.3,<2.0.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'torch>=1.11.0,<2.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'transformers>=4.18.0,<5.0.0']

setup_kwargs = {
    'name': 'asian-mtl',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Joseph Chen',
    'author_email': 'jchen42703@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
