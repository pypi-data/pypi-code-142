# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stoppy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stoppy',
    'version': '1.0.1',
    'description': 'A precise and lightweight stopwatch built on top of `perf_counter`. Stopwatch can be used as a direct replacement for `perf_counter` that returns absolute timing starting from zero.',
    'long_description': '# stoppy ⏱\n\nA precise and lightweight stopwatch built on top of `perf_counter`. Stopwatch can be used as a direct replacement for `perf_counter` that returns absolute timing starting from zero.\n\nThe stopwatch can optionally be started automatically by calling `time` instead of `start`, which can streamline usage when polling the time repeatedly.\n\n## Installation\n\nInstall from [PyPI](https://pypi.org/project/stopwatch/) via:\n\n```shell\npip install stoppy\n```\n\n## Usage\n\nBasic usage is as follows:\n\n```python\nfrom time import sleep\nfrom stoppy import Stopwatch\n\nwith Stopwatch(start=True) as stopwatch:\n    sleep(0.1)\n    stopwatch.stop()\n    print(stopwatch.time())\n    stopwatch.reset()\n```\n\nIt can also be used as a direct replacement for `perf_counter` with absolute timing starting from zero.\n\n```python\nfrom stoppy import Stopwatch\n\nwith Stopwatch() as stopwatch:\n    # Calling `stopwatch.time(True)` is equivalent to calling `perf_counter`, but starts from exactly zero\n    print(stopwatch.time(True))\n```\n\nFor all usage examples see [examples/](https://github.com/morefigs/stoppy/tree/main/examples).\n',
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
