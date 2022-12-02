# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spotify_interlude']

package_data = \
{'': ['*']}

install_requires = \
['pycaw>=20220416,<20220417',
 'pydantic>=1.9.1,<2.0.0',
 'pywin32>=305,<306',
 'spotipy>=2.20.0,<3.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['interlude = spotify_interlude.cli:app']}

setup_kwargs = {
    'name': 'spotify-interlude',
    'version': '0.1.0',
    'description': 'Pause Spotify playback when other apps start making noise',
    'long_description': 'None',
    'author': 'Hubert Bereś',
    'author_email': 'h.beres@hotmail.com',
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
