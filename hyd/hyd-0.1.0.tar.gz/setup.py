# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyd']

package_data = \
{'': ['*']}

install_requires = \
['moviepy>=1.0.3,<2.0.0', 'pytube>=12.1.0,<13.0.0']

entry_points = \
{'console_scripts': ['hyd = hyd.HaukursYouTubeDownloader:main']}

setup_kwargs = {
    'name': 'hyd',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'haukurlogi',
    'author_email': 'haukurlogi2008@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
