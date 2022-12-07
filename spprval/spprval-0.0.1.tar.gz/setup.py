# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spprval', 'spprval.validation']

package_data = \
{'': ['*'], 'spprval': ['data/*', 'data_for_val/*', 'val_datasets/*']}

install_requires = \
['matplotlib==3.5.1',
 'numpy-indexed==0.3.5',
 'numpy==1.22.3',
 'pandas==1.4.1',
 'reportlab>=3.6.12,<4.0.0',
 'scipy==1.8.0',
 'seaborn==0.11.2']

setup_kwargs = {
    'name': 'spprval',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
