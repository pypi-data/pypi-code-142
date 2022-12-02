# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bgmiget', 'bgmiget.sources']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'dacite>=1.6.0,<2.0.0',
 'fire>=0.4.0,<0.5.0',
 'requests>=2.28.1,<3.0.0',
 'torrentp>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['bgmiget = bgmiget:main']}

setup_kwargs = {
    'name': 'bgmiget',
    'version': '0.1.1',
    'description': 'a way to download anime.',
    'long_description': '# TODO\n\n1. add a command to save the "include/exclude" rule, and the results. The results can be updates with its rules.\n2. add a command to set the save-path. the default save-path is the path you run the script.\n3. add smp support?\n4. add multi-files download support.',
    'author': 'aoout',
    'author_email': 'wuz66280@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
