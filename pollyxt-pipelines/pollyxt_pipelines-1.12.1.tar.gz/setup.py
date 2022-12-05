# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pollyxt_pipelines',
 'pollyxt_pipelines.locations',
 'pollyxt_pipelines.polly_to_scc',
 'pollyxt_pipelines.qc_eldec',
 'pollyxt_pipelines.radiosondes',
 'pollyxt_pipelines.scc_access']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'cleo>=0.8.1,<0.9.0',
 'matplotlib>=3.6.0,<4.0.0',
 'netCDF4>=1.5.7,<2.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['pollyxt_pipelines = pollyxt_pipelines:main']}

setup_kwargs = {
    'name': 'pollyxt-pipelines',
    'version': '1.12.1',
    'description': 'Tools and scripts related to the automated processing of PollyXT files',
    'long_description': 'None',
    'author': 'Thanasis Georgiou',
    'author_email': 'ageorgiou@noa.gr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
