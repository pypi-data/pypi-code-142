# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['high_order_implicit_representation']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.1,<10.0.0',
 'high-order-layers-torch>=1.1.18,<2.0.0',
 'hydra-core>=1.2.0,<2.0.0',
 'hydra-nevergrad-sweeper==1.3.0.dev0',
 'matplotlib>=3.5.2,<4.0.0',
 'omegaconf>=2.2.2,<3.0.0',
 'pytorch-lightning>=1.8.3,<2.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'torch-optimizer>=0.3.0,<0.4.0',
 'torch>=1.13.0,<2.0.0',
 'torchsummary>=1.5.1,<2.0.0',
 'torchvision>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'high-order-implicit-representation',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'John Loverich',
    'author_email': 'john.loverich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
