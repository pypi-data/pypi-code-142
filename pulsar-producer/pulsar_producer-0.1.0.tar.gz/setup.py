# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pulsar_producer']

package_data = \
{'': ['*']}

install_requires = \
['pulsar-client>=2.10.2,<3.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['pulsar-producer = pulsar_producer.cli:start']}

setup_kwargs = {
    'name': 'pulsar-producer',
    'version': '0.1.0',
    'description': 'CLI that help developers to publish messages into any pulsar topic in order to test features (usually, consumers) that relies on a pulsar consumer',
    'long_description': '# Pulsar Producer\n\nCLI that allows to send a message into a Apache Pulsar topic\n\n#\n\nUsually, implementing an Apache Pulsar Consumers, you will need to test it before release. Then, it\'s quite painful that you need to write or change some code in order to test it. Having that said, I have implemented this CLI that can help you with that.\n\nNow, you can have a file with the message you want to send into a specific Apache Pulsar Topic and simply test your Apache Pulsar Consumer easily.\n\n# How to use it\n\nFirst, you should install the CLI on your machine\n\n`pip install pulsar-producer` or `pip install --user pulsar-producer` if you want make it available only for your user.\n\n> **_NOTE:_**  This package still *not* publish on pypi, only on [testing environment](https://test.pypi.org/project/pulsar-producer/0.1.0/#description)\n\n> **_NOTE:_** pip install -i https://test.pypi.org/simple/ pulsar-producer==0.1.0\n\nThen, you need to have an file with your Apache Pulsar server address. This file SHOULD follow a JSON format.\n\nExample:\n\n[_my-apache-pulsar-configuration.json_](./examples/pulsar-connection.json)\n\n```json\n{\n        "host": "localhost",\n        "port": "6650",\n        "topic": "my-topic-name"\n}\n\n```\n\nThen, you need to have another file with contains the message you want to publish in your Apache Pulsar topic in order to test your Apache Pulsar Consumer.\nThis file can contains ANYTHING you want. In this example, let\'s say you want to publish a JSON structure message.\n\n[_my-message-file-example.json_](./examples/message-file)\n\n```json\n{\n    "KEY": "THIS IS MY MESSAGE WHICH COULD BE ONLY PURE TEXT (NOT JSON)"\n}\n\n```\n\nNow, you just need to run:\n\n`pulsar-producer --pulsar-connection-file ./path-of-your-my-apache-pulsar-configuration-example-json --message-file ./path-or-your-message-file`\n\n# License\nMIT\n',
    'author': 'Luiz Filipe',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/vandaimer/pulsar-producer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
