# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dash_antd', 'dash_antd.ext']

package_data = \
{'': ['*']}

install_requires = \
['dash>=2.7,<3.0']

setup_kwargs = {
    'name': 'dash-antd',
    'version': '0.1.5',
    'description': 'Ant Design components for Plotly Dash',
    'long_description': '# Dash Ant Design Components\n\n<p align="center">\n<a href="https://github.com/roeap/dash-ant-design-components/actions"><img alt="Actions Status" src="https://github.com/roeap/dash-ant-design-components/actions/workflows/test.yaml/badge.svg"></a>\n<a href="https://codecov.io/gh/roeap/dash-ant-design-components">\n  <img src="https://codecov.io/gh/roeap/dash-ant-design-components/branch/main/graph/badge.svg?token=DNVIU3FXL5"/>\n</a>\n<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>\n<a href="https://pypi.org/project/dash-antd/"><img alt="PyPI" src="https://img.shields.io/pypi/v/dash-antd"></a>\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\nAnt Design components for Plotly Dash.\n\n## Install\n\nto install in your python environment.\n\n```shell\npoetry add dash-antd\n```\n\nor via pip.\n\n```shell\npip install dash-antd\n```\n\n## Development\n\nWe use [just](https://github.com/casey/just) as command runner, if you prefer not to install\njust, have a look at the `justfile` for detailed commands.\n\nTo manage python dependencies, we utilize [poetry](python-poetry.org/).\n\n### Getting Started\n\nInstall python and node dependencies.\n\n```sh\njust install\n```\n\nBuild the Dash packages.\n\n```sh\njust build\n```\n\nSee all commands with `just -l`\n\n### Example app\n\nAn example app is contained in the `example` folder. To run it execute:\n\n```sh\njust run\n```\n',
    'author': 'Robert Pack',
    'author_email': 'robstar.pack@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/roeap/dash-ant-design-components',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
