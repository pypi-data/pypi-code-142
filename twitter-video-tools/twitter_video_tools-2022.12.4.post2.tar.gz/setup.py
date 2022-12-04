# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twitter_video_tools',
 'twitter_video_tools.tests',
 'twitter_video_tools.utils']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'playwright>=1.27.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'yt-dlp>=2022.11.11,<2023.0.0']

setup_kwargs = {
    'name': 'twitter-video-tools',
    'version': '2022.12.4.post2',
    'description': 'Twitter Video Tools is a multi-processing supported video downloader, supports videos from twitter (or specific user from twitter) && monsnode.',
    'long_description': '# Twitter Video Tools\n\n[![PyPI version](https://badge.fury.io/py/twitter-video-tools.svg)](https://badge.fury.io/py/twitter-video-tools)\n[![Test](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml/badge.svg?branch=master)](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml)\n[![codecov](https://codecov.io/gh/code-yeongyu/TwitterVideoTools/branch/master/graph/badge.svg?token=97K8BBWOH7)](https://codecov.io/gh/code-yeongyu/TwitterVideoTools)\n\n- A multi-processing supported video downloader\n- supports downloading videos from twitter (or specific user from twitter) && monsnode.\n\n## Install\n\n### with PIP\n\n```sh\npip install twitter-video-tools\n```\n\n### with Poetry (Recommended)\n\n```sh\npoetry add twitter-video-tools\n```\n\n## Contribution\n\n### Prerequisites\n\n- Python 3.9\n- poetry\n- code editor (vscode recommended)\n\n### Overview of Development Environments\n\n- Local\n  - vscode ready (launching, debugging, formatting)\n  - strict type checking using [mypy](https://github.com/python/mypy) & [pyright](https://github.com/microsoft/pyright)\n    - type hint generator [monkeytype](https://github.com/Instagram/MonkeyType) also included\n  - amazing linters & formatters ([`yapf`](https://github.com/google/yapf), [`pylint`](https://github.com/PyCQA/pylint), [`isort`](https://github.com/PyCQA/isort))\n    - `unify` for forcing single-quote\n  - unit test using [`pytest`](https://github.com/myint/unify)\n\n- GitHub Actions\n  - [All PRs are statically analyzed & checked by `yapf`, `pylint`, `pyright`, `mypy`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/check_code.yaml)\n  - [All PRs are tested with `pytest`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/test.yaml)\n  - [Can be released with Github Action when creating GitHub Releases](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/release.yaml)\n\n### All-in-one\n\n```sh\ngh repo clone code-yeongyu/twitter_video_tools\npython3 -m pip install poetry\npoetry install # install dependencies\ncode --install-extension emeraldwalk.RunOnSave # to force single quote\ncode --install-extension tamasfe.even-better-toml # for handling toml\n```\n\nDone!\n\n### Test\n\n```sh\npoetry shell\ninv test\n```\n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/code-yeongyu/twitter_video_tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
