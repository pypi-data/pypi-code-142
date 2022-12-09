# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gewv_timeseries_client']

package_data = \
{'': ['*']}

install_requires = \
['ciso8601>=2.2.0,<3.0.0',
 'influxdb-client>=1.32.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'urllib3>=1.26.12,<2.0.0']

setup_kwargs = {
    'name': 'gewv-timeseries-client',
    'version': '0.5.9',
    'description': 'Client to read & write data from timeseries db.',
    'long_description': '# GEWV Timeseries Client\n\nThis client is a abstraction of the offical Influx-Client to get and write points to our Influx-TimeseriesDB.\n\n## Installation\n\n```\npip install gewv-timeseries-client\n```\n\n## Development\n\nFor testing you can install all deps and start the module with that commands.\n\n```\npoetry install\npoetry shell\npython examples/read_and_write_data.py\n```\n\n## Plans\n\n- Add more example\n- Add tests\n',
    'author': 'Karl Wolfgang',
    'author_email': 'karl_eugen.wolffgang@tu-dresden.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gewv-tu-dresden/timeseries-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
