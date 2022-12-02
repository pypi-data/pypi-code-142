# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uwuify']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['uwuify = uwuify.cli:main']}

setup_kwargs = {
    'name': 'uwuify',
    'version': '1.2.0',
    'description': 'uwuifys text',
    'long_description': '# uwuify\n\n![PyPI - Downloads](https://img.shields.io/pypi/dm/uwuify?style=for-the-badge)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\nCommand line uwuification\n\n# Installation\n```shell\npip install uwuify\n```\n\n# Usage\n```shell\nuwuify hello\n# outputs hewwo in console\n\nuwuify how are you? --smiley --yu\n# outputs how awe yoyu? with a random smiley\n\nuwuify how are you? --smiley --yu --do-stutter\n# outputs h-how awe yoyu? with a random smiley\n# --do-stutter stutters every 4-th word\n```\nor\n```python\nimport uwuify\n\nprint(uwuify.uwu("hello"))\n# hewwo\n\nflags = uwuify.SMILEY | uwuify.YU\nprint(uwuify.uwu("how are you?", flags=flags))\n# how awe yoyu? with a random smiley\n\nflags = uwuify.SMILEY | uwuify.YU | uwuify.STUTTER\nprint(uwuify.uwu("how are you?", flags=flags))\n# h-how awe yoyu? with a random smiley\n```',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarrFox/uwuify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
