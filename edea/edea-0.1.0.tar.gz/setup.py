# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edea',
 'edea.draw',
 'edea.draw.schematic',
 'edea.draw.themes',
 'edea.types',
 'edea.types.schematic']

package_data = \
{'': ['*'], 'edea.draw.themes': ['json/*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'numpy>=1.21.4',
 'pydantic>=1.10.2,<2.0.0',
 'pyvips>=2.2.1,<3.0.0',
 'svg.py>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'edea',
    'version': '0.1.0',
    'description': 'KiCAD file format parser and tools',
    'long_description': 'None',
    'author': 'Elen Eisendle',
    'author_email': 'ln@calcifer.ee',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
