# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['farmworld',
 'farmworld.const',
 'farmworld.env',
 'farmworld.geojson',
 'farmworld.geojson.util',
 'farmworld.renderer',
 'farmworld.types']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'gym==0.21.0',
 'nvidia-cudnn-cu11==8.6.0.163',
 'pillow==9.3.0',
 'polygenerator>=0.2.0,<0.3.0',
 'pygame>=2.1.2,<3.0.0',
 'sb3-contrib>=1.6.2,<2.0.0',
 'stable-baselines3[extra]>=1.6.2,<2.0.0']

setup_kwargs = {
    'name': 'farmworld',
    'version': '0.0.3',
    'description': 'Reinforcement Learning for Agriculture',
    'long_description': '# FarmWorld\n\nA reinforcement learning library for agriculture.\n\n# HOWTO\n\n```python\npip install farmworld\n```\n\n# Install from source\n\n```\nmake venv\nmake install\n```\n\n# Build/Publish\n\nPut a new release on Github\n\n```shell\npoetry build\npoetry publish\n```\n\n# Test\n\n```python\nPYTHONPATH=. python test/test_env.py\n```\n\n# Current Status\n\nDQN basically solves it after 100k steps.\n\n* Normalized the easy way using vecnormalize.\n* Added a zeroth action and trimmed the action space a bit\n\n# TODO\n\n* complicate the problem! multiple crops, and they need to start dieing off at some point\n\n# make env realistic -- add different plants\n# fix planting density\n# add different plants which have different maturities, weather needs etc. \n# plus weather forecast, soil quality(split into attributes)',
    'author': 'Tom Grek',
    'author_email': 'tom.grek@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tomgrek/farmworld',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
