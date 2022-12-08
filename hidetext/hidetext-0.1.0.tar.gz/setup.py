# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hidetext',
 'hidetext.filters',
 'hidetext.placeholders',
 'hidetext.resources',
 'hidetext.resources.ca',
 'hidetext.resources.en']

package_data = \
{'': ['*']}

install_requires = \
['spacy[spacy]>=3.4.3,<4.0.0']

setup_kwargs = {
    'name': 'hidetext',
    'version': '0.1.0',
    'description': 'Hides non-desired text',
    'long_description': None,
    'author': 'Jaume Ferrarons',
    'author_email': 'jaume.ferrarons@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
