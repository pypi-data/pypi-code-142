# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_base_framework']

package_data = \
{'': ['*']}

install_requires = \
['flask>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'py-base-framework',
    'version': '0.0.7',
    'description': '抖店微应用 python 框架',
    'long_description': '抖店微应用 python 框架',
    'author': '陈志峰',
    'author_email': 'chenzhifeng.777@bytedance.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
