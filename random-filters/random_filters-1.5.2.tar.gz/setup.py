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
    'version': '1.5.2',
    'description': 'A package for generating random filters',
    'long_description': "# Random filters: Python packaging for generate random filters to use in your project\n\n## Installation\n\n```bash\npip install random-filters\n```\n\n## Usage\n\n```python\nfrom random_filters import checkbox\nfrom random_filters import combobox\nfrom random_filters import date\nfrom random_filters import date_partition\nfrom random_filters import store\n\n# Checkbox\ncheckbox()\n## jantar\n\n# Date\ndate('2022-01-01', '2022-01-30')\n## '2022-01-29'\n\n```",
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
