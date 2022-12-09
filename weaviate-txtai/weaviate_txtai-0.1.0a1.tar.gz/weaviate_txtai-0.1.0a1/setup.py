# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weaviate_txtai']

package_data = \
{'': ['*']}

install_requires = \
['txtai[api]>=5.1.0,<6.0.0', 'weaviate-client>=3.9.0,<4.0.0']

setup_kwargs = {
    'name': 'weaviate-txtai',
    'version': '0.1.0a1',
    'description': 'An integration of the weaviate vector search engine with txtai',
    'long_description': '',
    'author': 'hsm207',
    'author_email': 'hsm207@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
