# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['genomic_references']

package_data = \
{'': ['*']}

install_requires = \
['dataclass-type-validator>=0.1.2,<0.2.0', 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'genomic-references',
    'version': '1.1.0',
    'description': 'OncoDNA library to handle genomic reference directory',
    'long_description': 'None',
    'author': 'Benoitdw',
    'author_email': 'bw@oncodna.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
