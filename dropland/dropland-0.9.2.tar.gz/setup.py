# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dropland',
 'dropland.app',
 'dropland.core',
 'dropland.core.loaders',
 'dropland.data',
 'dropland.data.cache',
 'dropland.data.models',
 'dropland.data.serializers',
 'dropland.engines',
 'dropland.engines.databases',
 'dropland.engines.elasticsearch',
 'dropland.engines.redis',
 'dropland.engines.rmq',
 'dropland.engines.scheduler',
 'dropland.engines.sqla',
 'dropland.ext',
 'dropland.ext.fastapi',
 'dropland.tr']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy-Utils>=0.37.2,<0.38.0',
 'contextvars>=2.4,<3.0',
 'dependency-injector[pydantic]>=4.40.0',
 'orjson>=3.8.1,<4.0.0',
 'poetry-version>=0.2.0,<0.3.0',
 'pydantic[email,dotenv]>=1.8.2,<2.0.0',
 'pytz>=2021.3,<2022.0',
 'timeparse-plus>=1.2.0,<2.0.0',
 'tomlkit<0.6.0']

extras_require = \
{':extra == "fastapi"': ['fastapi[all]>=0.85.0'],
 'db': ['alembic>=1.8.0,<2.0.0', 'databases>=0.6.1'],
 'elasticsearch': ['elasticsearch[async]>=7.17.7,<8.0.0'],
 'mysql': ['aiomysql>=0.0.21', 'pymysql[rsa]>=0.9,<=0.9.3'],
 'pg': ['asyncpg>=0.22.0,<0.23.0', 'psycopg2>=2.8.6,<3.0.0'],
 'redis': ['aioredis[hiredis]<=1.3.1', 'redis>=4.1.0'],
 'rmq': ['aio-pika>=8.2.0'],
 'scheduler': ['APScheduler>=3.7.0', 'rpyc>=5.1.0'],
 'sqla': ['SQLAlchemy[asyncio,mypy]>=1.4,<2.0', 'alembic>=1.8.0,<2.0.0'],
 'sqlite': ['aiosqlite>=0.17.0,<0.18.0']}

setup_kwargs = {
    'name': 'dropland',
    'version': '0.9.2',
    'description': 'Mini-framework for building a backend servers for web-services using SQLAlchemy, Databases, Redis, RabbitMQ and APScheduler',
    'long_description': 'Dropland\n========\n\nMini-framework for building a backend servers for web-services using SQLAlchemy, Databases, Redis, RabbitMQ and APScheduler\n\n\nHow to build\n------------\n\n- Create a Python virtual environment.\n\n    ``pyenv local 3.9.0``\n\n    ``pip install --upgrade pip``\n\n    ``poetry env use $(pyenv which python)``\n\n    ``pip install poetry``\n\n\n- Install the project\n\n    ``poetry install --no-root --extras "extras"``\n\n\nWhere extras may be in: `sqla`, `db`, `redis`, `rmq`, `sqlite`, `pg`, `mysql`, `scheduler`, `fastapi`, `test`\n\n\n- Start the docker environment for development\n\n    ``docker-compose up -d``\n\n\n- Run tests\n\n    ``poetry run pytest``\n\n\n- Stop the docker environment\n\n    ``docker-compose down``\n\n\n- Uninstall the project\n\n    ``pip uninstall dropland -y``\n',
    'author': 'Max Plutonium',
    'author_email': 'plutonium.max@gmail.com',
    'maintainer': 'Max Plutonium',
    'maintainer_email': 'plutonium.max@gmail.com',
    'url': 'https://gitlab.com/thegamma/dropland',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
