# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flexible_list_of_values', 'flexible_list_of_values.migrations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'flexible-list-of-values',
    'version': '0.1.0',
    'description': 'Flexible Lists of Values (LOV) for Django',
    'long_description': '# flexible-list-of-values\nFlexible and Extensible Lists of Values (LOV) for Django\n',
    'author': 'Jack Linke',
    'author_email': 'jack@watervize.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
