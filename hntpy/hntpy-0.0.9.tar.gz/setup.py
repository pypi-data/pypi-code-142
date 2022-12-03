# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hntpy', 'hntpy.network', 'hntpy.resources']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'hntpy',
    'version': '0.0.9',
    'description': 'Python wrapper for Helium API to simplify interactions with the Helium blockchain.',
    'long_description': '# hntpy\n\n<p align="left">\n    <a alt="Version" href="https://pypi.org/project/hntpy/">\n    <img src="https://img.shields.io/badge/version-0.0.9-blue"/></a>\n    <a href="https://github.com/h-morgan/hntpy/blob/main/LICENSE" alt="License">\n    <img src="https://img.shields.io/github/license/h-morgan/hntpy"/></a>\n    <a href="#">\n    <img src="https://img.shields.io/badge/coverage-99%25-green"/></a>\n</p>\n\n## Introduction\n\nhntpy is a Python wrapper for Helium API to simplify requests and interaction with Helium blockchain. The aim of this project is to enable retrieval of Helium data from the API in a Pythonic way.\n\nFor comprehensive documentation (with examples), review the full usage [docs](https://github.com/h-morgan/hntpy/tree/main/docs).\n\nFor more detail on exact API responses/data, please see the officical [Helium documentation](https://docs.helium.com/api/blockchain/introduction).\n\nThis project is continually under development. If you notice a bug, or have a feature request, please submit a Github issue [here](https://github.com/h-morgan/hntpy/issues).\n\n## Install\n\nTo use the latest version of this Python package, download from PyPi:\n\n```\npip install hntpy\n```\n\n## Example Usage\n\nBelow are a couple of examples to show how the `hntpy` package can be used. For comprehensive documentation, including all function definitions, argument examples, and more, view the [full docs](https://github.com/h-morgan/hntpy/tree/main/docs).\n\n```python\nfrom hntpy import Account, Hotspot, Validator\n\n# ===================================\n\n## sample account functionality\naccount = Account(address="51-character-account-address")\n\n# get validators and hotspots associated with an account\nvalidators = account.validators()\nhotspots = account.hotspots()\n\n# get a generator of rewards, in a given time window, for an account (optionally can also return a list)\nrewards_generator = account.rewards(min_time="2022-01-01", max_time="2022-06-01", gen=True)\n\nfor batch in rewards_generator:\n    for reward in batch:\n        # do some processing with the reward here...\n\n# ===================================\n\n## sample hotspot functionality\n\nhotspot = Hotspot(address="51-character-hotspot-address")\n\n# get roles (activity) for a hotspot, can optionally provide timeframe and response limit\nroles = hotspot.roles(min_time="2022-01-01", limit=100)\n\n# get the total reward sum for the hotspot, optionally in a given timeframe\nrewards = hotspot.rewards(min_time="2022-01-01", max_time="2022-06-01")\n\n# get hotspots that the given hotspot witnessed over the last 5 days\nwitnessed = hotspot.witnessed()\n\n# ===================================\n\n## sample validator functionality\n\nvalidator = Validator(address="51-character-validator-address")\n\n# get roles (activity) for a hotspot, can optionally provide timeframe and response limit\nroles = validator.roles(limit=200)\n\n```\n\n## Return types\n\nThe Helium API returns either JSON objects (loaded as `dicts`) of data, or `lists` of data. All of the functions in the `hntpy` package that make requests to the Helium API return either:\n\n- `list`\n- `dict`\n- `GeneratorType`\n\nFor requests that have the potential to return large amounts of data, there is the option to provide a `gen=True` argument to the method, which will yield the data in batches (rather than compile and return one single large list). By default, `gen` parameter is set to `False` for all methods.\n\nTo see available return types for specific methods, see method definitions in the respective module\'s documentation page.\n',
    'author': 'Haley Morgan',
    'author_email': 'haleymorgan3264@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/h-morgan/hntpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
