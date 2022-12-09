# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imqfody']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'imqfody',
    'version': '0.1.3',
    'description': 'Python wrapper for IntelMQ Fody API',
    'long_description': '# Python IntelMQ Fody Wrapper\n\nThis is a small module wrapping [IntelMQ Fody API](https://github.com/Intevation/intelmq-fody-backend) for easier use within Python projects.  ',
    'author': '3c7',
    'author_email': '3c7@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/3c7/python-imqfody',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
