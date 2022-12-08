# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['esetconnect', 'esetconnect.models', 'esetconnect.urls']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'esetconnect',
    'version': '0.1.0',
    'description': '',
    'long_description': '# ESET Connect\n\n## API Docs\nhttp://epcpublicapi-test.westeurope.cloudapp.azure.com/swagger/\n\n',
    'author': 'Donny Maasland',
    'author_email': 'donny@unauthorizedaccess.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
