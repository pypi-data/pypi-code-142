# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchsilk', 'torchsilk.distributions', 'torchsilk.init', 'torchsilk.modules']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.1.0,<23.0.0',
 'lovely-tensors>=0.1.8,<0.2.0',
 'numpy>=1.23.5,<2.0.0',
 'optree>=0.5.0,<0.6.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'scipy>=1.9.3,<2.0.0',
 'torch>=1.13.0,<2.0.0',
 'torchopt>=0.5.0.post4,<0.6.0',
 'typer[all]>=0.7.0,<0.8.0']

extras_require = \
{'all': ['autoflake>=1.4,<2.0',
         'black>=22.3.0,<23.0.0',
         'isort>=5.10.1,<6.0.0',
         'mypy>=0.961,<0.962',
         'pytest>=7.2.0,<8.0.0',
         'pytest-vscodedebug>=0.1.0,<0.2.0',
         'pyupgrade>=2.37.3,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'xdoctest[all]>=1.1.0,<2.0.0'],
 'test': ['autoflake>=1.4,<2.0',
          'black>=22.3.0,<23.0.0',
          'isort>=5.10.1,<6.0.0',
          'mypy>=0.961,<0.962',
          'pytest>=7.2.0,<8.0.0',
          'pytest-vscodedebug>=0.1.0,<0.2.0',
          'pyupgrade>=2.37.3,<3.0.0',
          'toml>=0.10.2,<0.11.0',
          'xdoctest[all]>=1.1.0,<2.0.0']}

setup_kwargs = {
    'name': 'torchsilk',
    'version': '0.7.0',
    'description': 'TorchSilk is a neural network library for working with functorch.',
    'long_description': '# TorchSilk\n\nTorchSilk is a neural network library for working with functorch.\n',
    'author': 'Aditya Gudimella',
    'author_email': 'aditya.gudimella@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
