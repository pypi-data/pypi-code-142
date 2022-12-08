# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arabic_to_roman']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'arabic-to-roman',
    'version': '1.0.0',
    'description': 'Arabic number to Roman numeral converter',
    'long_description': '# Arabic number to Roman numeral converter\n\nA simple converter that converts an Arabic number (e.g. `42`) to a Roman numeral (e.g. `XLII`).\n\nRequires [Poetry](https://python-poetry.org/) to install:\n\n```sh\npoetry install --no-dev\n```\n\n## Running the tests\n\nThe tests consist of:\n\n* Unit tests using `pytest`\n* Static type checking using `mypy`\n\nTo run the tests, first install the required packages using\n\n```sh\npoetry install\n```\n\nThen run the tests with\n\n```sh\npoetry run test\n```\n',
    'author': 'Carl Mattsson',
    'author_email': 'carl.mattsson@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
