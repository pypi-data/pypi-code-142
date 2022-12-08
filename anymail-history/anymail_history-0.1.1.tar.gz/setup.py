# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anymail_history', 'anymail_history.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django-anymail>=8.6,<9.0', 'django>=3.2,<5.0']

setup_kwargs = {
    'name': 'anymail-history',
    'version': '0.1.1',
    'description': 'Email History for Django Anymail',
    'long_description': '# anymail-history - Email History for Django Anymail\n\n[![CI tests](https://github.com/pfouque/django-anymail-history/actions/workflows/tox.yml/badge.svg)](https://github.com/pfouque/django-anymail-history/actions/workflows/tox.yml)\n[![Documentation](https://img.shields.io/static/v1?label=Docs&message=READ&color=informational&style=plastic)](https://anymail-history.github.io/anymail-history/)\n[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=informational&style=plastic)](https://github.com/pfouque/anymail-history/)\n\nKeep history of all emails sent by Django Anymail\n\n## Introduction\n\nanymail-history implements models and signals for Django Anymail.\n\n## Resources\n\n-   Full documentation: SOON\n-   Package on PyPI: SOON\n-   Project on Github: [https://github.com/pfouque/django-anymail-history](https://github.com/pfouque/django-anymail-history)\n\n## Features\n\n-   Store sent emails\n-   Store tracking events\n-   Display Admin\n-   html templating\n\n\n## Requirements\n\n-   Django >=3.2\n-   Python >=3.7\n\n## How to\n\n1. Install\n    ```\n    $ pip install "django-anymail[mailgun]" "django-anymail-history"\n    ```\n2. [Configure Anymail](https://github.com/anymail/django-anymail/#anymail-1-2-3)\n    ```\n    INSTALLED_APPS = [\n        # ...\n        "anymail",\n        "anymail_history",\n        # ...\n    ]\n    ```\n3. Enjoy!\n\n## settings\n\nYou can add settings to your project’s settings.py either as a single ANYMAIL dict, or by breaking out individual settings prefixed with ANYMAIL_. So this settings dict:\n\n```\nANYMAIL = {\n    "STORE_HTML": True,\n}\n```\n…is equivalent to these individual settings:\n\n```\nANYMAIL_STORE_HTML = True\n```\n\n### Available settings\n\n-   `ANYMAIL_STORE_FAILED_SEND`: (default: False) Store message even if esp didn\'t returned a message-id.\n-   `ANYMAIL_STORE_HTML`: (default: False) Store html alternatives.\n-   `ANYMAIL_RENDER_HTML`: (default: True) Generate html alternatives.\n\n## Contribute\n\n### Principles\n\n-   Simple for developers to get up-and-running\n-   Consistent style (`black`, `isort`, `flake8`)\n-   Future-proof (`pyupgrade`)\n-   Full type hinting (`mypy`)\n\n### Coding style\n\nWe use [pre-commit](https://pre-commit.com/) to run code quality tools.\n[Install pre-commit](https://pre-commit.com/#install) however you like (e.g.\n`pip install pre-commit` with your system python) then set up pre-commit to run every time you\ncommit with:\n\n```bash\n> pre-commit install\n```\n\nYou can then run all tools:\n\n```bash\n> pre-commit run --all-files\n```\n\nIt includes the following:\n\n-   `poetry` for dependency management\n-   `isort`, `black`, `pyupgrade` and `flake8` linting\n-   `mypy` for type checking\n-   `tox` and Github Actions for builds and CI\n\nThere are default config files for the linting and mypy.\n\n### Tests\n\n#### Tests package\n\nThe package tests themselves are _outside_ of the main library code, in a package that is itself a\nDjango app (it contains `models`, `settings`, and any other artifacts required to run the tests\n(e.g. `urls`).) Where appropriate, this test app may be runnable as a Django project - so that\ndevelopers can spin up the test app and see what admin screens look like, test migrations, etc.\n\n#### Running tests\n\nThe tests themselves use `pytest` as the test runner. If you have installed the `poetry` evironment,\nyou can run them thus:\n\n```\n$ poetry run pytest\n```\n\nor\n\n```\n$ poetry shell\n(anymail-history-py3.10) $ pytest\n```\n\nThe full suite is controlled by `tox`, which contains a set of environments that will format, lint,\nand test against all support Python + Django version combinations.\n\n```\n$ tox\n...\n______________________ summary __________________________\n  fmt: commands succeeded\n  lint: commands succeeded\n  mypy: commands succeeded\n  py37-django32: commands succeeded\n  py37-django40: commands succeeded\n  py37-djangomain: commands succeeded\n  py38-django32: commands succeeded\n  py38-django40: commands succeeded\n  py38-djangomain: commands succeeded\n  py39-django32: commands succeeded\n  py39-django40: commands succeeded\n  py39-djangomain: commands succeeded\n```\n\n#### CI\n\nThere is a `.github/workflows/tox.yml` file that can be used as a baseline to run all of the tests\non Github. This file runs the oldest LTS (3.2), newest (4.1), and head of the main Django branch.\n',
    'author': 'Pascal Fouque',
    'author_email': 'fouquepascal@gmail.com',
    'maintainer': 'Pascal Fouque',
    'maintainer_email': 'fouquepascal@gmail.com',
    'url': 'https://github.com/pfouque/anymail-history',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
