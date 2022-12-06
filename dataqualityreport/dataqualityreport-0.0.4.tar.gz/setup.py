# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataqualityreport']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.1,<4.0.0',
 'joblib',
 'matplotlib>=3.5.0,<4.0.0',
 'numpy>=1.20,<2.0',
 'pandas>=1.1.5,<2.0.0',
 'pytest-cov>=3.0.0,<4.0.0',
 'pytest>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'dataqualityreport',
    'version': '0.0.4',
    'description': 'Data Quality Report - visual data profiling for python',
    'long_description': 'None',
    'author': 'Devjit Chakravarti',
    'author_email': 'devjit.chakravarti@doordash.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
