# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['physical_units']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'physical-units',
    'version': '0.0.1',
    'description': 'Представление физ. единиц как объектов в python',
    'long_description': '',
    'author': 'konstantin-dudersky',
    'author_email': 'konstantin.dudersky@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Konstantin-Dudersky/python-physical-units',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
