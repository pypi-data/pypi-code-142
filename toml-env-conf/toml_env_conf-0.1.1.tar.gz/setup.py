# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toml_env_conf']

package_data = \
{'': ['*']}

install_requires = \
['mergedeep>=1.3.4,<2.0.0', 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'toml-env-conf',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'sa-',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sa-/toml_env_conf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
