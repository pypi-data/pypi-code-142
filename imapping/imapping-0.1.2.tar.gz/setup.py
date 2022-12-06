# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imapping']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'imapping',
    'version': '0.1.2',
    'description': 'iMapping was created with the intention of helping when mapping your future projects and facilitating their compilations',
    'long_description': '',
    'author': 'Noxty',
    'author_email': 'noxty@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
