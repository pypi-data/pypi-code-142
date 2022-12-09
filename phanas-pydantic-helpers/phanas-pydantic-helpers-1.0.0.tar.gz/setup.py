# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phanas_pydantic_helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'phanas-pydantic-helpers',
    'version': '1.0.0',
    'description': 'A collection of helper functions/classes for Pydantic.',
    'long_description': '# Phana\'s Pydantic Helpers\n\n[![release](https://img.shields.io/github/v/release/phanabani/phanas-pydantic-helpers)](https://github.com/phanabani/phanas-pydantic-helpers/releases)\n[![license](https://img.shields.io/github/license/phanabani/phanas-pydantic-helpers)](LICENSE)\n\nA collection of helper functions/classes for Pydantic.\n\n## Table of Contents\n\n- [Install](#install)\n- [Usage](#usage)\n- [Developers](#developers)\n- [License](#license)\n\n## Install\n\n### Prerequisites\n\n- [Poetry](https://python-poetry.org/docs/#installation) – dependency manager\n\n### Install Phana\'s Pydantic Helpers\n\nTo get started, install the repo with Poetry.\n\n```shell\npoetry add "https://github.com/phanabani/phanas-pydantic-helpers.git"\n```\n\n## Usage\n\n```python\nfrom pydantic import BaseModel\n\nfrom phanas_pydantic_helpers import update_forward_refs_recursive, Factory\n\n@update_forward_refs_recursive\nclass MyModel(BaseModel):\n  hi: str = "there"\n  \n  class _Friend(BaseModel):\n    whats: str = "up?"\n    \n  friend: _Friend = Factory(_Friend)\n\nmodel = MyModel()\nassert model.friend.whats == "up?"\n```\n\n## Developers\n\n### Installation\n\nFollow the installation steps in [install](#install) and use Poetry to \ninstall the development dependencies:\n\n```shell\npoetry install\n```\n\n## License\n\n[MIT © Phanabani.](LICENSE)\n',
    'author': 'Phanabani',
    'author_email': 'phanabani@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Phanabani/phanas-pydantic-helpers',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
