# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statlink']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'aiolimiter>=1.0.0,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'lxml>=4.9.1,<5.0.0',
 'playwright>=1.28.0,<2.0.0',
 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['statlink = statlink.command:main']}

setup_kwargs = {
    'name': 'statlink',
    'version': '0.1.3',
    'description': 'An asyncio based multipurpose link checker.',
    'long_description': '# Statlink\n\nAn asyncio based multipurpose link explorer.\n\n- Check broken links in websites.\n- Headless browsers support (Chromium, Firefox, WebKit).\n- Domain / URL Regex / status code filters.\n- Incremental timeout.\n- Panda dataframe / CSV output.\n- Database store support.\n\n\n## Get started\n\n### Installation\n\n    pip install statlink\n\nWith browser support:\n\n    pip install statlink[chromium|fifefox|webkit|all]\n\n## Usage\n\n    Usage: statlink [OPTIONS] [SOURCES]...\n\n    Options:\n      -c, --concurrency INTEGER       Set the maximum number of concurrent\n                                      requests.  [default: 20]\n      --allow-external                Allow external URL to be checked.\n      -d, --depth INTEGER             Recursion depth value for checking URLs,\n                                      negative value will set it to infinity.\n                                      [default: -1]\n      -t, --timeout INTEGER           Set timeout for each requests.  [default:\n                                      20]\n      --engine [aiohttp|chromium|firefox|webkit]\n                                      Engine that will be used to make requests.\n                                      [default: aiohttp]\n      --help                          Show this message and exit.\n\n\n## Examples\n\nFind the dead links for a https domain\n\n    $ statlink https://google.com\n\n\nFind the dead links in a text file\n\n    $ statlink -d 0 bad_urls.txt\n\n\n## Library\n\n\n    from statlink.crawler import Crawler\n\n    crawler = Crawler()\n    crawler.add_url("https://google.com")\n    crawler.start()\n',
    'author': 'Thibaut Frain',
    'author_email': 'thibaut.frain@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
