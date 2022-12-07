# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncpg_trek']

package_data = \
{'': ['*']}

install_requires = \
['asyncpg>=0.26.0']

extras_require = \
{':python_version < "3.8"': ['typing_extensions>=4']}

setup_kwargs = {
    'name': 'asyncpg-trek',
    'version': '0.2.1',
    'description': 'A simple migrations system for asyncpg',
    'long_description': '# asyncpg-trek: simple migrations for asyncpg\n\nA simple library for managing migrations.\n\n## Target audience\n\nMe.\nBut maybe if you use [asyncpg] and prefer to write migrations as raw SQL (i.e. you\'re not using SQLAlchemy/Alembic) then you as well.\n\n## Features\n\n- **async**: migrations usually don\'t benefit from being async, but you benefit from using the same database driver in as your application uses (only [asyncpg] is supported).\n- **simple**: you just create `.sql` or Python files in a folder of your choosing and point this tool at that folder. No need to fight a new API to write migrations in.\n- **API centric**: there is no CLI to figure out, _you_ decide how migrations get called, _you_ control how the database connection gets created. This makes it trivial to run migrations in tests, wrap them in a CLI or run them via an exposed HTTP endpoint.\n- **declarative**: just specify the version you want and the library figures out if it needs an upgrade, downgrade or no action.\n\n## Example usage\n\n```python\nfrom pathlib import Path\n\nimport asyncpg\nfrom asyncpg_trek import plan, execute, Direction\nfrom asyncpg_trek.asyncpg import AsyncpgBackend\n\nMIGRATIONS_DIR = Path(__file__).parent / "migrations"\n\nasync def migrate(\n    conn: asyncpg.Connection,\n    target_revision: str,\n) -> None:\n    backend = AsyncpgBackend(conn)\n    async with backend.connect() as conn:\n        planned = await plan(conn, backend, MIGRATIONS_DIR, target_revision=target_revision, direction=Direction.up)\n        await execute(conn, backend, planned)\n```\n\nYou could make this an entrypoint in a docker image, an admin endpoint in your API or a helper function in your tests (or all of the above).\nHow you run your migrations depends on the complexity of your system.\nFor example, for simple systems it may be easy to run migrations on app startup based on a hardcoded revision.\nFor more complex systems you may want to run migrations manually or via an admin API.\n\nSee this release on GitHub: [v0.2.1](https://github.com/adriangb/asyncpg-trek/releases/tag/0.2.1)\n',
    'author': 'Adrian Garcia Badaracco',
    'author_email': 'adrian@adriangb.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/adriangb/asyncpg-trek',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
