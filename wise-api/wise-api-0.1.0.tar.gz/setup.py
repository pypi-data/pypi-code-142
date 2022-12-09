# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wise_api']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.16.0,<4.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'wise-api',
    'version': '0.1.0',
    'description': 'Python API client for the Wise API',
    'long_description': '# wise-api-client\n\nA Python client for the Wise API.\n',
    'author': 'Jerome Leclanche',
    'author_email': 'jerome@leclan.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
