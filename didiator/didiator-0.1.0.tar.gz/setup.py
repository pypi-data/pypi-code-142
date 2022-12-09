# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['didiator',
 'didiator.dispatchers',
 'didiator.interface',
 'didiator.interface.dispatchers',
 'didiator.interface.entities',
 'didiator.interface.handlers',
 'didiator.middlewares',
 'didiator.utils']

package_data = \
{'': ['*']}

extras_require = \
{'di': ['di[anyio]>=0.73.0,<0.74.0']}

setup_kwargs = {
    'name': 'didiator',
    'version': '0.1.0',
    'description': 'A library that implements the Mediator pattern and uses DI library',
    'long_description': '========\nDidiator\n========\n\n``didiator`` is an asynchronous library that implements the Mediator pattern and\nuses the `DI <https://www.adriangb.com/di/>`_ library to help you to inject dependencies to called handlers\n\nThis library is inspired by the `MediatR <https://github.com/jbogard/MediatR>`_ used in C#\nand follows CQRS principles\n\nInstallation\n============\n\nDidiator is available on pypi: https://pypi.org/project/didiator\n\n.. code-block:: bash\n\n    pip install -U didiator[di]\n\nIt will install ``didiator`` with its optional DI dependency that is necessary to use ``DiMiddleware`` and ``DiBuilder``\n\nExamples\n========\n\nYou can find examples in `this folder <https://github.com/SamWarden/didiator/tree/dev/examples>`_\n\nCreate Commands and Queries with handlers for them\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n.. code-block:: python\n\n    @dataclass\n    class CreateUser(Command[int]):\n        user_id: int\n        username: str\n\n    class CreateUserHandler(CommandHandler[CreateUser, int]):\n        def __init__(self, user_repo: UserRepo) -> None:\n            self._user_repo = user_repo\n\n        async def __call__(self, command: CreateUser) -> int:\n            user = User(id=command.user_id, username=command.username)\n            await self._user_repo.add_user(user)\n            await self._user_repo.commit()\n            return user.id\n\nYou can use functions as handlers\n\n.. code-block:: python\n\n    @dataclass\n    class GetUserById(Query[User]):\n        user_id: int\n\n    async def handle_get_user_by_id(query: GetUserById, user_repo: UserRepo) -> User:\n        user = await self._user_repo.get_user_by_id(user)\n        return user\n\nCreate DiBuilder\n~~~~~~~~~~~~~~~~\n\n``DiBuilder`` is a facade for Container from DI with caching of `solving <https://www.adriangb.com/di/0.73.0/solving/>`_\n\n``di_scopes`` is a sequence with the order of `scopes <https://www.adriangb.com/di/0.73.0/scopes/>`_\n\n``di_builder.bind(...)`` will `bind <https://www.adriangb.com/di/0.73.0/binds/>`_ ``UserRepoImpl`` type to ``UserRepo`` protocol\n\n.. code-block:: python\n\n    di_scopes = ("request",)\n    di_builder = DiBuilder(Container(), AsyncExecutor(), di_scopes)\n    di_builder.bind(bind_by_type(Dependent(UserRepoImpl, scope="request"), UserRepo))\n\nCreate Mediator and register handlers to it\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nCreate dispatchers with their middlewares and use them to initialize the ``MediatorImpl``\n\n``cls_scope`` is a scope that will be used to bind class Command/Query handlers initialized during request handling\n\n.. code-block:: python\n\n    dispatchers_middlewares = (LoggingMiddleware(), DiMiddleware(di_builder, cls_scope="request"))\n    command_dispatcher = CommandDispatcherImpl(middlewares=dispatchers_middlewares)\n    query_dispatcher = QueryDispatcherImpl(middlewares=dispatchers_middlewares)\n\n    mediator = MediatorImpl(command_dispatcher, query_dispatcher)\n\n    # CreateUserHandler is not initialized during registration\n    mediator.register_command_handler(CreateUser, CreateUserHandler)\n    mediator.register_query_handler(GetUserById, handle_get_user_by_id)\n\nMain usage\n~~~~~~~~~~\n\nEnter the ``"request"`` scope that was registered earlier and create a new Mediator with ``di_state`` bound\n\nUse ``mediator.send(...)`` for commands and ``mediator.query(...)`` for queries\n\n.. code-block:: python\n\n        async with di_builder.enter_scope("request") as di_state:\n            scoped_mediator = mediator.bind(di_state=di_state)\n\n            # It will call CreateUserHandler(...).__call__(...) and inject UserRepoImpl to it\n            user_id = await scoped_mediator.send(CreateUser(1, "Jon"))\n            user = await scoped_mediator.query(GetUserById(user_id))\n            print("User:",  user)\n        # Session of UserRepoImpl will be closed after exiting the "request" scope\n\n⚠️ **Attention: this is a beta version of** ``didiator`` **that depends on** ``DI``, **which is also in beta. Both of them can change their API!**\n\nCQRS\n====\n\nCQRS stands for "`Command Query Responsibility Segregation <https://www.martinfowler.com/bliki/CQRS.html>`_".\nIts idea about splitting the responsibility of commands (writing) and queries (reading) into different models.\n\n``didiator`` have segregated ``.send(command)`` and ``.query(query)`` methods in its ``Mediator`` and\nassumes that you will separate its handlers.\nUse ``CommandMediator`` and ``QueryMediator`` protocols to explicitly define which method you need in ``YourController``\n\n.. code-block:: mermaid\n\n    graph LR;\n        YourController-- Command -->Mediator;\n        YourController-- Query -->Mediator;\n        Mediator-. Command .->CommandDispatcher-.->di1[DiMiddleware]-.->CommandHandler;\n        Mediator-. Query .->QueryDispatcher-.->di2[DiMiddleware]-.->QueryHandler;\n\n``DiMiddleware`` initializes handlers and injects dependencies for them, you can just send a command with the data you need\n\nWhy ``didiator``?\n=================\n\n- Easy dependency injection to your business logic\n- Separating dependencies from your controllers. They can just parse external requests and interact with the ``Mediator``\n- CQRS\n- Flexible configuration\n- Middlewares support\n\nWhy not?\n========\n\n- You don\'t need it\n- Maybe too low coupling: navigation becomes more difficult\n- Didiator is in beta now\n- No support for synchronous handlers\n\n',
    'author': 'SamWarden',
    'author_email': 'SamWardenSad@gmail.com',
    'maintainer': 'SamWarden',
    'maintainer_email': 'SamWardenSad@gmail.com',
    'url': 'https://github.com/SamWarden/didiator',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
