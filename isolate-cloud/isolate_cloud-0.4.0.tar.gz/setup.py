# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['isolate_cloud', 'isolate_cloud.auth']

package_data = \
{'': ['*']}

install_requires = \
['auth0-python>=3.24.0,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'typer>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'isolate-cloud',
    'version': '0.4.0',
    'description': 'SDK and cli for the fal isolate Cloud service',
    'long_description': '',
    'author': 'Features & Labels',
    'author_email': 'hello@fal.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
