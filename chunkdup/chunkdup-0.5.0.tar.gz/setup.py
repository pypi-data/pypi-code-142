# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chunkdup']

package_data = \
{'': ['*']}

install_requires = \
['chunksum']

entry_points = \
{'console_scripts': ['chunkdiff = chunkdup.chunkdiff:main',
                     'chunkdup = chunkdup.chunkdup:main']}

setup_kwargs = {
    'name': 'chunkdup',
    'version': '0.5.0',
    'description': 'Find (partial content) duplicate files.',
    'long_description': '# chunkdup\n\nFind (partial content) duplicate files using [chunksum](https://github.com/xyb/chunksum) outputs.\n\n[![test](https://github.com/xyb/chunkdup/actions/workflows/test.yml/badge.svg)](https://github.com/xyb/chunkdup/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/xyb/chunkdup/branch/main/graph/badge.svg?token=TVFUKMLFMX)](https://codecov.io/gh/xyb/chunkdup)\n[![Maintainability](https://api.codeclimate.com/v1/badges/0935f557916da1fdcddb/maintainability)](https://codeclimate.com/github/xyb/chunkdup/maintainability)\n[![Latest version](https://img.shields.io/pypi/v/chunkdup.svg)](https://pypi.org/project/chunkdup/)\n[![Support python versions](https://img.shields.io/pypi/pyversions/chunkdup)](https://pypi.org/project/chunkdup/)\n\n```\nusage: chunkdup [-h] [chunksums1] [chunksums2]\n\nFind (partial content) duplicate files.\n\npositional arguments:\n  chunksums1  path to chunksums\n  chunksums2  path to chunksums\n\noptional arguments:\n  -h, --help  show this help message and exit\n\nExamples:\n\n  $ chunksum dir1/ -f chunksums.dir1\n  $ chunksum dir2/ -f chunksums.dir2\n  $ chunkdup chunksums.dir1 chunksums.dir2\n```\n\n```\nusage: chunkdiff [-h] [-b BAR] [-w BARWIDTH] [-n] [-s CHUNKSUMS]\n                 [file1] [file2]\n\nShow the difference of two files.\n\npositional arguments:\n  file1                 path to file\n  file2                 path to file\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -b BAR, --bar BAR     the style of bar. default: oneline\n  -w BARWIDTH, --barwidth BARWIDTH\n                        the width of bar. default: 40\n  -n, --nocolor         do not colorize output. default: False\n  -s CHUNKSUMS, --chunksums CHUNKSUMS\n                        path to chunksums file\n\nExamples:\n\n  $ chunksum dir1/ -f chunksums.dir1\n  $ chunksum dir2/ -f chunksums.dir2\n\n  $ chunkdiff chunksums.dir1 chunksums.dir2 dir1/file1 dir2/file2\n\n  $ chunkdiff chunksums chunksums ./file1 ./file2\n```\n',
    'author': 'Xie Yanbo',
    'author_email': 'xieyanbo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyb/chunkdup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
