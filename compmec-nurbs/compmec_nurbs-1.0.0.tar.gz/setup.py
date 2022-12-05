# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nurbs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'compmec-nurbs',
    'version': '1.0.0',
    'description': '',
    'long_description': "[![PyPI Version][pypi-image]][pypi-url]\n[![Build Status][build-image]][build-url]\n[![Code Coverage][coverage-image]][coverage-url]\n[![][versions-image]][versions-url]\n\n# Nurbs\n\nThis repository contains code for inteporlate functions using B-Splines and Nurbs.\n\n\n#### Features\n\n* Basic Functions\n    * Spline ```N```\n    * Rational ```R```\n    * Derivative\n* Curves\n    * Spline\n    * Rational\n* Knot operations\n    * Insertion\n    * Removal\n* Degree operations\n    * Degree elevation\n    * Degree reduction\n\n## Install\n\nThis library is available in [PyPI][pypilink]. To install it\n\n```\npip install compmec-nurbs\n```\n\n## Documentation\n\nIn progress\n\n\n# FAQ\n\n#### Must I learn the theory to use it?\n\nNo! Just see the examples and it will be fine\n\n#### Can I understand the code here?\n\nYes! The easier way is to look up the **python notebook** which contains the theory along examples\n\n#### Is this code efficient?\n\nNo. It's written in python and the functions were made for easy understanding, not for performance.\nThat means: It's not very fast, but it works fine.\n\n\n## Contribute\n\nPlease use the [Issues][issueslink] or refer to the email ```compmecgit@gmail.com```\n\n<!-- Badges: -->\n\n[pypi-image]: https://img.shields.io/pypi/v/compmec-nurbs\n[pypi-url]: https://pypi.org/project/compmec-nurbs/\n[build-image]: https://github.com/compmec/nurbs/actions/workflows/build.yaml/badge.svg\n[build-url]: https://github.com/compmec/nurbs/actions/workflows/build.yaml\n[coverage-image]: https://codecov.io/gh/compmec/nurbs/branch/main/graph/badge.svg\n[coverage-url]: https://codecov.io/gh/compmec/nurbs/\n[versions-image]: https://img.shields.io/pypi/pyversions/compmec-nurbs.svg?style=flat-square\n[versions-url]: https://pypi.org/project/compmec-nurbs/\n[pypilink]: https://pypi.org/project/compmec-nurbs/\n[issueslink]: https://github.com/compmec/nurbs/issues\n",
    'author': 'Carlos Adir',
    'author_email': 'carlos.adir@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
