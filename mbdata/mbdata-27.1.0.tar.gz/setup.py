# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mbdata',
 'mbdata.api',
 'mbdata.data',
 'mbdata.tests',
 'mbdata.tools',
 'mbdata.utils']

package_data = \
{'': ['*'],
 'mbdata': ['sql/*',
            'sql/caa/*',
            'sql/dbmirror2/*',
            'sql/documentation/*',
            'sql/eaa/*',
            'sql/json_dump/*',
            'sql/report/*',
            'sql/sitemaps/*',
            'sql/statistics/*',
            'sql/updates/*',
            'sql/updates/schema-change/*',
            'sql/wikidocs/*']}

install_requires = \
['six>=1.16.0,<2.0.0']

extras_require = \
{'models': ['SQLAlchemy>=1.4.29,<2.0.0'],
 'replication': ['psycopg2>=2.9.2,<3.0.0'],
 'search': ['lxml>=4.9.1,<5.0.0']}

entry_points = \
{'console_scripts': ['mbslave = mbdata.replication:main']}

setup_kwargs = {
    'name': 'mbdata',
    'version': '27.1.0',
    'description': '',
    'long_description': None,
    'author': 'Lukáš Lalinský',
    'author_email': 'lalinsky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
