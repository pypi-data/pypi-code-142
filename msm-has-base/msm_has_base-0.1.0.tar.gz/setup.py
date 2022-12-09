# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msm_has_base']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'msm-has-base',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': '袁首京',
    'author_email': 'yuanshoujing@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
