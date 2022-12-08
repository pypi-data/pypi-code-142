# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['youtube_history_analysis']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.68.0,<3.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'youtube-history-analysis',
    'version': '1.0.1',
    'description': 'See how your YouTube interests evolved over time',
    'long_description': '# youtube-history-analysis\n\n[![PyPI](https://img.shields.io/pypi/v/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![PyPI - License](https://img.shields.io/pypi/l/youtube-history-analysis?style=flat-square)](https://pypi.python.org/pypi/youtube-history-analysis/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://armanckeser.github.io/youtube-history-analysis](https://armanckeser.github.io/youtube-history-analysis)\n\n**Source Code**: [https://github.com/armanckeser/youtube-history-analysis](https://github.com/armanckeser/youtube-history-analysis)\n\n**PyPI**: [https://pypi.org/project/youtube-history-analysis/](https://pypi.org/project/youtube-history-analysis/)\n\n---\n\nSee how your YouTube interests evolved over time\n\n## Installation\n\n```sh\npython -m venv yt-history-venv\n./yt-history-venv/Scripts/activate\npip install youtube-history-analysis\n```\n\n## Usage\n### Get a YouTube API Key\n\n1. Visit the [Google Cloud Console](https://console.cloud.google.com/).\n2. Click the project drop-down and select or create the project for which you want to add an API key.\n3. Click the hamburger menu and select APIs & Services > Credentials.\n4. On the Credentials page, click Create credentials > API key.\n5. The API key created dialog displays your newly created API key.\n\nRemember to restrict the API key so that it can only be used with certain websites or IP addresses by clicking the Edit button for the API key and then setting the restrictions in the Key restriction section.\n### Get your YouTube History as JSON\n1. Visit [Google Takeout](https://takeout.google.com/) and sign in to your Google account.\n2. Scroll down to the "YouTube" section and click All data included.\n3. Click the Deselect All button and then select the checkbox next to Watch history.\n4. Click the Next button at the bottom of the page.\n5. On the next page, you can select the file type and delivery method for your takeout. Make sure to select JSON as the file type.\n6. Click the Create export button to start the export process.\n\nOnce the export is complete, you will receive an email with a link to download your takeout. The downloaded file will be a zip archive containing your YouTube watch history in JSON format.\n\n```sh\npython -m youtube_history_analysis $API_KEY --watch-history-file-path $WATCH_HISTORY_JSON_PATH\n```\n\nThis will create an `outputs` folder with a bunch of `.csv` files and a few `.png` files. Feel free to use the `.csv` file to do your own analysis.\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.9+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/armanckeser/youtube-history-analysis/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/armanckeser/youtube-history-analysis/releases) and publish it. When\n a release is published, it\'ll trigger [release](https://github.com/armanckeser/youtube-history-analysis/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n',
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
