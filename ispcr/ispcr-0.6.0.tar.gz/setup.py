# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ispcr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ispcr',
    'version': '0.6.0',
    'description': 'Simple in silico PCR',
    'long_description': '# ispcr\n\n[![PyPI](https://img.shields.io/pypi/v/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![PyPI - License](https://img.shields.io/pypi/l/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://pommevilla.github.io/ispcr](https://pommevilla.github.io/ispcr)\n\n**Source Code**: [https://github.com/pommevilla/ispcr](https://github.com/pommevilla/ispcr)\n\n**PyPI**: [https://pypi.org/project/ispcr/](https://pypi.org/project/ispcr/)\n\n---\n\nA simple, light-weight package written in base Python to perform *in silico* PCR to determine primer performance.\n\n**Currently in development**\n\n## Installation\n\n```sh\npip install ispcr\n```\n## Demonstration\n\nThe main function to use in this package is `find_pcr_product`, which takes as input two file paths:\n  * `primer_file` - the path to fasta file containing your primers\n    * This is currently limited to a fasta file containing two sequences, with the forward primer coming first and the reverse primer coming second\n  * `sequence_file` the path to the fasta file containing the sequences to test your primers against\n\n`find_pcr_product` will then iterate through the sequences in `sequence` file and find all products amplified by the forward and reverse primer.\n\n![](imgs/find_pcr_product.png)\n\n`find_pcr_product` also takes a `minimum_product_length` argument:\n\n![](imgs/find_pcr_product_min_length.png)\n',
    'author': 'Paul Villanueva',
    'author_email': 'pvillanueva13@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pommevilla.github.io/ispcr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
