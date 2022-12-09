# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_customerio']

package_data = \
{'': ['*']}

install_requires = \
['httpx<1.0.0']

setup_kwargs = {
    'name': 'async-customerio',
    'version': '0.1.0',
    'description': 'Async CustomerIO Client - a Python client to interact with CustomerIO in an async fashion.',
    'long_description': '# async-customerio is a lightweight asynchronous client to interact with CustomerIO\n\n[![PyPI download total](https://img.shields.io/pypi/dt/async-customerio.svg)](https://pypi.python.org/pypi/async-customerio/)\n[![PyPI download month](https://img.shields.io/pypi/dm/async-customerio.svg)](https://pypi.python.org/pypi/async-customerio/)\n[![PyPI version fury.io](https://badge.fury.io/py/async-customerio.svg)](https://pypi.python.org/pypi/async-customerio/)\n[![PyPI license](https://img.shields.io/pypi/l/async-customerio.svg)](https://pypi.python.org/pypi/async-customerio/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/async-customerio.svg)](https://pypi.python.org/pypi/async-customerio/)\n[![GitHub Workflow Status for CI](https://img.shields.io/github/workflow/status/healthjoy/async-customerio/CI?label=CI&logo=github)](https://github.com/healthjoy/async-customerio/actions?query=workflow%3ACI)\n[![Codacy coverage](https://img.shields.io/codacy/coverage/b6a59cdf5ca64eab9104928d4f9bbb97?logo=codacy)](https://app.codacy.com/gh/healthjoy/async-customerio/dashboard)\n\n\n  * Free software: MIT license\n  * Requires: Python 3.7+\n\n## Features\n\n  *\n\n## Installation\n```shell script\n$ pip install async-customerio\n```\n\n## Getting started\nTBD...\n\n## License\n\n``async-customerio`` is offered under the MIT license.\n\n## Source code\n\nThe latest developer version is available in a GitHub repository:\n[https://github.com/healthjoy/async-customerio](https://github.com/healthjoy/async-customerio)\n',
    'author': 'Aleksandr Omyshev',
    'author_email': 'oomyshev@healthjoy.com',
    'maintainer': 'Healthjoy Developers',
    'maintainer_email': 'developers@healthjoy.com',
    'url': 'https://github.com/healthjoy/async-customerio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.15,<3.12',
}


setup(**setup_kwargs)
