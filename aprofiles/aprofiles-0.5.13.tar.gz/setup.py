# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aprofiles',
 'aprofiles.cli',
 'aprofiles.cli.utils',
 'aprofiles.detection',
 'aprofiles.io',
 'aprofiles.plot',
 'aprofiles.retrieval',
 'aprofiles.simulation']

package_data = \
{'': ['*'], 'aprofiles': ['config/*'], 'aprofiles.cli': ['config/*']}

install_requires = \
['dask>=2022.10.2,<2023.0.0',
 'matplotlib>=3.5.0,<4.0.0',
 'miepython>=2.2.1,<3.0.0',
 'netCDF4>=1.5.8,<2.0.0',
 'numpy>=1.21.4,<2.0.0',
 'orjson>=3.6.7,<4.0.0',
 'scipy>=1.7.2,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'tqdm>=4.62.3,<5.0.0',
 'xarray>=2022.03.0,<2023.0.0']

extras_require = \
{'cli': ['typer[all]>=0.7.0,<0.8.0'],
 'docs': ['sphinx>=4.3.0,<5.0.0',
          'pydata-sphinx-theme>=0.9.0',
          'recommonmark>=0.7.1,<0.8.0']}

entry_points = \
{'console_scripts': ['aprocess = aprofiles.cli.aprocess:app']}

setup_kwargs = {
    'name': 'aprofiles',
    'version': '0.5.13',
    'description': 'Analysis of atmospheric profilers measurements',
    'long_description': 'None',
    'author': 'augustinm',
    'author_email': 'augustinm@met.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
