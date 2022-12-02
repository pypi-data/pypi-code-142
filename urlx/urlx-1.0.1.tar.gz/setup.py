# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['urlx', 'urlx.url_enums']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'urlx',
    'version': '1.0.1',
    'description': 'The purpose of this package is to standardize URL declaration in the codebase',
    'long_description': '<p align="center">\n    <a href="https://volodymyrbor.github.io/urlx">\n        <img src="https://volodymyrbor.github.io/urlx/img/icon.png" alt="urlx" width="300">\n    </a>\n</p>\n\n# UrlX\n\n<a href="https://pypi.org/project/urlx" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/urlx.svg?color=%2334D058" alt="Supported Python versions">\n</a>\n<a href="https://pypi.org/project/urlx" target="_blank">\n    <img src="https://img.shields.io/pypi/v/urlx?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<img src="https://github.com/VolodymyrBor/urlx/actions/workflows/build.yml/badge.svg?event=push&branch=master" alt="Build">\n<img src="https://github.com/VolodymyrBor/urlx/actions/workflows/deploy-docs.yml/badge.svg" alt="Docs">\n\n[![Supported Versions](https://img.shields.io/badge/coverage-100%25-green)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/poetry-✅-grey)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/async-✅-grey)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/mypy-✅-grey)](https://shields.io/)\n\n---\n\n**urlx** - provide new data type - `Url`.\nThe purpose of this package is to standardize URL declaration in the codebase.\nThis approach should reduce the number of errors and speed up code writing.\n\n---\n\n## Example\n\n```python\nfrom pathlib import Path\n\nfrom urlx import Url, Protocol, Port\n\nurl = Url(\n    protocol=Protocol.HTTPS,\n    host=\'localhost\',\n    port=Port.HTTPS_443,\n    path=Path(\'api/user-list\'),\n    query={\n        \'limit\': \'100\',\n        \'skip\': \'20\',\n    },\n)\nprint(url)\n```\nOutput: \n\n> https://localhost:443/api/user-list?limit=100&skip=20\n\n---\n\n## Links\n\n**Source code**: [github.com/VolodymyrBor/urlx](https://github.com/VolodymyrBor/urlx)\n\n**Documentation**: [urlx](https://volodymyrbor.github.io/urlx/)\n\n**Changelog**: [changelog](https://volodymyrbor.github.io/urlx/changelog)\n',
    'author': 'volodymyrb',
    'author_email': 'volodymyr.borysiuk0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://volodymyrbor.github.io/urlx/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
