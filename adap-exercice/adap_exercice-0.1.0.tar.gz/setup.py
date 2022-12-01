# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adap_exercice']

package_data = \
{'': ['*']}

install_requires = \
['sympy>=1.11.1,<2.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['adap-exercice = adap_exercice.main:app']}

setup_kwargs = {
    'name': 'adap-exercice',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Mathieu',
    'author_email': 'mathieuveron@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
