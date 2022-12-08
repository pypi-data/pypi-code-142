# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dep_mongo']

package_data = \
{'': ['*']}

modules = \
['pyproject']
install_requires = \
['beanie>=1.11.9,<2.0.0', 'dep-spec>=2.3.29,<3.0.0', 'poetry==1.1.15']

setup_kwargs = {
    'name': 'dep-module-mongo',
    'version': '2.13.29',
    'description': '',
    'long_description': None,
    'author': 'everhide',
    'author_email': 'i.tolkachnikov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<=3.11',
}


setup(**setup_kwargs)
