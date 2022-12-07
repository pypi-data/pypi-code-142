# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiges',
 'aiges.aiges_inner',
 'aiges.backup',
 'aiges.client',
 'aiges.client.utils',
 'aiges.cmd',
 'aiges.core',
 'aiges.examples.once.mmocr',
 'aiges.examples.stream.mmocr',
 'aiges.examples.stream.mock',
 'aiges.schema',
 'aiges.schema.utils',
 'aiges.serve',
 'aiges.test_data',
 'aiges.utils']

package_data = \
{'': ['*'], 'aiges': ['tpls/*']}

install_requires = \
['flask_restx>=1.0.0',
 'grpcio-health-checking>=1.50.0',
 'grpcio-tools>=1.50.0',
 'grpcio>=1.50.0',
 'jinja2>=2.0',
 'jsonref>=1.0.0',
 'plumbum>=1.7.0',
 'protobuf>=4.21',
 'pydantic>=1.8']

setup_kwargs = {
    'name': 'aiges',
    'version': '0.6.4',
    'description': "A module for test aiges's python wrapper.py",
    'long_description': None,
    'author': 'maybaby',
    'author_email': 'ybyang7@iflytek.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
