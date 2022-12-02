# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anonlinkclient']

package_data = \
{'': ['*'], 'anonlinkclient': ['data/*']}

install_requires = \
['bashplotlib>=0.6.5,<0.7.0',
 'blocklib>=0.1.8,<0.2.0',
 'click>=7.1.2,<8.0.0',
 'clkhash>=0.16.1,<0.17.0',
 'ijson>=3.1.4,<4.0.0',
 'jsonschema>=3.2,<5.0',
 'minio>=7.0.3,<8.0.0',
 'requests>=2.25.1,<3.0.0',
 'retrying>=1.3.3,<2.0.0']

entry_points = \
{'console_scripts': ['anonlink = anonlinkclient.cli:cli']}

setup_kwargs = {
    'name': 'anonlink-client',
    'version': '0.1.6',
    'description': 'Client side tool for clkhash and blocklib',
    'long_description': "[![codecov](https://codecov.io/gh/data61/anonlink-client/branch/main/graph/badge.svg)](https://codecov.io/gh/data61/anonlink-client)\n[![Documentation Status](https://readthedocs.org/projects/anonlink-client/badge/?version=latest)](http://anonlink-client.readthedocs.io/en/latest/?badge=latest)\n[![Testing](https://github.com/data61/anonlink-client/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/data61/anonlink-client/actions/workflows/ci.yml)\n[![Requirements Status](https://requires.io/github/data61/anonlink-client/requirements.svg?branch=main)](https://requires.io/github/data61/anonlink-client/requirements/?branch=main)\n[![Downloads](https://pepy.tech/badge/anonlink-client)](https://pepy.tech/project/anonlink-client)\n# Anonlink Client\n\n\nClient-facing API to interact with anonlink system including command line tools and Rest API communication.\nAnonlink system needs the following three components to work together:\n\n* [clkhash](https://github.com/data61/clkhash)\n* [blocklib](https://github.com/data61/blocklib)\n\nThis package provides an easy to use API to interact with the above packages to complete a record linkage job.\n\nThe way to interact with anonlink system is via Command Line Tool `anonlink`. You can hash data containing PI (Personal\n Identifying Information) locally using `anonlink hash` and generate candidate blocks locally to scale up record linkage \n using `anonlink block`.\n\n### Installation\n\nInstall with pip/poetry etc:\n\n```python3\npip install anonlink-client\n```\n\n### Documentation\n\nhttps://anonlink-client.readthedocs.io/en/stable/\n\n### CLI Tool\n\nAfter installation, you should have a `anonlink` program in your path. For\nexample, to hash PII data  `alice.csv` locally with schema `schema.json` and secret `horse`, run:\n```bash\n$ anonlink hash 'alice.csv' 'horse' 'schema.json' 'encoded-entities.json'\n```\n\nIt will generate the CLK output and store in `clk.json`. To find out how to define the schema\nfor your PII data, please refer [this page](https://clkhash.readthedocs.io/en/stable/schema.html) for \ndetails.\n\n",
    'author': 'Wilko Henecka',
    'author_email': 'wilkohenecka@gmx.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/data61/anonlink-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
