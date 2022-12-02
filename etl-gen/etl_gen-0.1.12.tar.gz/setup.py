# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['etl_gen', 'etl_gen.commands']

package_data = \
{'': ['*'],
 'etl_gen': ['resources/*',
             'resources/address_data_xml/*',
             'resources/html_list/*']}

install_requires = \
['faker>=15.3.3,<16.0.0',
 'kafka-python>=2.0.2,<3.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['etl-gen = etl_gen.main:app']}

setup_kwargs = {
    'name': 'etl-gen',
    'version': '0.1.12',
    'description': '',
    'long_description': '',
    'author': 'realdengziqi',
    'author_email': '993396365@qq.com',
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
