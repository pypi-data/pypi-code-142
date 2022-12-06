# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['presto']

package_data = \
{'': ['*']}

install_requires = \
['attrdict3>=2.0.2,<3.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'presto-requests',
    'version': '0.3.6',
    'description': '',
    'long_description': '# Presto! Requests\n\nAn object-oriented REST API client & requests extesion library.\n\n## Installation\n\n```bash\npip install presto-requests\n```\n```bash\npoetry add presto-requests\n```\n\n### Concept:\n\nPresto! Requests is a library that extends the functionality of the requests library.\nIt provides a simple way to create a REST API client that is object-oriented and easy to use.\n\n### Example:\n\n```python\nfrom pprint import pprint\nfrom presto import Presto\n\npresto = Presto("https://api.github.com")\n\nuser = presto.users.sitbon()  # == presto.users["sitbon"]()\n\nprint(f"User {user.attr.login} has {user.attr.public_repos} public repositories.")\n\npprint(user.json())\n```\n```shell\nUser sitbon has 15 public repositories.\n{\'avatar_url\': \'https://avatars.githubusercontent.com/u/1381063?v=4\',\n \'bio\': None,\n \'blog\': \'\',\n \'company\': None,\n \'created_at\': \'2012-01-26T04:25:21Z\',\n \'email\': None,\n \'events_url\': \'https://api.github.com/users/sitbon/events{/privacy}\',\n \'followers\': 7,\n \'followers_url\': \'https://api.github.com/users/sitbon/followers\',\n \'following\': 13,\n \'following_url\': \'https://api.github.com/users/sitbon/following{/other_user}\',\n \'gists_url\': \'https://api.github.com/users/sitbon/gists{/gist_id}\',\n \'gravatar_id\': \'\',\n \'hireable\': None,\n \'html_url\': \'https://github.com/sitbon\',\n \'id\': 1381063,\n \'location\': \'Portland, OR, USA\',\n \'login\': \'sitbon\',\n \'name\': \'Phillip Sitbon\',\n \'node_id\': \'MDQ6VXNlcjEzODEwNjM=\',\n \'organizations_url\': \'https://api.github.com/users/sitbon/orgs\',\n \'public_gists\': 4,\n \'public_repos\': 15,\n \'received_events_url\': \'https://api.github.com/users/sitbon/received_events\',\n \'repos_url\': \'https://api.github.com/users/sitbon/repos\',\n \'site_admin\': False,\n \'starred_url\': \'https://api.github.com/users/sitbon/starred{/owner}{/repo}\',\n \'subscriptions_url\': \'https://api.github.com/users/sitbon/subscriptions\',\n \'twitter_username\': None,\n \'type\': \'User\',\n \'updated_at\': \'2022-11-22T00:41:18Z\',\n \'url\': \'https://api.github.com/users/sitbon\'}\n\n```\n\n### Usage:\n\nEach dot in the path of the request is a new request object.\n\nCalling the object without any arguments will execute the request and return the response object.\n\nIndexing the object like a list is a convient way to extend the path to a new object for things\nlike id paths, e.g. `presto.note[1]()`.\n\nSpecifying keyword arguments will add them to the request as keyword arguments to requests.request(),\nand then return the current object for further chaining.\n\nThere are a few special top-level attributes that can be used to modify the request:\n`get`, `post`, `put`, `patch`, `delete`, `head`, `options`, and finally `request` which is\nan empty path component that can be used to indirectly modify existing top-level auto created request objects.\n\nAll of these top-level attributes are able to clone existing request attributes, to modify the path\nand parent parameters while using the same component path and parameters.\n\nFor example:\n\n```python\nfrom presto import Presto\n\npresto = Presto("http://127.0.0.1:8000", APPEND_SLASH=True)\n\napi = presto.api\n\nprint("api:", api)\nprint("presto.request.api:", presto.request.api)\n\napi(headers={"X-User": "Testing"})(allow_redirects=False)\n\nprint("api(...):", api)\n\nresp = api.note[4]()\n\nprint("req headers:", resp.request.headers)\nprint("resp:", resp)\nprint("note:", resp.attr)\n```\n```output\napi: Request(url=\'http://127.0.0.1:8000/api/\', params=adict(method=\'GET\', headers=adict(Accept=\'application/json\')))\npresto.request.api: Request(url=\'http://127.0.0.1:8000/api/\', params=adict(method=\'GET\', headers=adict(Accept=\'application/json\')))\napi(...): Request(url=\'http://127.0.0.1:8000/api/\', params=adict(method=\'GET\', headers=adict(Accept=\'application/json\', X-User=\'Testing\'), allow_redirects=False))\nreq headers: {\'User-Agent\': \'python-requests/2.28.1\', \'Accept-Encoding\': \'gzip, deflate\', \'Accept\': \'application/json\', \'Connection\': \'keep-alive\', \'X-User\': \'Testing\'}\nresp: <Response [200]>\nnote: adict(id=4, url=\'http://127.0.0.1:8000/api/note/4/\', time=\'2022-12-02T19:26:09-0800\', note=\'Hello from the API!!\', collection=\'http://127.0.0.1:8000/api/coll/3/\')\n```\n\n`response.attr` is an `adict` instance, which is a dictionary that can be accessed as attributes.\nIt contains the JSON-decoded content of a response, if any.\n\n`APPEND_SLASH` is meant to be client implementation-specific, e.g. for a Django Rest Framework client, one would\ntypically set `Presto.APPEND_SLASH = True` or inherit from `Presto` in a pre-defined API client class.\n',
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
