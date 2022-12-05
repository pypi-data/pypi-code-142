# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stoppy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stoppy',
    'version': '1.0.0',
    'description': 'A precise stopwatch built on top of perf_counter.',
    'long_description': '# stoppy ⏱\n\nA precise stopwatch built on top of `perf_counter`, which \n\nThe stopwatch can optionally be started automatically by calling `time` instead of `start`, which can streamline usage when polling the time repeatedly.\n\n## Installation\n\nInstall from [PyPI](https://pypi.org/project/stopwatch/) via:\n\n```shell\npip install stoppy\n```\n\n## Usage\n\nBasic usage is as follows:\n\n```python\nfrom time import sleep\nfrom stoppy import Stopwatch\n\nstopwatch = Stopwatch(start=True)\nsleep(1)\nstopwatch.stop()\nprint(stopwatch.time())\nstopwatch.reset()\n```\n\nFor more usage examples see [examples/](examples).\n',
    'author': 'morefigs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/morefigs/stoppy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
