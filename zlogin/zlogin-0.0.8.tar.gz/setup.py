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
    'version': '0.0.8',
    'description': 'Zerodha Login Automation - Selenium Based',
    'long_description': '# Zerodha Login Automated; This package reads access token stored in dynamodb and provides KiteConnect / KiteTicker instances.\n# This package can only be used in conjunction with a dynamodb access_store that keeps access key stored \n## Context\nThis code is for a python package for automated login to Zerodha. The redirect URL is not handled here - Separate Repos with a container that runs as a lambda function saves the access token to dynamoDB\n\nCheck out zlogin-puppeteer (headless chrome based login to zerodha) [can be hosted for free in Google cloud functions]\nand zerodha-dynamodb-save-accesstoken [AWS lambda container] to save access token to dynamodb from redirect url.\n\n## How to productionalize\n- Get Zerodha (kite.trade) account for API based access to the platform.\n- Save the API key as env variable ZAPI\n\n- Checkout zlogin-puppeteer repository that automates login process (using headless chrome)\n- Check out the zerodha-dynamodb-save-accesstoken repository to set up a lambda function to handle Zerodha redirect url (it saves the access token in the save_access table in dynamodb)\n- Install zlogin package from pypi, "pip install zlogin"\n\n```python\nimport zlogin\naccess_token = zlogin.fetch_access_token()\n```\n\n## This repo is a sister repo with zerodha-dynamodb-save-accesstoken & zlogin-puppeteer tools which have a container code for lambda function that handles storage of access token to dynamodb and puppeteer based Google Cloud Function code to handle login process which redirects to the lambda.\n',
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
