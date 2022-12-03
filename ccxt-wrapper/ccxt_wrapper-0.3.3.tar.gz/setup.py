# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ccxt_wrapper', 'ccxt_wrapper.wrapper']

package_data = \
{'': ['*']}

install_requires = \
['attrs', 'ccxt', 'strenum', 'tqdm']

setup_kwargs = {
    'name': 'ccxt-wrapper',
    'version': '0.3.3',
    'description': 'A wrapper for CCXT with type hints, etc.',
    'long_description': '# CCXT Wrapper\n\n<p align="center">\n  <a href="https://github.com/34j/ccxt-wrapper/actions?query=workflow%3ACI">\n    <img src="https://img.shields.io/github/workflow/status/34j/ccxt-wrapper/CI/main?label=CI&logo=github&style=flat-square" alt="CI Status" >\n  </a>\n  <a href="https://ccxt-wrapper.readthedocs.io">\n    <img src="https://img.shields.io/readthedocs/ccxt-wrapper.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">\n  </a>\n  <a href="https://codecov.io/gh/34j/ccxt-wrapper">\n    <img src="https://img.shields.io/codecov/c/github/34j/ccxt-wrapper.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/ccxt-wrapper/">\n    <img src="https://img.shields.io/pypi/v/ccxt-wrapper.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/ccxt-wrapper.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/ccxt-wrapper.svg?style=flat-square" alt="License">\n</p>\n\nA wrapper around [CCXT](https://github.com/ccxt/ccxt) with type hints, etc. using [attrs](https://pypi.org/project/attrs/).\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install ccxt-wrapper`\n\n## Usage\n\n```Python\nimport warnings\nfrom src.ccxt_wrapper.wrapper import CCXTWrapper\nfrom ccxt.async_support import binance\n\nwith warnings.catch_warnings():\n    # ccxt_wrapper will raise numerous warnings about wrong types, missing keys, etc.\n    # This is 99% blame on ccxt :>\n    warnings.simplefilter("ignore")\n\n    # Creating exchange instance from CCXTWrapper\n    async with CCXTWrapper.new(binance, default_type=\'future\') as wrapper:\n        # Our API\n        ticker = await wrapper.fetch_ticker("BTC/USDT")\n        print(type(ticker)) # attrs class <class \'src.ccxt_wrapper.dtypes.Ticker\'>\n\n        # CCXT API\n        ticker_orginal = await wrapper.exchange.fetch_ticker("BTC/USDT")\n        print(type(ticker_orginal)) # dict <class \'dict\'>\n\n        # Same result but more fluent\n        assert ticker.high == ticker_orginal["high"]\n\n    # Using existing exchange instance\n    async with CCXTWrapper(binance()) as wrapper:\n        pass\n```\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- prettier-ignore-start -->\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tbody>\n    <tr>\n      <td align="center"><a href="https://github.com/34j"><img src="https://avatars.githubusercontent.com/u/55338215?v=4?s=80" width="80px;" alt="34j"/><br /><sub><b>34j</b></sub></a><br /><a href="https://github.com/34j/ccxt-wrapper/commits?author=34j" title="Code">💻</a></td>\n    </tr>\n  </tbody>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n<!-- prettier-ignore-end -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## Credits\n\nThis package was created with\n[Copier](https://copier.readthedocs.io/) and the\n[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)\nproject template.\n',
    'author': '34j',
    'author_email': '55338215.34j@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/34j/ccxt-wrapper',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
