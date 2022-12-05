# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stripe_payment_setup']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'pydantic[email]>=1.9.0,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'stripe>=5.0.0,<6.0.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['stripe-payment-setup = stripe_payment_setup.app:serve']}

setup_kwargs = {
    'name': 'stripe-payment-setup',
    'version': '0.1.0',
    'description': 'Small app used to save payment details for future usage (for ex subscriptions)',
    'long_description': '# Stripe - setup payment methods\n\nUseful to generate a `checkout` session needed to save customers payment methods for recurring payments (in particular SEPA debits)\n\n\n## Requirements\n\n    poetry\n    python >= 3.9\n\n## Installation\n\n    poetry install\n\n## Config\n\nCopy `.env.sample` to `.env` and customize it\n\n## Launch the service\n\n    poetry run stripe-setup-payment\n\nJump to [http://localhost:4242/](http://localhost:4242/)',
    'author': 'Ludovic Delauné',
    'author_email': 'message@cartodev.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ldgeo/stripe-payment-setup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
