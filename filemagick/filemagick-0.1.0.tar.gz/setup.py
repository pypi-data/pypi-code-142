# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['filemagick']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

extras_require = \
{'testing': ['pytest>=7.1.2,<8.0.0']}

entry_points = \
{'console_scripts': ['filemagick = filemagick.__main__:cli']}

setup_kwargs = {
    'name': 'filemagick',
    'version': '0.1.0',
    'description': 'Tools for files manipulation',
    'long_description': '## FileMagick - Tools for files manipulation\n\n```bash\nfilemagick sub __init__.py -p \'__version__ = "0.0.0"\' -r \'__version__ = "0.1.0"\'\n```\n\nFor more use cases see the test cases in the `tests` directory.\n',
    'author': 'Wonder',
    'author_email': 'wonderbeyond@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wonderbeyond/filemagick',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
