# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xenosite']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'rich>=12.6.0,<13.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['xenosite = xenosite.__main__:app']}

setup_kwargs = {
    'name': 'xenosite',
    'version': '0a1',
    'description': '',
    'long_description': 'This is the core package for XenoSite.\n\nThis package primarily serves as a namespace package for the xenosite family of packages, while also including an extensible command line interface. All useful functionality requires installing one of the XenoSite subpackages.',
    'author': 'S. Joshua Swamidass',
    'author_email': 'swamidass@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
