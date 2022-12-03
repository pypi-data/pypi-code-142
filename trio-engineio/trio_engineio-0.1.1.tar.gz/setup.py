# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['trio_engineio']

package_data = \
{'': ['*']}

install_requires = \
['httpcore>=0.16.0,<0.17.0',
 'trio-websocket>=0.9.2,<0.10.0',
 'trio>=0.22.0,<0.23.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.4.0,<5.0.0']}

setup_kwargs = {
    'name': 'trio-engineio',
    'version': '0.1.1',
    'description': 'An asynchronous Engine.IO client using the trio framework',
    'long_description': '\n# Trio-Engine.IO\n\n[![python](https://img.shields.io/badge/python-3.7%2B-blue)](https://github.com/Elmeric/trio-engineio)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Tests](https://github.com/Elmeric/trio-engineio/actions/workflows/test.yml/badge.svg)](https://github.com/Elmeric/trio-engineio/actions/workflows/test.yml)\n[![Coverage Status](https://coveralls.io/repos/github/Elmeric/trio-engineio/badge.svg)](https://coveralls.io/github/Elmeric/trio-engineio)\n[![license](https://img.shields.io/badge/license-BSD--3--Clause-green)](https://github.com/Elmeric/trio-engineio/blob/master/LICENSE)\n\nAn asynchronous **[Engine.IO](https://github.com/socketio/engine.io-protocol/tree/v3)** client using the [`trio`](https://trio.readthedocs/en/latest) framework.\n\nOnly the revision **3** of the Engine.IO protocol is supported.\n\n## Requirements\n\n- Python 3.7+\n- [`trio`](https://trio.readthedocs.io/)\n- [`httpcore`](https://www.encode.io/httpcore/)\n- [`trio-websocket`](https://trio-websocket.readthedocs.io/)\n\n## Usage\n\n```Python\nimport trio\n\nfrom trio_engineio.trio_client import EngineIoClient, EngineIoConnectionError\n\n\ndef on_connect():\n    print(f"***** Connected")\n\n\ndef on_message(msg):\n    print(f"***** Received message: {msg}")\n\n\ndef on_disconnect():\n    print(f"***** Disconnected")\n\n    \nasync def main():\n    eio = EngineIoClient(logger=False)\n\n    eio.on("connect", on_connect)\n    eio.on("message", on_message)\n    eio.on("disconnect", on_disconnect)\n\n    async with trio.open_nursery() as nursery:\n        try:\n            await eio.connect(nursery, "http://127.0.0.1:1234")\n        except EngineIoConnectionError:\n            return False\n    return True\n\n\ntrio.run(main)\n```\n',
    'author': 'Eric Lemoine',
    'author_email': 'erik.lemoine@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Elmeric/trio-engineio',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
