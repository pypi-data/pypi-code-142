# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zlogin']

package_data = \
{'': ['*']}

install_requires = \
['boto3', 'kiteconnect', 'pyotp']

setup_kwargs = {
    'name': 'zlogin',
    'version': '0.0.7',
    'description': 'Zerodha Login Automation - Selenium Based',
    'long_description': '# Zerodha Login Automated; Supported by Lambda function that processes the redirect rul and stores accessk key to DynamoDB AND GCP function that automates login through headless chrome\n\n## Context\nThis code is for a python package for automated login to Zerodha. The redirect URL is not handled here - Separate Repo with a container that runs as a lambda function saves the access token to dynamoDB\n\n## How to productionalize\n- Get Zerodha (kite.trade) account for API based access to the platform.\n- Create a \'.zerodha\' file in your home directory (Sample provided - check .zerodha.sample file)\n    - Needed Variables in File are Zerodha API keys/secret\n\n\n- Checkout zlogin-puppeteer repository that automates login process (using headless chrome)\n- Check out the zerodha-dynamodb-save-accesstoken repository to set up a lambda function to handle Zerodha redirect url (it saves the access token in the save_access table in dynamodb)\n- Install zlogin package from pypi, "pip install zlogin"\n\n```python\nimport zlogin\naccess_token = zlogin.fetch_access_token()\n```\n\n## This repo is a sister repo with zerodha-dynamodb-save-accesstoken & zlogin-puppeteer tools which has a container code for lambda function that handles storage of access token to dynamodb; \n',
    'author': 'Prabhat Rastogi',
    'author_email': 'prabhatrastogik@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/prabhatrastogik/zlogin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
