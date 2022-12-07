# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['honorific']

package_data = \
{'': ['*'], 'honorific': ['dicts/*']}

install_requires = \
['pymorphy2>=0.9.1,<0.10.0', 'spacy>=3.4.3,<4.0.0', 'twine>=4.0.2,<5.0.0']

setup_kwargs = {
    'name': 'honorific',
    'version': '0.1.1',
    'description': '',
    'long_description': '# honorific\n\nГоноратив',
    'author': 'Artem Snegirev',
    'author_email': 'a.snegirev@promo-bot.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
