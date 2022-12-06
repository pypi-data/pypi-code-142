# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['together_worker', 'together_worker.profiler']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'dacite>=1.6.0,<2.0.0',
 'influxdb-client>=1.34.0,<2.0.0',
 'netifaces>=0.11.0,<0.12.0',
 'pynvml>=11.4.1,<12.0.0',
 'together-web3>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'together-worker',
    'version': '0.1.3',
    'description': '',
    'long_description': '# together_worker\n',
    'author': 'together',
    'author_email': 'together@together.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/together-computer/together_worker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
