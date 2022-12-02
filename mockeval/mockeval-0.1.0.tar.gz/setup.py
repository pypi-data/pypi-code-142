# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mockeval']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mockeval',
    'version': '0.1.0',
    'description': 'Cursed lambdas because yes',
    'long_description': '# mockeval\n Cursed lambdas because yes\n',
    'author': 'CircuitSacul',
    'author_email': 'circuitsacul@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
