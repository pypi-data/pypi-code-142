# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['es2loki', 'es2loki.aio', 'es2loki.commands', 'es2loki.pos', 'es2loki.proto']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4',
 'elasticsearch>=8.5.2,<9',
 'frozendict',
 'protobuf',
 'python-snappy',
 'tortoise-orm[asyncpg]',
 'yarl']

setup_kwargs = {
    'name': 'es2loki',
    'version': '0.1.3',
    'description': 'es2loki is a migration library that helps to transfer logs from Elasticsearch to Grafana Loki',
    'long_description': '# es2loki\n\n[![Build](https://github.com/ktsstudio/es2loki/actions/workflows/package.yml/badge.svg?branch=main)](https://github.com/ktsstudio/es2loki/actions)\n[![Build](https://github.com/ktsstudio/es2loki/actions/workflows/docker.yml/badge.svg?branch=main)](https://github.com/ktsstudio/es2loki/actions)\n[![PyPI](https://img.shields.io/pypi/v/es2loki.svg)](https://pypi.python.org/pypi/es2loki)\n[![Docker Image](https://img.shields.io/docker/v/ktshub/es2loki?label=docker&sort=semver)](https://hub.docker.com/repository/docker/ktshub/es2loki)\n\n`es2loki` is a migration library that helps to transfer logs from\nElasticsearch to Grafana Loki.\n\nTo use es2loki currently you need to define your own mapping of elasticsearch documents\nto labels for Grafana Loki.\n\n## Demo\nYou may find helpful a [demo](demo) folder which contains a fully-sufficient demo stand\nthat demonstrates transferring logs using `es2loki`.\n\n## Usage\nIn the simplest form you don\'t need to write any Python code at all,\nLoki will receive no meaningful labels, but nevertheless - let\'s see how it works.\n\n```bash\n$ pip install -U es2loki\n$ ELASTIC_HOSTS=http://localhost:9200 \\\n  ELASTIC_INDEX="filebeat-*" \\\n  LOKI_URL=http://localhost:3100 \\\n  python -m es2loki\n```\n\nIn order to override default `es2loki` behaviour you need to subclass\na `es2loki.BaseTransfer` class.\n\nTo declare how documents map to Loki labels you have to override a\n`extract_doc_labels` method (see [demo/example.py](demo/example.py)):\n\n```python\n\nfrom es2loki import BaseTransfer\n\n\nclass TransferLogs(BaseTransfer):\n    def extract_doc_labels(self, source: dict) -> Optional[MutableMapping[str, str]]:\n        return dict(\n            app=source.get("fields", {}).get("service_name"),\n            job="logs",\n            level=source.get("level"),\n            node_name=source.get("host", {}).get("name"),\n            logger_name=source.get("logger_name"),\n        )\n```\n\nYou can run this using the following code:\n```python\nimport sys\nfrom es2loki import run_transfer\n\nif __name__ == "__main__":\n    sys.exit(run_transfer(TransferLogs()))\n```\n\nYou can find more examples in the [demo](demo) folder.\n\n### Sorting\n\nBy default `es2loki` assumes that in the documents returned from Elasticsearch\nthere are fields `@timestamp` (you can change the name - see below) and `log.offset`.\nUsing these 2 fields we can be sure that we will not reread the same lines multiple times.\nBut if you have your fields that could guarantee such a behaviour - please\noverride a `make_es_sort` and `make_es_search_after` methods.\n\n* `make_es_sort` defines by which fields the sorting will happen.\n* `make_es_search_after` defines an initial "offset". It is needed to resume es2loki after a shutdown.\n\n## Configuration\n\n| name                    | default                            | description                                                        |\n|-------------------------|------------------------------------|--------------------------------------------------------------------|\n| ELASTIC_HOSTS           | http://localhost:9200              | Elasticsearch hosts. Separate multiple hosts using `,`             |\n| ELASTIC_USER            | ""                                 | Elasticsearch username                                             |\n| ELASTIC_PASSWORD        | ""                                 | Elasticsearch password                                             |\n| ELASTIC_INDEX           | ""                                 | Elasticsearch index pattern to search documents in                 |\n| ELASTIC_BATCH_SIZE      | 3000                               | How much documents to extract from ES in one batch                 |\n| ELASTIC_TIMEOUT         | 120                                | Elasticsearch `search` query timeout                               |\n| ELASTIC_MAX_DATE        |                                    | Upper date limit (format is the same as @timestamp field)          |\n| ELASTIC_TIMESTAMP_FIELD | @timestamp                         | Name of timesteamp field in Elasticsearch                          |\n| LOKI_URL                | http://localhost:3100              | Loki instance URL                                                  |\n| LOKI_USERNAME           | ""                                 | Loki username                                                      |\n| LOKI_PASSWORD           | ""                                 | Loki password                                                      |\n| LOKI_TENANT_ID          | ""                                 | Loki Tenant ID (Org ID)                                            |\n| LOKI_BATCH_SIZE         | 1048576                            | Maximum batch size (in bytes)                                      |\n| LOKI_POOL_LOAD_FACTOR   | 10                                 | Maximum number of push non-waiting requests                        |\n| LOKI_PUSH_MODE          | pb                                 | `pb` - protobuf + snappy, `gzip` - json + gzip, `json` - just json |\n| LOKI_WAIT_TIMEOUT       | 0                                  | How much time (in seconds) to wait after a Loki push request       |\n| PERSIST_MODE            | db                                 | Configures es2loki persistence (`db` is recommended).              |\n| PERSIST_START_OVER      |                                    | Clean up persisted data and start over                             |\n| PERSIST_FILE_DIR        | /var/es2loki                       | `file` persistence location                                        |\n| PERSIST_DB_URL          | postgres://127.0.0.1:5432/postgres | Database URL for `db` persistence                                  |\n\n\n\n',
    'author': 'igorcoding',
    'author_email': 'igorcoding@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ktsstudio/es2loki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
