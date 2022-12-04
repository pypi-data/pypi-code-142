# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogithubapi',
 'aiogithubapi.common',
 'aiogithubapi.graphql_examples',
 'aiogithubapi.legacy',
 'aiogithubapi.models',
 'aiogithubapi.namespaces',
 'aiogithubapi.objects',
 'aiogithubapi.objects.login',
 'aiogithubapi.objects.orgs',
 'aiogithubapi.objects.repos',
 'aiogithubapi.objects.repos.traffic',
 'aiogithubapi.objects.repository',
 'aiogithubapi.objects.repository.issue',
 'aiogithubapi.objects.users']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8,<4.0', 'backoff<3']

setup_kwargs = {
    'name': 'aiogithubapi',
    'version': '22.12.0',
    'description': 'Asynchronous Python client for the GitHub API',
    'long_description': "# aiogithubapi\n\n[![codecov](https://codecov.io/gh/ludeeus/aiogithubapi/branch/main/graph/badge.svg)](https://codecov.io/gh/ludeeus/aiogithubapi)\n![python version](https://img.shields.io/badge/Python-3.8=><=3.10-blue.svg)\n[![PyPI](https://img.shields.io/pypi/v/aiogithubapi)](https://pypi.org/project/aiogithubapi)\n![Actions](https://github.com/ludeeus/aiogithubapi/workflows/Actions/badge.svg?branch=main)\n\n_Asynchronous Python client for the GitHub API_\n\nThis is not a full client for the API (Have you seen it, it's huge), and will probably never be.\nThings are added when needed or requested.\n\nIf something you need is missing please raise [a feature request to have it added](https://github.com/ludeeus/aiogithubapi/issues/new?assignees=&labels=enhancement&template=feature_request.md) or [create a PR 🎉](#contribute).\n\nFor examples on how to use it see the [tests directory](./tests).\n\n## Install\n\n```bash\npython3 -m pip install aiogithubapi\n```\n\n## Project transition\n\n**Note: This project is currently in a transition phase.**\n\nIn august 2021 a new API interface was introduced (in [#42](https://github.com/ludeeus/aiogithubapi/pull/42)). With that addition, all parts of the old interface is now considered deprecated.\nWhich includes:\n\n- The [`aiogithubapi.common`](./aiogithubapi/common) module\n- The [`aiogithubapi.legacy`](./aiogithubapi/legacy) module\n- The [`aiogithubapi.objects`](./aiogithubapi/objects) module\n- All classes starting with `AIOGitHub`\n- The `async_call_api` function in the [`aiogithubapi.helpers.py`](./aiogithubapi/helpers.py) file\n- The `GitHubDevice` class in `aiogithubapi`, replaced with `GitHubDeviceAPI`\n- The `GitHub` class in `aiogithubapi`, replaced with `GitHubAPI`\n\nLater this year (2022), warning logs will start to be emitted for deprecated code.\n\nEarly next year (2023), the old code will be removed.\n\n## Contribute\n\n**All** contributions are welcome!\n\n1. Fork the repository\n2. Clone the repository locally and open the devcontainer or use GitHub codespaces\n3. Do your changes\n4. Lint the files with `make lint`\n5. Ensure all tests passes with `make test`\n6. Ensure 100% coverage with `make coverage`\n7. Commit your work, and push it to GitHub\n8. Create a PR against the `main` branch\n",
    'author': 'Ludeeus',
    'author_email': 'ludeeus@ludeeus.dev',
    'maintainer': 'Ludeeus',
    'maintainer_email': 'ludeeus@ludeeus.dev',
    'url': 'https://github.com/ludeeus/aiogithubapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
