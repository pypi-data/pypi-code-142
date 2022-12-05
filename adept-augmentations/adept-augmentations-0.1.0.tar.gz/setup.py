# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adept_augmentations',
 'adept_augmentations.analyzers',
 'adept_augmentations.augmentors']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.5,<3.0', 'pydantic>=1.8,<2.0', 'spacy>=3,<4']

setup_kwargs = {
    'name': 'adept-augmentations',
    'version': '0.1.0',
    'description': 'A Python library aimed at dissecting and augmenting NLP training data.',
    'long_description': '# adept-augmentations\nA Python library aimed at dissecting and augmenting NLP training data.\n',
    'author': 'david',
    'author_email': 'david.m.berenstein@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/davidberenstein1957/adept-augmentations',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
