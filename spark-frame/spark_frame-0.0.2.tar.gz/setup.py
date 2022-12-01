# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spark_frame',
 'spark_frame.examples',
 'spark_frame.graph_impl',
 'spark_frame.transformations_impl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'spark-frame',
    'version': '0.0.2',
    'description': 'A library containing various utility functions for playing with PySpark DataFrames',
    'long_description': "# Spark-frame\n\n[![PyPI version](https://badge.fury.io/py/spark-frame.svg)](https://badge.fury.io/py/spark-frame)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/spark-frame.svg)](https://pypi.org/project/spark-frame/)\n[![GitHub Build](https://img.shields.io/github/workflow/status/FurcyPin/spark-frame/Build%20and%20Validate)](https://github.com/FurcyPin/spark-frame/actions)\n[![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=coverage)](https://sonarcloud.io/component_measures?id=FurcyPin_spark-frame&metric=coverage&view=list)\n[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=bugs)](https://sonarcloud.io/component_measures?metric=reliability_rating&view=list&id=FurcyPin_spark-frame)\n[![SonarCloud Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=FurcyPin_spark-frame&metric=vulnerabilities)](https://sonarcloud.io/component_measures?metric=security_rating&view=list&id=FurcyPin_spark-frame)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/spark-frame)](https://pypi.org/project/spark-frame/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## What is it ?\n\nSpark-frame is a library that brings several utility methods and transformation functions for PySpark DataFrames.\nThese methods were initially part of the [karadoc](https://github.com/FurcyPin/karadoc) project \nused at [Younited](https://medium.com/younited-tech-blog), but they don't rely on karadoc, so it makes more sense \nto keep them as standalone library.\n\nSeveral of these methods were my initial inspiration to make the cousin project \n[bigquery-frame](https://github.com/FurcyPin/bigquery-frame), which is why you will find similar \nmethods in `transformations` and `data_diff` for both `spark_frame` and `bigquery_frame`, except\nthe former runs on PySpark while the latter runs on BigQuery (obviously).\n\n## Installation\n\n[spark-frame is available on PyPi](https://pypi.org/project/spark-frame/).\n\n```bash\npip install spark-frame\n```\n\n\n",
    'author': 'FurcyPin',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FurcyPin/spark-frame',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
