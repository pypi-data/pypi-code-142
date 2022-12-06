# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdb_codegen', 'mdb_codegen.output']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'pytz>=2022.6,<2023.0', 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'mdb-codegen',
    'version': '0.1.5',
    'description': '',
    'long_description': '# mdb-codegen\n\nA static file generator to create Django model definitions and Pydantic BaseModels from an MS Access database.\n\nThis reads data from an Access file using [mdbtools](https://github.com/mdbtools/mdbtools), see the [installation](https://github.com/mdbtools/mdbtools#installation) instructions on how to install for your os.\n\n\n## Howto\n\n This parser is based on different classes to determine the Django model name, Pydantic "BaseModel" name, and the fields for Django and/or Pydantic.\n\nThere is a command line tool to generate files, `mdb-codegen.py`\n\n - Run `poetry install`\n - Then run `cd mdb_codegen`\n - Then run `./mdb-codegen.py path_to_your_db`\n',
    'author': 'Josh Brooks',
    'author_email': 'josh@catalpa.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
