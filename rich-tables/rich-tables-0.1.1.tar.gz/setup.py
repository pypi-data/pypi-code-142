# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rich_tables']

package_data = \
{'': ['*']}

install_requires = \
['multimethod', 'rgbxy>=0.5', 'rich>=12.3.0']

entry_points = \
{'console_scripts': ['table = rich_tables.table:main']}

setup_kwargs = {
    'name': 'rich-tables',
    'version': '0.1.1',
    'description': 'Ready-made rich tables for various purposes',
    'long_description': None,
    'author': 'Šarūnas Nejus',
    'author_email': 'snejus@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.3,<4',
}


setup(**setup_kwargs)
