# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assmblr', 'assmblr.strict']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'assmblr',
    'version': '0.0.3',
    'description': 'Tools for assembling classes in a concise, performant way',
    'long_description': '### Assmblr\n___\n Simple to use class building tools to make your life easier. The goal is to dry up code by providing generics of common functions and utilities.\n___\n\nCurrently includes: \n- Strict type enforcement',
    'author': 'Alyce',
    'author_email': 'Alyceosbourne@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AlyceOsbourne/assmblr',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
