# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_dbt']

package_data = \
{'': ['*']}

install_requires = \
['grai-client>=0.1.8,<0.2.0',
 'networkx>=2.8.3,<3.0.0',
 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'grai-source-dbt',
    'version': '0.0.4',
    'description': '',
    'long_description': 'None',
    'author': 'Ian Eaves',
    'author_email': 'ian@grai.io',
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
