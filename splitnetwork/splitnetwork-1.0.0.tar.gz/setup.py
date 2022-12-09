# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['splitnetwork']

package_data = \
{'': ['*']}

install_requires = \
['prettytable>=3.5.0,<4.0.0']

setup_kwargs = {
    'name': 'splitnetwork',
    'version': '1.0.0',
    'description': 'split the network',
    'long_description': '# 路网拆分\n',
    'author': 'DynJax',
    'author_email': 'devinceding@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
