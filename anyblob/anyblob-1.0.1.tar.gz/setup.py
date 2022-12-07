# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anyblob']

package_data = \
{'': ['*']}

install_requires = \
['pooch>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'anyblob',
    'version': '1.0.1',
    'description': '',
    'long_description': '# anyblob\n\nSummon binary objects into your local file system by their SHA-256 hashes.\n',
    'author': 'Danilo Horta',
    'author_email': 'danilo.horta@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
