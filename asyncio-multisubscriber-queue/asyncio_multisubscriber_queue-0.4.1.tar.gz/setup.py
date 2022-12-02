# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncio_multisubscriber_queue']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pytest = pytest:main']}

setup_kwargs = {
    'name': 'asyncio-multisubscriber-queue',
    'version': '0.4.1',
    'description': 'Allow a single producer to provide the same payload to multiple consumers simultaneously',
    'long_description': '# asyncio-multisubscriber-queue\n\n[![PyPI version](https://img.shields.io/pypi/v/asyncio-multisubscriber-queue)](https://pypi.org/project/asyncio-multisubscriber-queue/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/asyncio-multisubscriber-queue)](https://pypi.org/project/asyncio-multisubscriber-queue/)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![](https://github.com/smithk86/asyncio-multisubscriber-queue/workflows/pytest/badge.svg)](https://github.com/smithk86/asyncio-multisubscriber-queue/actions?query=workflow%3Apytest)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Usage\n\nMultisubscriberQueue allows a single producer to provide the same payload to multiple consumers simultaneously. An asyncio.Queue is created for each consumer and each call to MultisubscriberQueue.put() iterates over each asyncio.Queue and puts the payload on each queue.\n\nPlease see [example.py](https://github.com/smithk86/asyncio-multisubscriber-queue/blob/master/example.py) for a simple example.\n',
    'author': 'Kyle Smith',
    'author_email': 'smithk86@smc3.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/smithk86/asyncio-multisubscriber-queue',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
