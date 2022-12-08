# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlops_utilities']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26,<1.27', 'omegaconf>=2.2,<2.3', 'sagemaker>=2.112,<2.113']

setup_kwargs = {
    'name': 'mlops-utilities',
    'version': '0.1.6',
    'description': '',
    'long_description': "# MLOps Utilities\n\nThis library provides implementation for a few high level operations most commonly occuring in any MLOps workflows built in AWS:\n- Upsert pipeline\n- Run pipeline\n- Deploy model\n    - Create endpoint\n    - Update endpoint\n\n### User guide\n#### Installation\n`pip3 install mlops-utilities`\n#### Project structure conventions\nTODO\n#### Actions\nTODO\n```\nfrom mlops_utilities.actions import run_pipeline\n    \nrun_pipeline(\n  pipeline_name='test_pipeline',\n  execution_name_prefix='test_pipeline',\n  dryrun=True,\n  pipeline_params={}\n)\n```\n",
    'author': 'Provectus Team',
    'author_email': 'mlops@provectus.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
