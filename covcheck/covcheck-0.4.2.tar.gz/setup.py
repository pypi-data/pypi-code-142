# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['covcheck', 'covcheck._cli', 'covcheck._parsing']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['covcheck = covcheck._cli.main:run']}

setup_kwargs = {
    'name': 'covcheck',
    'version': '0.4.2',
    'description': 'Code coverage validation',
    'long_description': '<div align="center">\n  <img src="https://storage.googleapis.com/hume-public-logos/covcheck/covcheck-dino-banner.png">\n  <h1>covcheck</h1>\n\n  <p>\n    <strong>Command-line tool for code coverage validation</strong>\n  </p>\n\n  <br>\n  <div>\n    <a href="https://badge.fury.io/py/covcheck"><img src="https://badge.fury.io/py/covcheck.svg" alt="PyPI"></a>\n    <a href="https://pepy.tech/project/covcheck"><img src="https://pepy.tech/badge/covcheck" alt="Downloads"></a>\n    <a href="https://github.com/HumeAI/covcheck/actions/workflows/ci.yml"><img src="https://github.com/HumeAI/covcheck/actions/workflows/ci.yaml/badge.svg" alt="CI"></a>\n  </div>\n  <br>\n</div>\n\n## About\n\n`covcheck` is intended to be used in conjunction with [coverage.py](https://coverage.readthedocs.io/), which already has support for `pytest`, `unittest`, and `nosetest`. All you have to do is point `covcheck` to the `coverage.xml` file produced when running your tests.\n\nFor more information on how to use `covcheck` please check out the [official docs page](https://humeai.github.io/covcheck).\n',
    'author': 'Hume AI Dev',
    'author_email': 'dev@hume.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/HumeAI/covcheck',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
