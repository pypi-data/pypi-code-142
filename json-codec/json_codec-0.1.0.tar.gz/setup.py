# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json_codec', 'json_codec.codecs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'json-codec',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Json Codec\n\nIt's a simple library to encode and decode json to strict python types using dataclasses and builtin python types.\n\n",
    'author': 'Lucas Silva',
    'author_email': 'lucas76leonardo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
