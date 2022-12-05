# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numaprom', 'numaprom.tests', 'numaprom.tests.udf', 'numaprom.udf']

package_data = \
{'': ['*'],
 'numaprom.tests': ['resources/data/*', 'resources/models/*'],
 'numaprom.udf': ['models/*']}

install_requires = \
['boto3>=1.25.2,<2.0.0',
 'cachetools>=5.0.0,<6.0.0',
 'confluent-kafka>=1.8.2,<2.0.0',
 'dataclasses-json>=0.5.6,<0.6.0',
 'numalogic[mlflow]==0.2.8',
 'pynumaflow>=0.2.6,<0.3.0',
 'redis>=4.3.1,<5.0.0']

setup_kwargs = {
    'name': 'numalogic-prometheus',
    'version': '0.0.2',
    'description': 'ML inference on numaflow using numalogic on Prometheus metrics',
    'long_description': 'None',
    'author': 'Numalogic developers',
    'author_email': 'None',
    'maintainer': 'Avik Basu',
    'maintainer_email': 'avikbasu93@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
