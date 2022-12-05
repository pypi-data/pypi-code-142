# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['random_filters',
 'random_filters.checkbox',
 'random_filters.combobox',
 'random_filters.date',
 'random_filters.date_partition',
 'random_filters.store']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'random-filters',
    'version': '1.5.1',
    'description': 'A package for generating random filters',
    'long_description': '',
    'author': 'Renan',
    'author_email': 'renancavalcantercb@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
