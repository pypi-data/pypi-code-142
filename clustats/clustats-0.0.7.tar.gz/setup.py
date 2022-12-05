# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clustats']

package_data = \
{'': ['*']}

install_requires = \
['belinda==0.0.4a8',
 'pandas>=1,<2',
 'polars>=0.15.2,<0.16.0',
 'structlog>=22.3.0,<23.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['clustats = clustats.runstats:entry_point',
                     'clustats2latex = clustats.format_latex:entry_point']}

setup_kwargs = {
    'name': 'clustats',
    'version': '0.0.7',
    'description': '',
    'long_description': '',
    'author': 'runeblaze',
    'author_email': 'runeblaze@excite.co.jp',
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
