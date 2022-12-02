# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faker_stalker_names',
 'faker_stalker_names.de_DE',
 'faker_stalker_names.en_US',
 'faker_stalker_names.es_ES',
 'faker_stalker_names.fr_FR',
 'faker_stalker_names.it_IT',
 'faker_stalker_names.pl_PL',
 'faker_stalker_names.ru_RU',
 'faker_stalker_names.uk_UA']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'faker-stalker-names',
    'version': '0.1.4',
    'description': 'Faker provider to generate stalker names.',
    'long_description': '![python version](https://img.shields.io/pypi/pyversions/faker-stalker-names?style=for-the-badge) \n[![version](https://img.shields.io/pypi/v/faker-stalker-names?style=for-the-badge)](https://pypi.org/project/faker-stalker-names/)\n![Codecov](https://img.shields.io/codecov/c/github/booqoffsky/faker-stalker-names?style=for-the-badge&token=1W6WD47RFU)\n\n# faker-stalker-names\n![](https://raw.githubusercontent.com/booqoffsky/faker-stalker-names/main/imgs/head.png)\n\n>_Faker-stalker-names_ is a provider for the [Faker](https://github.com/joke2k/faker) Python package that allows you\n>to generate stalker names for your tests and other tasks. \n>\n>Don\'t forget your friends) (с) Slava Smartass\n\n# Localizations\nThe following localizations are present:\n>`de_DE`, `en_US`, `es_ES`, `fr_FR`, `it_IT`, `pl_PL`, `ru_RU`, `uk_UA`\n\n# Installation\nFrom PyPi:\n\n`pip3 install faker-stalker-names`\n\n# Usage\nJust add the `Provider` to your `Faker` instance:\n\n```\nfrom faker import Faker\nfrom faker_stalker_names.en_US import Provider as StalkerNamesProvider\n\nfake = Faker()\nfake.add_provider(StalkerNamesProvider)\n```\nOr pass it to the constructor:\n```\nfrom faker import Faker\n\nfake = Faker(includes=["faker_stalker_names"], locale="ru_RU")\n```\nNow you can start to generate data:\n```\nfake.stalker_name()\n# Яшка Нытик\n\nfake.stalker_first_name()\n# Саня\n\nfake.stalker_last_name()\n# Резкий\n```\n\nYou can specify the desired type of name (`stalker` or `bandit` are available). \nBy default, the first and last names are randomly selected.\n```\nfake.stalker_name(name_type="stalker")\n# Slava Smartass\n\nfake.stalker_first_name(name_type="bandit")\n# Vasyan\n```\n\nIn addition, a way to replace the standard `name` method at your own risk:\n```\nStalkerNamesProvider.name = StalkerNamesProvider.stalker_name\nfake = Faker()\nfake.add_provider(StalkerNamesProvider)\nfake.name()\n# Shurik Professor\n```\n',
    'author': 'Grigory Bukovsky',
    'author_email': 'booqoffsky@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/booqoffsky/faker-stalker-names',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
