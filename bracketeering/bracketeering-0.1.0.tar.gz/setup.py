# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bracketeering', 'bracketeering.data']

package_data = \
{'': ['*']}

install_requires = \
['clearcut>=0.2.1,<0.3.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'bracketeering',
    'version': '0.1.0',
    'description': 'Library to calculate withholdings based on tiered brackets',
    'long_description': '# `bracketeering`',
    'author': 'Austin Howard',
    'author_email': 'austin@ahoward.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/austin1howard/bracketeering',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
