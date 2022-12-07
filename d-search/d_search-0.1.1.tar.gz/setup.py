# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['d_search']

package_data = \
{'': ['*']}

install_requires = \
['lxml==4.9.1', 'pydantic>=1.9.1,<1.10.0']

setup_kwargs = {
    'name': 'd-search',
    'version': '0.1.1',
    'description': '网页数据处理工具',
    'long_description': 'None',
    'author': 'wangmengdi',
    'author_email': 'wangmengdi@smart-insight.com.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
