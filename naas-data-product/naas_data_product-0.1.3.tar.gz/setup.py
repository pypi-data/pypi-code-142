# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['naas_data_product', 'naas_data_product..ipynb_checkpoints']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'naas-data-product',
    'version': '0.1.3',
    'description': '',
    'long_description': '',
    'author': 'Maxime Jublou',
    'author_email': 'maxime@jublou.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
