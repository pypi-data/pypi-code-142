# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['semestr1580']
setup_kwargs = {
    'name': 'semestr1580',
    'version': '0.1.0',
    'description': 'Sdo docks',
    'long_description': 'None',
    'author': 'pavelglazunov',
    'author_email': 'p6282813@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
