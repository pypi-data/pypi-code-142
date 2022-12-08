# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drive_screen']

package_data = \
{'': ['*'], 'drive_screen': ['static/*']}

install_requires = \
['Flask>=2.0.1,<3.0.0',
 'Pillow>=9.2.0,<10.0.0',
 'PyMySQL>=1.0.2,<2.0.0',
 'dash-core-components>=2.0.0,<3.0.0',
 'dash-html-components>=2.0.0,<3.0.0',
 'dash>=2.0.0,<3.0.0',
 'dash_bootstrap_components>=1.2.1,<2.0.0',
 'pandas>=1.1.5,<2.0.0',
 'plotly>=5.2.1,<6.0.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'drive-screen',
    'version': '0.2.1',
    'description': 'add install source',
    'long_description': '# This is pypi code for drive-panel\n',
    'author': 'shengqin ding',
    'author_email': 'dshengq@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
