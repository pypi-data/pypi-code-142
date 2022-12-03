# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['japanese_dictionary_parser',
 'japanese_dictionary_parser.parsing_utils',
 'japanese_dictionary_parser.parsing_utils.parsing_dataclass']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'japanese-dictionary-parser',
    'version': '0.1.0',
    'description': 'Parsers for japanese dictionaries: JMdict and kanjidic2',
    'long_description': '# Japanese dictionary parser\n___\nThe package contains two classes for parsing dictionaries:\n* JMdict: contains information on japanese vocabulary\n* kanjidic2: contains information on japanese kanji\n',
    'author': 'Maxim R',
    'author_email': 'joey-hzpfywtd@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
