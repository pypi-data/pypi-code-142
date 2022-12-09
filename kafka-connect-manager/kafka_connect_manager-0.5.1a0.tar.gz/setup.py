# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kafka_connect_manager']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['kcm = kafka_connect_manager.cli:app']}

setup_kwargs = {
    'name': 'kafka-connect-manager',
    'version': '0.5.1a0',
    'description': 'A tool to manage Apache Kafka Connect connectors and tasks using asyncio',
    'long_description': '<h1 align="center">Kafka Connect Manager</h1>\n<p align="center">A tool to manage Apache Kafka Connect connectors and tasks</p>\n\n**Usage**:\n\n```console\n$ kcm [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--host TEXT`: Connect worker host  [env var: CONNECT_HOST; default: http://localhost:8083]\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `add`: Register new connector Supporting environment...\n* `list`: List all connectors\n* `status`: Get status connector\n* `update`: Update connector configuration\n* `watch`: Actively monitor your connectors health\n\n## `kcm add`\n\nRegister new connector\n\nSupporting environment variable expansion in JSON file.\n\nA connector requires a name and configuration, we take both of them separately.\n\nFor example:\n\n```json\n{\n    "name": "MySinkConnector",\n    "config": {\n        "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",\n        "connection.uri": "${MONGODB_URL}"\n    }\n}\n```\n\n**Usage**:\n\n```console\n$ kcm add [OPTIONS]\n```\n\n**Options**:\n\n* `-f, --file FILE`: Config JSON file path  [required]\n* `--help`: Show this message and exit.\n\n## `kcm list`\n\nList all connectors\n\n**Usage**:\n\n```console\n$ kcm list [OPTIONS]\n```\n\n**Options**:\n\n* `--type [all|sink|source]`: Type of connectors to list  [default: all]\n* `--help`: Show this message and exit.\n\n## `kcm status`\n\nGet status connector\n\n**Usage**:\n\n```console\n$ kcm status [OPTIONS]\n```\n\n**Options**:\n\n* `--connector TEXT`: Name of connector  [required]\n* `--help`: Show this message and exit.\n\n## `kcm update`\n\nUpdate connector configuration\n\n**Usage**:\n\n```console\n$ kcm update [OPTIONS] CONNECTOR\n```\n\n**Arguments**:\n\n* `CONNECTOR`: Connector name  [required]\n\n**Options**:\n\n* `-f, --file FILE`: Config JSON file path  [required]\n* `--help`: Show this message and exit.\n\n## `kcm watch`\n\nActively monitor your connectors health\n\n![Dashboard Screenshot](https://res.cloudinary.com/ajamalkhan/image/upload/f_auto,q_auto/v1662560403/projects/kafka-connect-manager-watch-dashboard.png)\n\n**Usage**:\n\n```console\n$ kcm watch [OPTIONS] [CONNECTORS]...\n```\n\n**Arguments**:\n\n* `[CONNECTORS]...`: Connectors to monitor\n\n**Options**:\n\n* `--refresh-interval INTEGER`: Refresh interval  [default: 5]\n* `--help`: Show this message and exit.\n',
    'author': 'Ajamal Khan',
    'author_email': '13559558+khan-ajamal@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/khan-ajamal/kafka-connect-manager',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
