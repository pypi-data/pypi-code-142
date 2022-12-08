# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hidetext',
 'hidetext.filters',
 'hidetext.placeholders',
 'hidetext.resources',
 'hidetext.resources.ca',
 'hidetext.resources.en']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hidetext',
    'version': '0.1.1',
    'description': 'Hides non-desired text',
    'long_description': '# Hidetext\n\nExtensible Python library to hide fragments of text.\n\n[![version](https://img.shields.io/pypi/v/hidetext?logo=pypi&logoColor=white)](https://pypi.org/project/hidetext/)\n[![build](https://github.com/jaume-ferrarons/hidetext/actions/workflows/push-event.yml/badge.svg)](https://github.com/jaume-ferrarons/hidetext/actions/workflows/push-event.yml)\n[![codecov](https://codecov.io/github/jaume-ferrarons/hidetext/branch/main/graph/badge.svg?token=MZQOAFBQ5I)](https://codecov.io/github/jaume-ferrarons/hidetext)\n\n## Installation\n**Requirements**: python >= 3.8\n\nIt can be easily installed with:\n```bash\npip install -U hidetext\n```\n\n## Basic usage\n\n\n```python\nfrom hidetext import Hidetext\n\nhide = Hidetext()\n\nprint(hide.character("""\nDear Mr Robinson,\n\nI\'m contacting you regarding \nMy DNI is 43244328J.\n\nEmail: fdsfsd@gmail.com\n"""))\n```\n\n    \n    Dear Mr Robinson,\n    \n    I\'m contacting you regarding \n    My DNI is *********.\n    \n    Email: ****************\n    \n\n\n\n```python\nprint(hide.kind("""\nDear Mr Robinson,\n\nI\'m contacting you regarding \nMy DNI is 43244328J.\n\nEmail: fdsfsd@gmail.com\n"""))\n```\n\n    \n    Dear Mr Robinson,\n    \n    I\'m contacting you regarding \n    My DNI is <ID_CARD>.\n    \n    Email: <EMAIL>\n    \n\n\n## Creating custom filters\n\nIt\'s easy to create custom filters to remove undesired text using `PatternFilter`:\n\n\n```python\nfrom typing import Dict\n\nfrom hidetext import Hidetext\nfrom hidetext.filters import PatternFilter\n\nclass HourFilter(PatternFilter):\n    name: str = "HOUR"\n\n    patterns: Dict[str, str] = {\n        "digital_hour": r"\\d{2}(:\\d{2}){1,2}",\n        "hour": "\\d{1,2}\\s?(am|pm)"\n    }\n\nhide = Hidetext(filters=[HourFilter()])\n\nhide.kind("The train departs at 15:45 and arrives at 19:35, therefore I\'ll be at the party at 8pm.")\n```\n\n\n\n\n    "The train departs at <HOUR> and arrives at <HOUR>, therefore I\'ll be at the party at <HOUR>."\n\n\n',
    'author': 'Jaume Ferrarons',
    'author_email': 'jaume.ferrarons@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jaume-ferrarons/hidetext',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
