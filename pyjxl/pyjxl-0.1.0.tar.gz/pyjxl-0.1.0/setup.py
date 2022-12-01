# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyjxl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyjxl',
    'version': '0.1.0',
    'description': '',
    'long_description': "# pyJXL\n\npyjxl is an experimental decoder for JPEG-XL .jxl files in Python.\n\npyjxl's primary goals are being an easy to understand decoder and enabling experimentation.\nIt's not meant to be performant or complete.\nPlease use [`libjxl`](https://github.com/libjxl/libjxl) instead for actual decoding purposes.\n\n\n\n",
    'author': 'Aravind Reddy Voggu',
    'author_email': 'aravind.reddy@iiitb.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
