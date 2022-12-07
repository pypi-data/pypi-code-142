# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['feedforbot', 'feedforbot.core']

package_data = \
{'': ['*']}

install_requires = \
['aiocron>=1.8,<2.0',
 'aiofiles>=22.1.0,<23.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'feedparser>=6.0.10,<7.0.0',
 'httpx>=0.23.1,<0.24.0',
 'jinja2>=3.1.2,<4.0.0',
 'orjson>=3.8.2,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'sentry-sdk>=1.11.1,<2.0.0']

entry_points = \
{'console_scripts': ['feedforbot = feedforbot.cli:main']}

setup_kwargs = {
    'name': 'feedforbot',
    'version': '3.3.0',
    'description': 'Forward links from RSS/Atom feeds to messengers',
    'long_description': 'FeedForBot\n==========\n\n[![PyPI](https://img.shields.io/pypi/v/feedforbot.svg)](https://pypi.python.org/pypi/feedforbot)\n[![PyPI](https://img.shields.io/pypi/dm/feedforbot.svg)](https://pypi.python.org/pypi/feedforbot)\n[![Docker Pulls](https://img.shields.io/docker/pulls/shpaker/feedforbot)](https://hub.docker.com/r/shpaker/feedforbot)\n[![PyPI](https://img.shields.io/badge/code%20style-black-000000.svg)](href="https://github.com/psf/black)\n\nForward links from RSS/Atom feeds to messengers\n\nInstallation\n------------\n\n```commandline\npip install feedforbot -U\n```\n\nUsage\n-----\n\n### From code\n\n```python\nimport asyncio\n\nfrom feedforbot import Scheduler, TelegramBotTransport, RSSListener\n\n\ndef main():\n  loop = asyncio.new_event_loop()\n  asyncio.set_event_loop(loop)\n  scheduler = Scheduler(\n    \'* * * * *\',\n    listener=RSSListener(\'https://www.debian.org/News/news\'),\n    transport=TelegramBotTransport(\n      token=\'123456789:AAAAAAAAAA-BBBB-CCCCCCCCCCCC-DDDDDD\',\n      to=\'@channel\',\n    )\n  )\n  scheduler.run()\n  loop.run_forever()\n\nif __name__ == \'__main__\':\n  main()\n```\n\n### CLI\n\n#### Save to file `config.yml` data\n\n```yaml\ncache:\n  type: \'files\'\nschedulers:\n  - listener:\n      type: \'rss\'\n      params:\n        url: \'https://www.debian.org/News/news\'\n    transport:\n      type: \'telegram_bot\'\n      params:\n        token: \'123456789:AAAAAAAAAA-BBBB-CCCCCCCCCCCC-DDDDDD\'\n        to: \'@channel\'\n```\n\n#### Start script\n\n```commandline\nfeedforbot --verbose config.yml\n```\n\n### Docker \n\n#### Docker Hub\n\n```commandline\ndocker run shpaker/feedforbot --help\n```\n\n#### GHCR\n\n```commandline\ndocker run ghcr.io/shpaker/feedforbot --help\n```\n',
    'author': 'Aleksandr Shpak',
    'author_email': 'shpaker@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shpaker/feedforbot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
