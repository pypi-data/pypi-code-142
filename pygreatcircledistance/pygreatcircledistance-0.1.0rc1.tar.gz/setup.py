# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pygreatcircledistance']
setup_kwargs = {
    'name': 'pygreatcircledistance',
    'version': '0.1.0rc1',
    'description': 'Calculate the distance between two GPS coordinates in meters',
    'long_description': 'pyGreatCircleDistance\n=====================\n\nCalculate the distance between two GPS coordinates in meters\n\n[![PyPI](https://img.shields.io/pypi/v/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)\n[![PyPI](https://img.shields.io/pypi/dm/pyGreatCircleDistance.svg)](https://pypi.python.org/pypi/pyGreatCircleDistance)\n[![Docker Pulls](https://img.shields.io/docker/pulls/shpaker/pyGreatCircleDistance)](https://hub.docker.com/r/shpaker/pyGreatCircleDistance)\n[![PyPI](https://img.shields.io/badge/code%20style-black-000000.svg)](href="https://github.com/psf/black)\n\nInstallation\n------------\n\n```\npip install pyGreatCircleDistance -U\n```\n\nExample\n-------\n\n```\n>>> from_coords = (77.1539, -120.398)\n>>> to_coords = (77.1804, 129.55)\n>>> dist = calc_distance(from_coords, to_coords)\n>>> print(dist)\n2332668.5392066096\n```\n',
    'author': 'Aleksandr Shpak',
    'author_email': 'shpaker@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shpaker/pyGreatCircleDistance',
    'py_modules': modules,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
