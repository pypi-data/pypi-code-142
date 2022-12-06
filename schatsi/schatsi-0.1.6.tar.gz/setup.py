# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['schatsi',
 'schatsi.jobs',
 'schatsi.models',
 'schatsi.processor',
 'schatsi.reader']

package_data = \
{'': ['*']}

install_requires = \
['PyMuPDF>=1.20.2,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'dask[diagnostics,distributed]>=2022.10.0,<2023.0.0',
 'loguru>=0.6.0,<0.7.0',
 'nltk>=3.7,<4.0',
 'pandas>=1.5.1,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['schatsi = schatsi.cli:cli']}

setup_kwargs = {
    'name': 'schatsi',
    'version': '0.1.6',
    'description': '',
    'long_description': "# (f)SCHA.T.S.I\n\n(f)SCHA.T.S.I - An abbreviation for '**f**aster **SCH**eduling *A*lgorithm for **T**ext **S**each **I**ntelligence'.\n\n\n## Getting Started\nhttps://python-poetry.org/\npip install poetry  \npoetry install  \n",
    'author': 'robnoflop',
    'author_email': 'info@robertkasseck.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/robnoflop/Schatsi',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.8,<4.0.0',
}


setup(**setup_kwargs)
