# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['potyk_doc', 'potyk_doc.translation']

package_data = \
{'': ['*']}

install_requires = \
['potyk-lib>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'potyk-doc',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'potykion',
    'author_email': 'potykion@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
