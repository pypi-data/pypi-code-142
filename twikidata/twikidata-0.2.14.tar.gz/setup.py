# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twikidata']

package_data = \
{'': ['*']}

install_requires = \
['ergodiff>=0.2.0,<0.3.0', 'grimm>=0.1.0,<0.2.0', 'xmltodict>=0.13.0,<0.14.0']

entry_points = \
{'console_scripts': ['twikidata = twikidata.__main__:main']}

setup_kwargs = {
    'name': 'twikidata',
    'version': '0.2.14',
    'description': '',
    'long_description': '',
    'author': 'Lingxi Li',
    'author_email': 'lilingxi01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
