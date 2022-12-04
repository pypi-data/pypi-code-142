# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['roe_teer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'roe-teer',
    'version': '0.1.0',
    'description': '',
    'long_description': '# RoeTeer\n\nRoeTeer is a simple router using radix trees.\n\n> Big thanks to [DreamTexX](https://github.com/DreamTexX) who coded most of this.\n\n',
    'author': 'cheetahbyte',
    'author_email': '40123243+cheetahbyte@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
