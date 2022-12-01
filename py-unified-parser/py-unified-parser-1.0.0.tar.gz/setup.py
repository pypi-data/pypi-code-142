# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py_unified_parser']

package_data = \
{'': ['*'],
 'py_unified_parser': ['dict/*',
                       'rules/*',
                       'tsylb2-1.1/*',
                       'tsylb2-1.1/doc/*',
                       'tsylb2-1.1/lexdata/foreign/*',
                       'tsylb2-1.1/lexdata/nat+for/*',
                       'tsylb2-1.1/lexdata/native/*']}

install_requires = \
['g2p-en>=2.0.0,<3.0.0', 'numpy>=1.14,<2.0', 'packaging>=20.9,<21.0']

setup_kwargs = {
    'name': 'py-unified-parser',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'Arun Baby',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
