# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['library2notion']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'csv2notion>=0.3.7,<0.4.0',
 'epub-meta>=0.0.7,<0.0.8',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pypdf2>=2.11.2,<3.0.0']

entry_points = \
{'console_scripts': ['library2notion = library2notion.library2notion:main']}

setup_kwargs = {
    'name': 'library2notion',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'helguera',
    'author_email': 'javier@javierhelguera.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
