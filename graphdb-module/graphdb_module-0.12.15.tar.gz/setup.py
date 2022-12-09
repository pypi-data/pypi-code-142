# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphdb',
 'graphdb.connection',
 'graphdb.interface',
 'graphdb.schema',
 'graphdb.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'gremlinpython>=3.5.2,<4.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'graphdb-module',
    'version': '0.12.15',
    'description': '',
    'long_description': '# Wrapper for AWS Neptune Query\n\n## Example\n\nSee [this repository](https://mnc-repo.mncdigital.com/ai-team/vision_plus/graph_db_module_example) for example\n\n## Install [module](https://pypi.org/project/graphdb-module/0.1.0/#description)\n\n```shell\n    pip install graphdb-module\n```\n\n## Run unit test\n\n```shell\n    python -m unittest discover -v\n```',
    'author': 'AIML Team',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
