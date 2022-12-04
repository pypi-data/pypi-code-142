# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aocutil']

package_data = \
{'': ['*']}

install_requires = \
['pyquery>=1.4.3,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'aocutil',
    'version': '0.1.0',
    'description': 'Utility library for Advent of Code (https://adventofcode.com)',
    'long_description': '# AoC Utils\n\nThis small library can be used for the yearly Advent of Code\n(https://adventofcode.com) challenge. It automates the retrieval of puzzle input\nand submission.\n\n# Usage\n\n``` python\nfrom aocutil import Aoc\n\n# Initialize for year 2022, day 1 with session id 53616c746\n#\n# Everything here is optional. If left out year and day is determined\n# from the current date -- be aware that your code is non-repeatable if year \n# and date is not specified.\n# Session id is read from `${HOME}/.config/aocutil/session_id` if not specified.\naoc = Aoc(year=2022, day=1, session_id="53616c746")\n\n# Retrieve input and split into list of lines\n#\n# You can also retrieve the content as a string with `aoc.input().read()`.\npuzzle = aoc.input().lines()\n\n# solve the puzzle (your implementation)\nsolution = solve(puzzle)\n\n# Submit the solution for level 1\n#\n# If left out, the level is determined automatically by\n# which level is not solved yet.\naoc.submit(solution, level=1)\n```\n\n# Retrieving the Session ID\n\nA user in Advent of Code submissions and input retrieval is determined by a\nsession id stored in a cookie in the user\'s browser. For this library to work it\nneeds a users session id. The session id can be found by opening your browsers\ndeveloper tools and looking for a cookie named `session`.\n\nYou can either initialize `Aoc` with the token or store it in a file named\n`${HOME}/.config/aocutil/session_id`. I would recommend the latter so you don\'t\naccidentially publish your session id. Note that everyone who gets hold of your\nsession id can impersonate you.\n',
    'author': 'Armin Friedl',
    'author_email': 'dev@friedl.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
