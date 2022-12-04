# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rich_tables']

package_data = \
{'': ['*']}

install_requires = \
['multimethod', 'rgbxy>=0.5', 'rich>=12.3.0']

entry_points = \
{'console_scripts': ['table = rich_tables.table:main']}

setup_kwargs = {
    'name': 'rich-tables',
    'version': '0.1.2',
    'description': 'Ready-made rich tables for various purposes',
    'long_description': '# Rich tables\n\n* [Album](#album)\n* [Calendar](#calendar)\n* [Emails](#emails)\n* [Hue](#hue)\n* [Nested json](#nested_json)\n* [Pr](#pr)\n* [Simple json](#simple_json)\n* [Tasks](#tasks)\n* [Timed](#timed)\n\n\n## Album\n![image](svgs/album.svg)\n## Calendar\n![image](svgs/calendar.svg)\n## Emails\n![image](svgs/emails.svg)\n## Hue\n![image](svgs/hue.svg)\n## Nested json\n![image](svgs/nested_json.svg)\n## Pr\n![image](svgs/pr.svg)\n## Simple json\n![image](svgs/simple_json.svg)\n## Tasks\n![image](svgs/tasks.svg)\n## Timed\n![image](svgs/timed.svg)\n',
    'author': 'Šarūnas Nejus',
    'author_email': 'snejus@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/snejus/rich-tables',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.3,<4',
}


setup(**setup_kwargs)
