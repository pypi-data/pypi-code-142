# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nemglo', 'nemglo.backend', 'nemglo.components']

package_data = \
{'': ['*']}

install_requires = \
['mip>=1.13.0,<2.0.0',
 'nemed',
 'nemosis>=3.1.0,<4.0.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0']

setup_kwargs = {
    'name': 'nemglo',
    'version': '0.1.1',
    'description': 'Green-energy Load Optimisation tool for the NEM',
    'long_description': 'None',
    'author': 'dec-heim',
    'author_email': '92137442+dec-heim@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
