# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['git_send_telegram']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.1.29,<4.0.0',
 'pyrogram>=2.0.64,<3.0.0',
 'tgcrypto>=1.2.5,<2.0.0']

entry_points = \
{'console_scripts': ['git-send-telegram = git_send_telegram:main']}

setup_kwargs = {
    'name': 'wldhx-git-send-telegram',
    'version': '0.1.2',
    'description': 'Your git send-email for 2023!',
    'long_description': "# git send-telegram\n\nyour git send-email for 2023!\n\n## Setup\n\n- Obtain API credentials from <https://core.telegram.org/api/obtaining_api_id>\n- Set credentials:\n  ```\n  git config sendtelegram.apiid <api_id>\n  git config sendtelegram.apihash <api_hash>\n  ```\n- Set session string:\n  ```\n  TELEGRAM_API_ID=<api_id> TELEGRAM_API_HASH=<api_hash> ./export-session-string.py\n  git config sendtelegram.sessionstring <session_string>\n  ```\n\nYou're good to go, let's get those patches a-sending!\n\n`git send-telegram --to torvalds HEAD^!`\n",
    'author': 'wldhx',
    'author_email': 'wldhx+pypi_python_org@wldhx.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.sr.ht/~wldhx/git-send-telegram',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
