# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['licencer', 'licencer.errors', 'licencer.questions', 'licencer.sessions']

package_data = \
{'': ['*']}

install_requires = \
['aiosqlite>=0.17.0,<0.18.0',
 'fastapi-sessions>=0.3.2,<0.4.0',
 'fastapi>=0.87.0,<0.88.0',
 'oracledb>=1.2.1,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests-oauthlib>=1.3.1,<2.0.0',
 'returns>=0.19.0,<0.20.0',
 'sqlalchemy[asyncio]>=2.0.0b3,<3.0.0',
 'uvicorn>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'licencer',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Backend Licencer\n\n## Sposób budowy i uruchomienia za pomocą docker\n\n```sh\ndocker build -t licencer_be .\n```\n\n```sh\ndocker run --rm -p 8080:8080 --env-file ENV_FILE licencer_be \n```\n',
    'author': 'Jakub Ostrzołek',
    'author_email': 'jakub.ostrzolek.stud@pw.edu.pl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
