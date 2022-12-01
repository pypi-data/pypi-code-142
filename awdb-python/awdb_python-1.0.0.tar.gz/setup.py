# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awdb']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'awdb-python',
    'version': '1.0.0',
    'description': '',
    'long_description': '# awdb-python\nwww.ipplus360.com 官方支持的解析awdb格式的Python代码(Official support for parsing Python code in AWDB format )\n',
    'author': 'ipplus360',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
