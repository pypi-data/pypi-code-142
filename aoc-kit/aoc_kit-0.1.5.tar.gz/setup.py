# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aockit']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['aoc-download = aockit.download:main',
                     'aoc-new-day = aockit.template:main']}

setup_kwargs = {
    'name': 'aoc-kit',
    'version': '0.1.5',
    'description': 'Toolkit for advent of code',
    'long_description': "# Advent Of Code kit\n\n## Advent of what?\n\nAdvent of code is a coding competition during december. \n[https://adventofcode.com/about](adventofcode.com).\n\n\n## Purpose\n\nWith this library it should be easy to get started.\n\n## Getting started\n\n### Create a folder for you aoc adventures:\n\n```\nmkdir aoc\ncd aoc\n```\n\n### Install the `aoc-kit` \n\n* Pipenv:\n```\npipenv init\npipenv install aoc-kit\n```\n\n* Poetry:\n```\npoetry init\npoetry add aoc-kit\n```\n\n* System wide\n```\npip install --user aoc-kit\n```\n\n### Create a `.env` file\nWithin your freshly created aoc folder you have to create a `.env` file with a\ncontents like this. You can find the token in your browser. When you are logged\nin you can open the dev tools and find it in the cookies. It is the session\ncookie. Just replace the xxxxxx with your actual token.\n\n`.env`\n```\nAOC_TOKEN=xxxxxx\n```\n\n## Basic usage\n\n### Using the template to get started on a puzzle for a day\n\nSimply run\n```\npoetry run aoc-new-day --year 2022 --day 1\n# or\npipenv run aoc-new-day --year 2022 --day 1\n# or if you have it installed systemwide\naoc-new-day --year 2022 --day 1\n```\nThis will create a file structure like this\n```\naoc/\n  2022/\n    01/\n      main.py\n```\nYou can implement you solution in `main.py` and run it with:\n```\npipenv run python 2022/01/main.py\n# or\npoetry run python 2022/01/main.py\n# or\npython 2022/01/main.py\n```\n\n### `get_input` function\n\nThe `get_input` will return the downloaded (on first call) puzzle input or\nreturn a locally saved puzzle input (on all later calls) of the given day and\nyear.\n\n```\nfrom aockit import get_input\n\ndef process(data):\n    return 'implement me'\n\ndata = get_input(2015, 1)\nresult = process(data)\nprint(result)\n```\n",
    'author': 'Pierre Hoffmeister',
    'author_email': 'pierre.git@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
