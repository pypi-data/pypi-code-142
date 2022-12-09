# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zipy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'zipy',
    'version': '0.3.0',
    'description': 'Zipy is a toolbox containing a set of convenient python function',
    'long_description': '# Developement\n## Prerequisit\n- install poetry\n\n## Build dev environment\n```\ncd <path-to-project>\n\npoetry install\n\npoetry env use 3.10\n\npre-commit install\n```',
    'author': '冒险岛真好玩',
    'author_email': '17826800084g@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
