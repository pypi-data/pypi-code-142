# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kedro_azureml', 'kedro_azureml.distributed']

package_data = \
{'': ['*']}

install_requires = \
['adlfs>=2022.2.0',
 'azure-ai-ml>=1.2.0',
 'azure-core>=1.26.1',
 'backoff>=2.2.1,<3.0.0',
 'cloudpickle>=2.1.0,<3.0.0',
 'kedro>=0.18.2,<0.19',
 'pydantic>=1.9.1,<1.10.0']

extras_require = \
{'mlflow': ['azureml-mlflow>=1.42.0', 'mlflow>=1.27.0,<2.0.0']}

entry_points = \
{'kedro.project_commands': ['azureml = kedro_azureml.cli:commands']}

setup_kwargs = {
    'name': 'kedro-azureml',
    'version': '0.3.3',
    'description': 'Kedro plugin with Azure ML Pipelines support',
    'long_description': '# Kedro Azure ML Pipelines plugin\n\n[![Python Version](https://img.shields.io/pypi/pyversions/kedro-azureml)](https://github.com/getindata/kedro-azureml)\n[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![SemVer](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/)\n[![PyPI version](https://badge.fury.io/py/kedro-azureml.svg)](https://pypi.org/project/kedro-azureml/)\n[![Downloads](https://pepy.tech/badge/kedro-azureml)](https://pepy.tech/project/kedro-azureml)\n\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=getindata_kedro-azureml&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=getindata_kedro-azureml)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=getindata_kedro-azureml&metric=coverage)](https://sonarcloud.io/summary/new_code?id=getindata_kedro-azureml)\n[![Documentation Status](https://readthedocs.org/projects/kedro-vertexai/badge/?version=latest)](https://kedro-azureml.readthedocs.io/en/latest/?badge=latest)\n\n<p align="center">\n  <a href="https://getindata.com/solutions/ml-platform-machine-learning-reliable-explainable-feature-engineering"><img height="150" src="https://getindata.com/img/logo.svg"></a>\n  <h3 align="center">We help companies turn their data into assets</h3>\n</p>\n\n## About\nFollowing plugin enables running Kedro pipelines on Azure ML Pipelines service.\n\nWe support 2 native Azure Machine Learning types of workflows:\n* For Data Scientists: fast, iterative development with code upload \n* For MLOps: stable, repeatable workflows with Docker \n\n## Documentation \n\nFor detailed documentation refer to https://kedro-azureml.readthedocs.io/\n\n## Usage guide\n\n```\nUsage: kedro azureml [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -e, --env TEXT  Environment to use.\n  -h, --help      Show this message and exit.\n\nCommands:\n  compile  Compiles the pipeline into YAML format\n  init     Creates basic configuration for Kedro AzureML plugin\n  run      Runs the specified pipeline in Azure ML Pipelines\n```\n\n## Quickstart\nFollow **quickstart** section on [kedro-azureml.readthedocs.io](https://kedro-azureml.readthedocs.io/) to get up to speed with plugin usage or watch the video below\n\n<a href="https://bit.ly/kedroazureml">\n    <img src="./docs/images/tutorial-video-yt.jpg" alt="Kedro Azure ML video tutorial" title="Kedro Azure ML video tutorial" />\n</a>\n\n',
    'author': 'marcin.zablocki',
    'author_email': 'marcin.zablocki@getindata.com',
    'maintainer': 'GetInData MLOPS',
    'maintainer_email': 'mlops@getindata.com',
    'url': 'https://github.com/getindata/kedro-azureml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
