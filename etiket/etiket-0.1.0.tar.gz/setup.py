# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['etiket',
 'etiket.api.v1',
 'etiket.app',
 'etiket.app.crud',
 'etiket.app.services',
 'etiket.core',
 'etiket.flows']

package_data = \
{'': ['*']}

install_requires = \
['aiobotocore>=2.4.0,<3.0.0',
 'aiofiles>=22.1.0,<23.0.0',
 'apscheduler>=3.9.1.post1,<4.0.0',
 'black>=22.1.0,<23.0.0',
 'boto3>=1.24.4,<2.0.0',
 'certifi>=2021.10.8,<2022.0.0',
 'charset-normalizer>=2.0.12,<3.0.0',
 'fastapi>=0.70.1,<0.71.0',
 'filelock>=3.8.0,<4.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'passlib[bcrypt]>=1.7.4,<2.0.0',
 'psutil>=5.9.4,<6.0.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic[email]>=1.9.0,<2.0.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'requests>=2.28.1,<3.0.0',
 'sqlmodel>=0.0.8,<0.0.9',
 'urllib3>=1.26.8,<2.0.0',
 'uvicorn[standard]>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'etiket',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Arthur Newton',
    'author_email': 'arthur@barinobo.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
