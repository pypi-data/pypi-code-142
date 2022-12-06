# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pancho',
 'pancho.bootstraping',
 'pancho.definitions',
 'pancho.definitions.contracts',
 'pancho.definitions.exceptions',
 'pancho.identity',
 'pancho.interaction',
 'pancho.markup',
 'pancho.obtaining',
 'pancho.operations',
 'pancho.processing']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'tacitus>=0.1.8,<0.2.0',
 'zorge>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'pancho',
    'version': '0.1.7',
    'description': 'Commands processor',
    'long_description': 'None',
    'author': 'smairon',
    'author_email': 'man@smairon.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
