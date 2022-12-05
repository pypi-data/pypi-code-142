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
 'typer[all]>=0.7.0,<0.8.0',
 'yt-dlp>=2022.11.11,<2023.0.0']

setup_kwargs = {
    'name': 'twitter-video-tools',
    'version': '2022.12.5',
    'description': 'Twitter Video Tools is a multi-processing supported video downloader, supports videos from twitter (or specific user from twitter) && monsnode.',
    'long_description': "# Twitter Video Tools\n\n[![PyPI version](https://badge.fury.io/py/twitter-video-tools.svg)](https://badge.fury.io/py/twitter-video-tools)\n[![Test](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml/badge.svg?branch=master)](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml)\n[![codecov](https://codecov.io/gh/code-yeongyu/TwitterVideoTools/branch/master/graph/badge.svg?token=97K8BBWOH7)](https://codecov.io/gh/code-yeongyu/TwitterVideoTools)\n\n- A multi-processing supported video downloader\n- supports downloading videos from twitter (or specific user from twitter) && monsnode.\n\n## Install\n\n### with PIP\n\n```sh\npip install twitter-video-tools\n```\n\n### with Poetry\n\n```sh\npoetry add twitter-video-tools\n```\n\n## Usage\n\n### Command line\n\n```sh\npython3 -m twitter_video_tools [link]\n```\n\nSupported link types:\n\n- Video tweet: <https://twitter.com/twtvtOfficial/status/1599748329927499777>\n- Video from [monsnode](https://monsnode.com): <https://monsnode.com/v1506575871309589251>\n- Specific user's uploaded videos: <https://twitter.com/twtvtOfficial/media>\n- Specific user's liked videos: <https://twitter.com/twtvtOfficial/likes>\n\n### Python Embedding\n\n```python\nfrom twitter_video_tools import TwitterVideoTools\n\nwith TwitterVideoTools() as twitter_video_tools:\n    twitter_video_tools.download_from_user('twtvtOfficial')\n```\n\n## Contribution\n\n### Prerequisites\n\n- Python 3.9\n- poetry\n- code editor (vscode recommended)\n\n### Overview of Development Environments\n\n- Local\n  - vscode ready (launching, debugging, formatting)\n  - strict type checking using [mypy](https://github.com/python/mypy) & [pyright](https://github.com/microsoft/pyright)\n    - type hint generator [monkeytype](https://github.com/Instagram/MonkeyType) also included\n  - amazing linters & formatters ([`yapf`](https://github.com/google/yapf), [`pylint`](https://github.com/PyCQA/pylint), [`isort`](https://github.com/PyCQA/isort))\n    - `unify` for forcing single-quote\n  - unit test using [`pytest`](https://github.com/myint/unify)\n\n- GitHub Actions\n  - [All PRs are statically analyzed & checked by `yapf`, `pylint`, `pyright`, `mypy`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/check_code.yaml)\n  - [All PRs are tested with `pytest`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/test.yaml)\n  - [Can be released with Github Action when creating GitHub Releases](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/release.yaml)\n\n### All-in-one\n\n```sh\ngh repo clone code-yeongyu/twitter_video_tools\npython3 -m pip install poetry\npoetry install # install dependencies\ncode --install-extension emeraldwalk.RunOnSave # to force single quote\ncode --install-extension tamasfe.even-better-toml # for handling toml\n```\n\nDone!\n\n### Test\n\n```sh\npoetry shell\ninv test\n```\n\n## Inspirations\n\n### [yt-dlp](https://github.com/yt-dlp/yt-dlp)\n- Inspired me to start this project. yt-dlp is a fork project of youtube-dl.\n- Since the cookie option of yt-dlp's twitter extractor is not working, I decided to make my own project, using browser automation.\n\n### [playwright](https://playwright.dev/python/)\n\n- Microsoft's browser automation module.\n- Another major project to made me to start this project. I made up my mind to make TwitterVideoTools to experience playwright.\n- It would be so painful to imagine making this project with selenium, but I enjoyed a lot while writing the twitter crawler part thanks to playwright.\n\n### [typer](https://typer.tiangolo.com/)\n\n- Ever since I started this project, I always wanted to support CLI with typer's awesome development experience.\n- TwitterVideoTools' CLI is written with typer, and it is so beautiful and easy to use at the same time.\n\n### [pyright](https://github.com/microsoft/pyright) & [mypy](http://mypy-lang.org/) & [monkeytype](https://github.com/Instagram/MonkeyType)\n\n- These three tools helped me to write fully-typed python code.\n- I won't start my python project without these tools.\n\n### [my python project template](https://github.com/code-yeongyu/python3.9-project-template)\n\n- I made this template to make my python project development experience better.\n  - Safe & Convient development environment\n    - Strict type checking\n    - Amazing linters & formatters\n    - Unit test supported\n- This project is also based on this template.\n",
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
