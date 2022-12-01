# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amqp_client_python',
 'amqp_client_python.domain.models',
 'amqp_client_python.event',
 'amqp_client_python.exceptions',
 'amqp_client_python.rabbitmq',
 'amqp_client_python.utils']

package_data = \
{'': ['*']}

install_requires = \
['pika>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'amqp-client-python',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'NUTES UEPB',
    'author_email': 'dev.seniorsaudemovel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
