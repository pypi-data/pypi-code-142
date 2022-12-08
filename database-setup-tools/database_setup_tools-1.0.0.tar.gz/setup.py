# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['database_setup_tools']

package_data = \
{'': ['*']}

install_requires = \
['sqlalchemy-utils==0.38.3', 'sqlalchemy==1.4.41']

setup_kwargs = {
    'name': 'database-setup-tools',
    'version': '1.0.0',
    'description': 'Tools to easily setup databases opinionated towards FastAPI and SQLModel',
    'long_description': '# Database tools\n\nEasy to understand and use tools that help you to create databases and interact with them.\n\n## Installation\n\n```bash\npip install database-setup-tools\n```\n\n## Features\n- **Database creation on app startup**\n- Thread-safe database **session manager**\n- Opinionated towards `FastAPI` and `SQLModel` but feasible with any other framework or pure `sqlalchemy`\n- Easily use a local database in your tests\n\n## Planned features\n- Database migrations with `Alembic`\n\n## Example\n\n```python\nimport random\n\nimport uvicorn\nfrom fastapi import FastAPI, Depends\nfrom sqlmodel import Session, SQLModel, Field\n\nfrom database_setup_tools.session_manager import SessionManager\nfrom database_setup_tools.setup import DatabaseSetup\n\nDATABASE_URI = "sqlite:///test.db"\n\napp = FastAPI()\nsession_manager = SessionManager(database_uri=DATABASE_URI)\n\n\nclass User(SQLModel, table=True):\n    """ User model """\n    id: int = Field(index=True, primary_key=True)\n    name: str\n\n\nmodel_metadata = SQLModel.metadata\n\n\n@app.post(\'/users/\', response_model=User)\ndef add_random_user(session: Session = Depends(session_manager.get_session)):\n    """ Endpoint to add a user with a random name """\n    user = User(name=f\'User {random.randint(0, 100)}\')\n    session.add(user)\n    session.commit()\n    return user\n\n\n@app.get(\'/users/\', response_model=list[User])\ndef get_all_users(session: Session = Depends(session_manager.get_session)):\n    """ Endpoint to get all users """\n    return session.query(User).all()\n\n\nif __name__ == \'__main__\':\n    database_setup = DatabaseSetup(model_metadata=model_metadata, database_uri=DATABASE_URI)\n    uvicorn.run(app, host=\'0.0.0.0\', port=8080)\n```\n\n *See  [tests/integration/example/app.py](tests/integration/example/app.py)\n\n## Example for pytest\n\n**conftest.py**\n```python\ndatabase_setup = DatabaseSetup(model_metadata=model_metadata, database_uri=DATABASE_URI)\n\ndef pytest_sessionstart(session):\n    database_setup.drop_database()\n    database_setup.create_database()\n```\n\n**test_users.py**\n```python\nsession_manager = SessionManager(database_uri=DATABASE_URI)\n\n@pytest.fixture\ndef session():\n\twith session_manager.get_session() as session:\n\t\tyield session\n\ndef test_create_user(session: Session):\n\tuser = User(name=\'Test User\')\n\tsession.add(user)\n\tsession.commit()\n\tassert session.query(User).count() == 1\n\tassert session.query(User).first().name == \'Test User\'\n```',
    'author': 'Jonas Scholl',
    'author_email': 'jonas@code-specialist.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
