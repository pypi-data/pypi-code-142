# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_profile']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'simple-profile',
    'version': '1.0.0',
    'description': 'Simple profile decorator to monitor execution time and memory usage.',
    'long_description': '# simple-profile\nSimple profile decorator for Python\n',
    'author': 'João Brilhante',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JoaoBrlt/simple-profile',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
