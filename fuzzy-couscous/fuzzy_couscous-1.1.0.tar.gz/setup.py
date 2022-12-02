# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fuzzy_couscous']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0']

entry_points = \
{'console_scripts': ['fuzzy-couscous = fuzzy_couscous.main:cli']}

setup_kwargs = {
    'name': 'fuzzy-couscous',
    'version': '1.1.0',
    'description': 'Generate a django project from the fuzzy-couscous template.',
    'long_description': '# fuzzy-couscous-cli\n\nA cli helper for https://github.com/Tobi-De/fuzzy-couscous.',
    'author': 'Tobi-De',
    'author_email': 'tobidegnon@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
