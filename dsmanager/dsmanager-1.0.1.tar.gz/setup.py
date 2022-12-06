# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dsmanager',
 'dsmanager.controller',
 'dsmanager.datamanager',
 'dsmanager.model',
 'dsmanager.view']

package_data = \
{'': ['*']}

install_requires = \
['SharePlum>=0.5.1,<0.6.0',
 'azure-common>=1.1.28,<2.0.0',
 'azure-storage-blob>=12.14.0,<13.0.0',
 'azure-storage-common>=2.1.0,<3.0.0',
 'dash>=2.6.2,<3.0.0',
 'explainerdashboard>=0.4.0,<0.5.0',
 'ipython>=8.5.0,<9.0.0',
 'numexpr>=2.8.3,<3.0.0',
 'numpy>=1.23.3,<2.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'optuna>=3.0.3,<4.0.0',
 'pandas>=1.5.0,<2.0.0',
 'paramiko>=2.12.0,<3.0.0',
 'pickle-mixin>=1.0.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'shap>=0.41.0,<0.42.0',
 'snowflake-connector-python>=2.8.0,<3.0.0',
 'snowflake-sqlalchemy>=1.4.2,<2.0.0',
 'sqlalchemy>=1.4.41,<2.0.0',
 'sweetviz>=2.1.4,<3.0.0']

setup_kwargs = {
    'name': 'dsmanager',
    'version': '1.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'Rayane AMROUCHE',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
