# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sitzungsdienst', 'sitzungsdienst.models']

package_data = \
{'': ['*']}

install_requires = \
['ics>=0.7,<0.8', 'pypdf2==2.0.0']

setup_kwargs = {
    'name': 'sitzungsdienst',
    'version': '2.2.0',
    'description': 'Handles weekly assignment PDFs as exported by "web.sta"',
    'long_description': "# sitzungsdienst\n[![License](https://badgen.net/badge/license/GPL/blue)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/LICENSE) [![PyPI](https://badgen.net/pypi/v/sitzungsdienst)](https://pypi.org/project/sitzungsdienst) [![Coverage](https://badgen.net/badge/coverage/100/cyan)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/COVERAGE) [![Build](https://ci.codeberg.org/api/badges/S1SYPHOS/sitzungsdienst/status.svg)](https://codeberg.org/S1SYPHOS/sitzungsdienst/issues)\n\nA simple Python utility for working with weekly assignment PDFs as exported by [`web.sta`](https://www.dvhaus.de/leistungen/web.sta).\n\n\n## Getting started\n\nSimply install all dependencies inside a virtual environment to get started:\n\n```bash\n# Set up & activate virtualenv\nvirtualenv -p python3 venv\n\n# shellcheck disable=SC1091\nsource venv/bin/activate\n\n# Install dependencies, either ..\n# (1) .. from PyPi (stable)\npython -m pip install sitzungsdienst\n\n# (2) .. from repository (dev)\npython -m pip install --editable .\n```\n\n\n## Usage\n\nUsing this library is straightforward:\n\n```python\nfrom sitzungsdienst import StA\n\n# Pass file path (or its stream) & retrieve data\ncourt_dates, express_dates = StA.run('path/to/file.pdf')\n\n# Use a subset by filtering it\nfiltered_court = court_dates.filter(['alice', 'bob'])\nfiltered_express = express_dates.filter('john')\n```\n\nIf you want to see it in action, head over to the [`sitzungsapp`](https://codeberg.org/S1SYPHOS/sitzungsapp)!\n\n\n**Happy coding!**\n",
    'author': 'Digitalbüro',
    'author_email': 'pypi@digitalbuero.eu',
    'maintainer': 'Martin Folkers',
    'maintainer_email': 'hello@twobrain.io',
    'url': 'https://digitalbuero.eu',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
