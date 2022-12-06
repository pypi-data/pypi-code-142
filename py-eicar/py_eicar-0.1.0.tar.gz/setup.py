# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_eicar']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-eicar',
    'version': '0.1.0',
    'description': 'pypi eicar',
    'long_description': 'dummy python module for eicar testing\n',
    'author': 'matthew.gill',
    'author_email': 'matthew.gill@servicenow.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
