# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orwynn']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0', 'uvicorn[standard]>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'orwynn',
    'version': '0.1.0',
    'description': 'Web-framework',
    'long_description': '',
    'author': 'ryzhovalex',
    'author_email': 'thed4rkof@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
