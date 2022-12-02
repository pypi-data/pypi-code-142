# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycomfoconnect']

package_data = \
{'': ['*']}

install_requires = \
['protobuf>=3.20.3']

setup_kwargs = {
    'name': 'pycomfoconnect',
    'version': '0.5',
    'description': 'Python interface for the Zehnder ComfoConnect LAN C bridge.',
    'long_description': 'pycomfoconnect\n==============\n\nA Python library to interface with the Zehnder ComfoConnect LAN C bridge that is connected to the Zehnder ComfoAir Q350/450/600 ventilation units.\n\nInstallation\n------------\n\n::\n\n    pip3 install pycomfoconnect\n',
    'author': 'Michaël Arnauts',
    'author_email': 'michael.arnauts@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/michaelarnauts/comfoconnect',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
