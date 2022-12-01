# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netcheck']

package_data = \
{'': ['*']}

install_requires = \
['dnspython>=2.2,<3.0',
 'pydantic>=1.10,<2.0',
 'requests>=2.28,<3.0',
 'rich>=12.6.0,<13.0.0',
 'typer[all]>=0.7,<0.8']

entry_points = \
{'console_scripts': ['netcheck = netcheck.cli:app']}

setup_kwargs = {
    'name': 'netcheck',
    'version': '0.1.7',
    'description': '',
    'long_description': '\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/netcheck) [![Coverage Status](https://coveralls.io/repos/github/hardbyte/netcheck/badge.svg?branch=main)](https://coveralls.io/github/hardbyte/netcheck?branch=main) ![PyPI - Downloads](https://img.shields.io/pypi/dm/netcheck)\n\n# Network Health Check\n\nConfigurable command line application that can be used to test network conditions are as expected.\n\nVery early work in progress version!\n\n## Quickstart\n\n\n\n### Installation\n\nInstall the Python package:\n\n```\npip install netcheck\n```\n\nOr use with Docker:\n\n```shell\ndocker pull ghcr.io/hardbyte/netcheck:latest\n```\n\n### Individual Assertions\n\nBy default `netcheck` won\'t output anything if the check passes. \n\n```\n$ poetry run netcheck dns\n```\n\nPass the `-v` flag to see what is going on:\n\n```\n$ poetry run netcheck dns -v\nDNS check with nameserver None looking up host \'github.com\'\n✔ Passed (as expected)\n{\n  "type": "dns",\n  "nameserver": null,\n  "host": "github.com",\n  "timeout": 10,\n  "result": {\n    "A": [\n      "20.248.137.48"\n    ]\n  }\n}\n```\n\nEach check can be configured, e.g. you can specify the `server` and `host` for a `dns` check, and\ntell `netcheck` whether a particular configuration is expected to pass or fail:\n\n```\n$ poetry run netcheck dns --server 1.1.1.1 --host hardbyte.nz --should-pass -v\nDNS check with nameserver 1.1.1.1 looking up host \'hardbyte.nz\'\n✔ Passed (as expected)\n{\n  "type": "dns",\n  "nameserver": "1.1.1.1",\n  "host": "hardbyte.nz",\n  "timeout": 10,\n  "result": {\n    "A": [\n      "209.58.165.79"\n    ]\n  }\n}\n\n```\n\nA few other individual examples:\n```\n$ netcheck dns --server=1.1.1.1 --host=made.updomain --should-fail -v\nDNS check with nameserver 1.1.1.1 looking up host \'made.updomain\'\n❌ Failed. As expected.\n{\n  "type": "dns",\n  "nameserver": "1.1.1.1",\n  "host": "made.updomain",\n  "timeout": 10,\n  "result": {\n    "exception-type": "NXDOMAIN",\n    "exception": "The DNS query name does not exist: made.updomain."\n  }\n}\n\n$ netcheck http --method=get --url=https://s3.ap-southeast-2.amazonaws.com --should-pass\n$ poetry run netcheck http --method=post --url=https://s3.ap-southeast-2.amazonaws.com --should-fail -v\nhttp check with url \'https://s3.ap-southeast-2.amazonaws.com\'\n❌ Failed. As expected.\n{\n  "type": "http",\n  "method": "post",\n  "url": "https://s3.ap-southeast-2.amazonaws.com",\n  "result": {\n    "status-code": 405,\n    "exception-type": "HTTPError",\n    "exception": "405 Client Error: Method Not Allowed for url: https://s3.ap-southeast-2.amazonaws.com/"\n  }\n}\n\n```\n\n\n### Configuration via file\n\nThe main way to run `netcheck` is passing in a list of assertions. \nA json file can be provided with a list of assertions to be checked:\n\n```json\n{\n  "assertions": [\n    {"name":  "deny-cloudflare-dns", "rules": [{"type": "dns", "server":  "1.1.1.1", "host": "github.com", "expected": "pass"}] }\n  ]\n}\n```\n\nAnd the command can be called:\n```\n$ poetry run netcheck run --config config.json \nLoaded 2 assertions\nRunning test \'cloudflare-dns\'\nRunning test \'github-status\'\n```\n\nOr with `--verbose`:\n\n```shell\n$ poetry run netcheck run --config tests/testdata/simple-config.json -v\nLoaded 2 assertions\nRunning test \'cloudflare-dns\'\nDNS check with nameserver 1.1.1.1 looking up host \'github.com\'\n✔ Passed (as expected)\n{\n  "type": "dns",\n  "nameserver": "1.1.1.1",\n  "host": "github.com",\n  "timeout": 10,\n  "result": {\n    "A": [\n      "20.248.137.48"\n    ]\n  }\n}\nRunning test \'github-status\'\nhttp check with url \'https://github.com/status\'\n✔ Passed (as expected)\n{\n  "type": "http",\n  "method": "get",\n  "url": "https://github.com/status",\n  "result": {\n    "status-code": 200\n  }\n}\n\n```\n\n## Development\n\nUpdate version and create a release on GitHub, Pypi release will be carried out by a Github action. \n\nTo release manually, use Poetry:\n\n```\npoetry version patch\npoetry build\npoetry publish\n```\n',
    'author': 'Brian Thorne',
    'author_email': 'brian@thorne.link',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
