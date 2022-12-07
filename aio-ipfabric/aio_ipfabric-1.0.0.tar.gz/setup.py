# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioipfabric', 'aioipfabric.mixins']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0',
 'parsimonious>=0.10.0,<0.11.0',
 'tenacity>=8.1.0,<9.0.0']

setup_kwargs = {
    'name': 'aio-ipfabric',
    'version': '1.0.0',
    'description': 'IP Fabric asyncio client',
    'long_description': '# Python Asyncio Client for IP Fabric\n\nThis package contains a Python 3.8+ asyncio client for use wih the IP Fabric product.\n\n   * About IP Fabric: https://ipfabric.io/\n   * About IP Fabric API: https://docs.ipfabric.io/api/\n\n\n[![Downloads](https://pepy.tech/badge/aio-ipfabric)](https://pepy.tech/project/aio-ipfabric)\n![Supported Python Version](https://img.shields.io/pypi/pyversions/aio-ipfabric)\n![Contributors](https://img.shields.io/github/contributors/jeremyschulman/aio-ipfabric)\n[![License](https://img.shields.io/github/license/jeremyschulman/aio-ipfabric)](https://github.com/jeremyschulman/aio-ipfabric/blob/main/LICENSE)\n\n\n# Installating aio-ipfabric and supported versions\n\naio-ipfabric is available on [PyPI](https://pypi.org/project/aio-ipfabric/):\n\n```shell script\npip install aio-ipfabric\n```\n\nDirect installation\n```shell script\npip install git+https://github.com/jeremyschulman/aio-ipfabric@master#egg=aio-ipfabric\n```\n\nRequests officially supports Python 3.8+.\n\n\n# Quick Start\n\n````python\nfrom aioipfabric import IPFabricClient\n\nasync def demo_1_devices_list():\n    """\n    Example code that uses IPFabricClient without contextmanager\n    """\n\n    # create a client using environment variables (see next section)\n    ipf = IPFabricClient()\n\n    # alternatively create instance with parameters\n    # ipf = IPFabricClient(base_url=\'https://myipfserver.com\', username=\'admin\', password=\'admin12345\')\n    # ipf = IPFabricClient(base_url=\'https://myipfserver.com\', token=\'TOKENFROMIPF\')\n    \n    # login to IP Fabric system\n    await ipf.login()\n\n    # fetch the complete device inventory\n    device_list = await ipf.fetch_devices()\n    \n    # close asyncio connection, otherwise you will see a warning.\n    await ipf.logout()\n    \n    return device_list\n\nasync def demo_2_devices_list():\n    """\n    Example code that uses IPFabricClient as contextmanager\n    """\n\n    # create a client using environment variables (see next section)\n    async with IPFabricClient() as ipf:\n        return await ipf.fetch_devices()    \n````\n\n\n## Environment Variables\n\nThe following environment variable can be used so that you do no need to\nprovide them in your program:\n\n   * `IPF_ADDR` - IP Fabric server URL, for example "https://my-ipfabric-server.com/"\n   * `IPF_USERNAME` - Login username\n   * `IPF_PASSWORD` - Login password\n   * `IPF_TOKEN` - A persistent API token\n\nYou can use either the login credentials or the token to login.\n\nIf you prefer not to use environment variables, the call to `IPFabricClient()` accepts\nparameters; refer to the `help(IPFabricClient)` for details.\n\n# Documentation\n\nSee the [docs](docs) directory.\n\n',
    'author': 'Jeremy Schulman',
    'author_email': 'nwkautomaniac@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
