# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pubhelper']

package_data = \
{'': ['*']}

install_requires = \
['ipy>=1.1,<2.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pubhelper',
    'version': '0.0.19',
    'description': '',
    'long_description': '# PubHelper\n\n- [x] add retry_wraps\n- [x] add request_base\n- [x] add rdm_str\n- [x] add md5\n- [x] add ip_2_int\n- [x] add int_2_ip\n- [x] add SimplePriorityQueue\n- [x] add CacheItem\n- [x] add timethis\n- [x] add with_log\n- [x] add params_check\n',
    'author': 'iulmt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
