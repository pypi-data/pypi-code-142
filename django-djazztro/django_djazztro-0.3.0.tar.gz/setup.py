# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_djazztro', 'django_djazztro.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django>=4.1.3,<5.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-djazztro',
    'version': '0.3.0',
    'description': 'Python-side of the Djazztro stack, provides a template backend for using Astro files.',
    'long_description': 'None',
    'author': 'Ben C',
    'author_email': 'bwc9876@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
