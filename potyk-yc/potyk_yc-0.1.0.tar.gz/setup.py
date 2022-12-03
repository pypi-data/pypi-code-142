# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['potyk_yc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'potyk-yc',
    'version': '0.1.0',
    'description': '',
    'long_description': '# potyk-yc\n\nУтилиты и тайпинги для работы с [Yandex Cloud](https://cloud.yandex.ru/) ',
    'author': 'potykion',
    'author_email': 'potykion@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
