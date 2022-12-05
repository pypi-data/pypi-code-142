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
    'version': '1.5.4',
    'description': 'A package for generating random filters',
    'long_description': '# Random filters: Python packaging for generate random filters to use in your project\n\n## Installation\n\n```bash\npip install random-filters\n```\n\n## Usage\n\n```python\nimport random_filters as rf\n\n# checkbox\nrf.checkbox()\n\n# combobox\nrf.combobox_hierarchy({"Estado": ["SP", "SP", "SP", "SC", "SC", "SC"],\n                       "Cidade": ["São Paulo", "Itatiba", "Campinas", "Chapecó", "Xaxim", "Xanxerê"]})\n\n# date\nrf.date(\'2019-01-01\', \'2019-12-31\')\n\n# date_partition\nrf.date_partition(2)\n\n# store\nrf.store(2)\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n',
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
