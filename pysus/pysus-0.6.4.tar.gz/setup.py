# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysus',
 'pysus.online_data',
 'pysus.preprocessing',
 'pysus.tests',
 'pysus.tests.test_data',
 'pysus.utilities']

package_data = \
{'': ['*'], 'pysus': ['Notebooks/*']}

install_requires = \
['cffi==1.15.1',
 'dbfread==2.0.7',
 'elasticsearch>=8.3.3,<9.0.0',
 'fastparquet>=0.8.1,<0.9.0',
 'geocoder>=1.38.1,<2.0.0',
 'jupyterlab>=3.4.5,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'numpy==1.23.2',
 'pandas==1.4.3',
 'pyarrow>=9.0.0,<10.0.0',
 'pycparser==2.21',
 'pyreaddbc==1.0.0',
 'python-dateutil==2.8.2',
 'pytz==2022.2.1',
 'six==1.16.0',
 'tqdm==4.64.0',
 'wget>=3.2,<4.0']

setup_kwargs = {
    'name': 'pysus',
    'version': '0.6.4',
    'description': "Tools for dealing with Brazil's Public health data",
    'long_description': 'None',
    'author': 'Flavio Codeco Coelho',
    'author_email': 'fccoelho@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
