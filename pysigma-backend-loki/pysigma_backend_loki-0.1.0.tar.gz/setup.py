# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigma', 'sigma.backends.loki', 'sigma.pipelines.loki']

package_data = \
{'': ['*']}

install_requires = \
['pysigma-pipeline-sysmon>=1.0.1,<2.0.0', 'pysigma>=0.8.9,<0.9.0']

setup_kwargs = {
    'name': 'pysigma-backend-loki',
    'version': '0.1.0',
    'description': 'pySigma Loki backend',
    'long_description': 'None',
    'author': 'Nick Moore',
    'author_email': 'nicholas.moore@grafana.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/grafana/pySigma-backend-loki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
