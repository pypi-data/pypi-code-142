# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_xsrf']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=38.0.0,<38.1.0']

setup_kwargs = {
    'name': 'simple-xsrf',
    'version': '0.2.1',
    'description': 'Simple package to protect against CSRF/XSRF attacks',
    'long_description': '# simple-xsrf\n\nA simple package to create CSRF/XSRF tokens and protect against CSRF/XSRF attacks.\n\n### Installation\n```\npip install simple-xsrf\n```\n\n### Usage\n\nTo use this package you will need a fernet key also known as a secret key. To create a key:\n```python\nfrom cryptography.fernet import Fernet\n\nkey = Fernet.generate_key()\n```\n**Make sure to store this key in a secure place like a database so that you can access it later. You will need it to create your tokens and decrypt them**\n\nCreating a token:\n```python\nfrom simple_xsrf.token import create_xsrf\n\ntoken = create_xsrf(key)\n```\n\nChecking if a token is valid:\n```python\nfrom simple_xsrf.token import is_valid\n\nis_token_valid = is_valid(key, token_from_request, token_from_storage)\n```\nYou should store your token in a storage layer such as Redis or DynamoDB to be retrived later.\n',
    'author': 'Sam Newby',
    'author_email': 'sam.newby19@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NWBY/simple-xsrf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
