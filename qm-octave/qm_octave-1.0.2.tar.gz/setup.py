# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['octave_sdk',
 'octave_sdk.connectivity',
 'octave_sdk.grpc.quantummachines',
 'octave_sdk.grpc.quantummachines.octave',
 'octave_sdk.grpc.quantummachines.octave.api',
 'octave_sdk.grpc.quantummachines.octave.api.v1']

package_data = \
{'': ['*']}

install_requires = \
['betterproto==2.0.0b5',
 'grpcio>=1.39.0,<2.0.0',
 'nest-asyncio>=1.5.4,<2.0.0',
 'numpy>=1.21.0',
 'protobuf>=3.17.3,<4.0.0']

extras_require = \
{':python_version >= "3.10" and python_version < "4.0"': ['grpclib>=0.4.3rc3,<0.5.0']}

setup_kwargs = {
    'name': 'qm-octave',
    'version': '1.0.2',
    'description': 'SDK to control an Octave with QUA',
    'long_description': "# QM Octave\nQuantum machine's Octave sdk\n",
    'author': 'QM',
    'author_email': 'info@quantum-machines.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
