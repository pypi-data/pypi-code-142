# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pastek']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pastek',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'achevrot',
    'author_email': 'antoine.chevrot@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
