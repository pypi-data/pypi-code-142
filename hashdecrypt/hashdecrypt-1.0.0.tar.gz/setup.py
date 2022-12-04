# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['hashdecrypt']
install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'hashdecrypt',
    'version': '1.0.0',
    'description': 'Decrypt Metamask, Brawe, Ronin, BinanceChain vault data via Python',
    'long_description': None,
    'author': 'M16',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
