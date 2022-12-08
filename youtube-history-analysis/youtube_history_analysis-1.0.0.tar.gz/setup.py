# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['youtube_history_analysis']

package_data = \
{'': ['*'], 'youtube_history_analysis': ['outputs/*']}

install_requires = \
['google-api-python-client>=2.68.0,<3.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'youtube-history-analysis',
    'version': '1.0.0',
    'description': 'See how your YouTube interests evolved over time',
    'long_description': "# youtube-history-analysis\n\n[![PyPI](https://img.shields.io/pypi/v/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![PyPI - License](https://img.shields.io/pypi/l/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://armanckeser.github.io/youtube-history-analysis](https://armanckeser.github.io/youtube-history-analysis)\n\n**Source Code**: [https://github.com/armanckeser/youtube-history-analysis](https://github.com/armanckeser/youtube-history-analysis)\n\n**PyPI**: [https://pypi.org/project/youtube-history-analysis/](https://pypi.org/project/youtube-history-analysis/)\n\n---\n\nSee how your YouTube interests evolved over time\n\n## Installation\n\n```sh\npip install youtube-history-analysis\n```\n\n## Usage\n```sh\npython -m youtube_history_analysis $API_KEY $WATCH_HISTORY_JSON_PATH\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.9+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/armanckeser/youtube-history-analysis/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/armanckeser/youtube-history-analysis/releases) and publish it. When\n a release is published, it'll trigger [release](https://github.com/armanckeser/youtube-history-analysis/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n",
    'author': 'Armanc Keser',
    'author_email': 'armanckeser@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://armanckeser.github.io/youtube-history-analysis',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<3.12',
}


setup(**setup_kwargs)
