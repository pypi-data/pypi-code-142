# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['matatupath']
install_requires = \
['openrouteservice>=2.3.3,<3.0.0', 'polyline>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'matatupath',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'shadmeoli',
    'author_email': 'shadcodes@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9.5,<4.0.0',
}


setup(**setup_kwargs)
