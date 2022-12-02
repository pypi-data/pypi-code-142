# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meshlab_pickedpoints']

package_data = \
{'': ['*']}

extras_require = \
{'cli': ['click>=8.0.3,<9.0.0']}

setup_kwargs = {
    'name': 'meshlab-pickedpoints',
    'version': '4.0.0',
    'description': 'Read and write MeshLab picked point (.pp) files',
    'long_description': 'None',
    'author': 'Paul Melnikow',
    'author_email': 'github@paulmelnikow.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lace/meshlab-pickedpoints',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<4',
}


setup(**setup_kwargs)
