# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mockeval']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mockeval',
    'version': '0.1.3',
    'description': 'Cursed lambdas because yes',
    'long_description': '# mockeval\nCursed lambdas because yes.\n\n## Usage\n```py\nfrom mockeval import var, val\n\ntimes2 = var.x * 2\nprint(times2.evl(x=2))  # 4\n\nlist_with_unkowns = val([1, 2, var.third, var.fourth])\nprint(list_with_unkowns.evl(third=3, fourth=4))  # [1, 2, 3, 4]\n\nprint(list_with_unkowns.map(sum).evl(third=3, fourth=4))  # 10\n```\n\n## Why?\nyes.\n',
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
