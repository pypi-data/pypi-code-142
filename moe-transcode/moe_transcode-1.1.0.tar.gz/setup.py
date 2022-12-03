# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moe_transcode']

package_data = \
{'': ['*']}

install_requires = \
['moe>=1.5.1,<2.0.0']

entry_points = \
{'moe.plugins': ['transcode = moe_transcode']}

setup_kwargs = {
    'name': 'moe-transcode',
    'version': '1.1.0',
    'description': 'Plugin for Moe to transcode music.',
    'long_description': '#########\nTranscode\n#########\nThis is a plugin for Moe that provides functionality for transcoding music.\n\nCurrently only flac -> mp3 [v0, v2, 320] is supported.\n\nCheck out the `full documentation <https://moe-transcode.readthedocs.io/en/latest/>`_ for more info.\n',
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
