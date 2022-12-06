# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcaflow_plugin_template_python']

package_data = \
{'': ['*']}

install_requires = \
['arcaflow-plugin-sdk==0.9.0']

setup_kwargs = {
    'name': 'arcaflow-plugin-template-python',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Arcalot',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
