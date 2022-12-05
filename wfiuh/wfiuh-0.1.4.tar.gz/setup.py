# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wfiuh', 'wfiuh.curve_fitting', 'wfiuh.curve_fitting.pdf']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0',
 'pandas>=1.5.1,<2.0.0',
 'rich>=12.6.0,<13.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'wfiuh',
    'version': '0.1.4',
    'description': 'Curve fitting width function IUH (WFIUH) in Hydrology',
    'long_description': '# WFIUH\n\nCurve fitting width function IUH (WFIUH) in Hydrology\n',
    'author': 'Qin Li',
    'author_email': 'liblaf@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://liblaf.github.io/WFIUH/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
