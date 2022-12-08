# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['isolate_proto']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.49', 'isolate[grpc]>=0.7,<0.8', 'protobuf']

setup_kwargs = {
    'name': 'isolate-proto',
    'version': '0.0.2',
    'description': '(internal) gRPC definitions for Isolate Cloud',
    'long_description': '# gRPC definitions\n\nFor regenerating definitions\n\n```\n$ python tools/regen_grpc.py src/isolate_proto/controller.proto <isolate version>\n```\n',
    'author': 'Features & Labels',
    'author_email': 'hello@fal.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
