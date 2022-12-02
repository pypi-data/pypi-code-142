# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_snowflake', 'tap_snowflake.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.14.0,<0.15.0',
 'snowflake-connector-python>=2.8.0,<3.0.0',
 'snowflake-sqlalchemy>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['tap-snowflake = tap_snowflake.tap:TapSnowflake.cli']}

setup_kwargs = {
    'name': 'meltanolabs-tap-snowflake',
    'version': '0.0.7',
    'description': '`tap-snowflake` is a Singer tap for Snowflake, built with the Meltano SDK for Singer Taps.',
    'long_description': 'None',
    'author': 'Ken Payne',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
