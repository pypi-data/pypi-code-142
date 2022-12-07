# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyjsondatabase']
setup_kwargs = {
    'name': 'pyjsondatabase',
    'version': '0.0.1',
    'description': 'Simple dictionary-based database',
    'long_description': '',
    'author': 'Xenely',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
