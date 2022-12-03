# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['parallel_apply']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'parallel-apply',
    'version': '0.1.1',
    'description': '',
    'long_description': 'None',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
