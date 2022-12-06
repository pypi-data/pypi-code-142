# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edsteva',
 'edsteva.io',
 'edsteva.io.synthetic',
 'edsteva.metrics',
 'edsteva.models',
 'edsteva.models.rectangle_function',
 'edsteva.models.rectangle_function.algos',
 'edsteva.models.step_function',
 'edsteva.models.step_function.algos',
 'edsteva.probes',
 'edsteva.utils',
 'edsteva.viz',
 'edsteva.viz.dashboards',
 'edsteva.viz.dashboards.predictor_dashboard',
 'edsteva.viz.plots',
 'edsteva.viz.plots.plot_probe']

package_data = \
{'': ['*']}

install_requires = \
['altair>=4.2,<5.0',
 'ipython>=7.31.0,<8.0.0',
 'koalas>=1.8.2,<2.0.0',
 'loguru==0.6.0',
 'numpy<1.20.0',
 'pandas>=1.3,<2.0',
 'pgpasslib>=1.1.0,<2.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pyarrow==0.16.0',
 'pyspark>=2.4.3,<2.5.0']

setup_kwargs = {
    'name': 'edsteva',
    'version': '0.1.0',
    'description': 'EDS-TeVa provides a set of tools that aims at modeling the adoption over time and across space of the Electronic Health Records.',
    'long_description': '<p align="center">\n<b>DISCLAIMER: </b>EDS-TeVa is intended to be a module of <a href="https://github.com/aphp/EDS-Scikit">EDS-Scikit</a>\n</p>\n\n<div align="center">\n\n<p align="center">\n  <a href="https://aphp.github.io/edsteva/latest/"><img src="https://aphp.github.io/edsteva/latest/assets/logo/edsteva_logo_small.svg" alt="EDS-TeVa"></a>\n</p>\n\n# EDS-TeVa\n\n<p align="center">\n<a href="https://aphp.github.io/edsteva/latest/" target="_blank">\n    <img src="https://img.shields.io/github/workflow/status/aphp/edsteva/Tests%20and%20Linting?label=tests&style=flat-square" alt="Tests">\n</a>\n<a href="https://aphp.github.io/edsteva/latest/" target="_blank">\n    <img src="https://img.shields.io/github/workflow/status/aphp/edsteva/Documentation?label=docs&style=flat-square" alt="Documentation">\n</a>\n<a href="https://pypi.org/project/edsteva/" target="_blank">\n    <img src="https://img.shields.io/pypi/v/edsteva?color=blue&style=flat-square" alt="PyPI">\n</a>\n<a href="https://codecov.io/gh/aphp/edsteva" target="_blank">\n    <img src="https://img.shields.io/codecov/c/github/aphp/edsteva?logo=codecov&style=flat-square" alt="Codecov">\n</a>\n<a href="https://github.com/psf/black" target="_blank">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black">\n</a>\n<a href="https://python-poetry.org/" target="_blank">\n    <img src="https://img.shields.io/badge/reproducibility-poetry-blue" alt="Poetry">\n</a>\n<a href="https://www.python.org/" target="_blank">\n    <img src="https://img.shields.io/badge/python-%3E%3D%203.7.1%20%7C%20%3C%203.8-brightgreen" alt="Supported Python versions">\n</a>\n</p>\n</div>\n\n**Documentation**: <a href="https://aphp.github.io/edsteva/latest/" target="_blank">https://aphp.github.io/edsteva/latest/</a>\n\n**Source Code**: <a href="https://github.com/aphp/edsteva" target="_blank">https://github.com/aphp/edsteva</a>\n\n---\n\nEDS-TeVa provides a set of tools that aims at modeling the adoption over time and across space of the Electronic Health Records.\n\n## Requirements\nEDS-TeVa stands on the shoulders of [Spark 2.4](https://spark.apache.org/docs/2.4.8/index.html) which requires:\n\n- Python ~3.7.1\n- Java 8\n\n## Installation\n\nYou can install EDS-TeVa through ``pip``:\n\n```shell\npip install edsteva\n```\nWe recommend pinning the library version in your projects, or use a strict package manager like [Poetry](https://python-poetry.org/).\n\n```shell\npip install edsteva==0.1.0\n```\n## Example\n\nA scientific paper is currently being written that describes extensively the use of the library on the study of pulmonary embolism of cancer patients.\n\n## Contributing\n\nContributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.\n\n## Acknowledgement\n\nWe would like to thank [Assistance Publique – Hôpitaux de Paris](https://www.aphp.fr/) and [AP-HP Foundation](https://fondationrechercheaphp.fr/) for funding this project.\n',
    'author': 'Adam Remaki',
    'author_email': 'adam.remaki@aphp.fr',
    'maintainer': 'Adam Remaki',
    'maintainer_email': 'adam.remaki@aphp.fr',
    'url': 'https://github.com/aphp/edsteva',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.8.0',
}


setup(**setup_kwargs)
