# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sheval']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sheval',
    'version': '1.1.0',
    'description': 'Safely evaluate mathematical and logical expressions.',
    'long_description': "# 🐴 sheval\n\nSafely evaluate mathematical and logical expressions. Most operations are supported.\n\n### Whitelisted data types\n\nFor security, only certain data types are allowed for constants and variables.\n\n- `str`\n- `int`\n- `float`\n- `complex`\n- `list`\n- `tuple`\n- `set`\n- `dict`\n- `bool`\n- `bytes`\n- `NoneType`\n\n## Example\n\n```py\nfrom sheval import sheval\n\n# Variables can be passed on.\nvariables = dict(\n    x =  2,\n    y =  3,\n)\n# And functions too!\nfunctions = dict(\n    double = lambda x: x * 2,\n)\n\nsheval('double(x) > y', variables, functions)\n```",
    'author': 'Maximillian Strand',
    'author_email': 'maxi@millian.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/deepadmax/sheval',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
