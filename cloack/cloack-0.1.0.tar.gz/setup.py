# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloack']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cloack',
    'version': '0.1.0',
    'description': 'A Python package to truncate dates and times.',
    'long_description': "# cloack\n\n[![PyPI](https://img.shields.io/pypi/v/cloack?style=flat-square)](https://pypi.python.org/pypi/cloack/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cloack?style=flat-square)](https://pypi.python.org/pypi/cloack/)\n[![PyPI - License](https://img.shields.io/pypi/l/cloack?style=flat-square)](https://pypi.python.org/pypi/cloack/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\nA Python package to truncate dates and times.\n\n## References\n\n- [Wolt Python Package Cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) repo\n- [Delorean](https://delorean.readthedocs.io/en/latest/) package\n\n## Development\n\n- `poetry install`\n- `poetry run isort .` or `poetry run isort . --verbose`\n- `poetry run black .` or `poetry run black . --verbose`\n- [Add an entry](https://github.com/mschmieder/python-kacl#add-an-entry-to-an-unreleased-section) to the `CHANGELOG.md` file and manually save it in VS Code to format it\n- `poetry run kacl-cli verify` or `poetry run kacl-cli verify --json`\n- `poetry run pytest` or `poetry run pytest --verbose`\n\n## Deployment\n\n- `poetry version patch` or `poetry version minor`\n- `poetry run kacl-cli release $(poetry version --short) --modify` and manually save the `CHANGELOG.md` file in VS Code to format it\n\n## Notes\n\n- [cruft](https://cruft.github.io/cruft/):\n  - Alternative to Cookiecutter\n  - cruft uses Cookiecutter as the template engine\n- [pytest-github-actions-annotate-failures](https://github.com/utgwkk/pytest-github-actions-annotate-failures)\n- [flake8-logging-format](https://github.com/globality-corp/flake8-logging-format)\n- Poetry:\n  - `poetry --version`\n  - Update Poetry: `poetry self update` or `curl -sSL https://install.python-poetry.org | python3 - --uninstall` + `curl -sSL https://install.python-poetry.org | python3 -`\n  - `curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0`\n  - Check the current configuration: `poetry config --list`\n  - `poetry config virtualenvs.in-project true --local`\n  - `poetry config virtualenvs.in-project --unset`\n  - `poetry new cloack`\n  - Check `poetry-core` version: `poetry about`\n  - `poetry shell`\n  - `poetry publish --help`\n- `poetry run black --help`\n- `poetry run kacl-cli --help`\n- `poetry run kacl-cli add --help`\n- `poetry run kacl-cli add added 'Boilerplate to create a Python package.' --modify`\n- `poetry run kacl-cli new` or `poetry run kacl-cli new | pbcopy`\n  - https://github.com/mschmieder/python-kacl/blob/v0.2.24/kacl/document.py#L426\n- https://python-poetry.org/docs/configuration/#local-configuration\n- GitHub Actions:\n  - [Relies-on](https://github.com/hadialqattan/relies-on)\n  - [Detect and Tag New Version](https://github.com/salsify/action-detect-and-tag-new-version)\n  - [actionlint](https://github.com/rhysd/actionlint):\n    - Online: https://rhysd.github.io/actionlint/\n    - https://github.com/rhysd/actionlint/blob/main/docs/install.md\n    - `brew install actionlint` + `actionlint --help` + `actionlint .github/workflows/*.yml` or `actionlint -verbose .github/workflows/*.yml`\n",
    'author': 'João Palmeiro',
    'author_email': 'jm.palmeiro@campus.fct.unl.pt',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/joaopalmeiro/cloack',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
