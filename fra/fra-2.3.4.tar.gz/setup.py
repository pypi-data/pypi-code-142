# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['migrations',
 'migrations.versions',
 'motor',
 'organizations',
 'server',
 'server.api',
 'server.api.handlers',
 'server.schemas']

package_data = \
{'': ['*']}

install_requires = \
['Flask-CeleryExt>=0.4.3,<0.5.0',
 'Flask-Migrate>=3.1.0,<4.0.0',
 'celery>=5.2.7,<6.0.0',
 'flask-rebar>=2.2.1,<3.0.0',
 'pandas>=1.5.0,<2.0.0',
 'psycopg2>=2.9.5,<3.0.0',
 'redis>=4.3.4,<5.0.0']

setup_kwargs = {
    'name': 'fra',
    'version': '2.3.4',
    'description': 'Simple Recommendation System, content based.',
    'long_description': '# FRA\nFra is a Recommendation based framework. It was created with the idea of have an option for creating content-based recommendations easily via API.\n\n\n## Architecture\n\n![Architecture diagram](docs/architecture_1.png)\n\n## Requirements\n* pyenv (optional but recommended)\n* poetry\n* python 3.9+\n* postgres\n* redis\n\n## Installation\n* create a virtualenv\n    >pyenv virtualenv 3.9.15 fra\n    >pyenv activate fra\n* create a database and update the config.py file with the name and host\n    >psql; create database fra; \\q\n* install the requirements\n    >poetry install\n* migrate the models \n    > flask --app server/app db upgrade\n\n\n## Running the app\n\n* activate the environment\n    > pyenv activate fra\n* run the app\n    > flask --app server/app run\n\n-- For async jobs that process recommendations\n\n    > celery -A motor.tasks worker  --loglevel=info  \n\n\nOpenAPI docs will be online on YOURDOMAIN/api/swagger/ui\n\nFollow this order to be able to get recommendations:\n1. create an organization\n2. add users to the organization\n3. add the files with the data (some examples on example_data folder)\n4. add file mapping\n5. add user ratings\n6. get recommendations\n\n\n## TODO\n\n* Build and publish on GCP\n* Add more data set to the examples\n',
    'author': 'Eliecer Daza',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/elin3t/fra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
