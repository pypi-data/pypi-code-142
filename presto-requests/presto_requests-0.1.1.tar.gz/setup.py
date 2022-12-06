# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['presto', 'presto.typing']

package_data = \
{'': ['*']}

install_requires = \
['attrdict3>=2.0.2,<3.0.0', 'deepdiff>=6.2.1,<7.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'presto-requests',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Presto! Requests\n\nAn object-oriented REST API client & requests extesion library.\n\nExample:\n\n```python\nfrom pprint import pprint\nfrom presto import Presto\n\npresto = Presto(\'https://api.github.com\')\n\nuser = presto.users.sitbon()  # == presto.users["sitbon"]()\n\nprint(f"User {user.attr.login} has {user.attr.public_repos} public repositories.")\n\npprint(user.json())\n```\n```shell\nUser sitbon has 15 public repositories.\n{\'avatar_url\': \'https://avatars.githubusercontent.com/u/1381063?v=4\',\n \'bio\': None,\n \'blog\': \'\',\n \'company\': None,\n \'created_at\': \'2012-01-26T04:25:21Z\',\n \'email\': None,\n \'events_url\': \'https://api.github.com/users/sitbon/events{/privacy}\',\n \'followers\': 7,\n \'followers_url\': \'https://api.github.com/users/sitbon/followers\',\n \'following\': 13,\n \'following_url\': \'https://api.github.com/users/sitbon/following{/other_user}\',\n \'gists_url\': \'https://api.github.com/users/sitbon/gists{/gist_id}\',\n \'gravatar_id\': \'\',\n \'hireable\': None,\n \'html_url\': \'https://github.com/sitbon\',\n \'id\': 1381063,\n \'location\': \'Portland, OR, USA\',\n \'login\': \'sitbon\',\n \'name\': \'Phillip Sitbon\',\n \'node_id\': \'MDQ6VXNlcjEzODEwNjM=\',\n \'organizations_url\': \'https://api.github.com/users/sitbon/orgs\',\n \'public_gists\': 4,\n \'public_repos\': 15,\n \'received_events_url\': \'https://api.github.com/users/sitbon/received_events\',\n \'repos_url\': \'https://api.github.com/users/sitbon/repos\',\n \'site_admin\': False,\n \'starred_url\': \'https://api.github.com/users/sitbon/starred{/owner}{/repo}\',\n \'subscriptions_url\': \'https://api.github.com/users/sitbon/subscriptions\',\n \'twitter_username\': None,\n \'type\': \'User\',\n \'updated_at\': \'2022-11-22T00:41:18Z\',\n \'url\': \'https://api.github.com/users/sitbon\'}\n\n```',
    'author': 'Phillip Sitbon',
    'author_email': 'phillip.sitbon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
