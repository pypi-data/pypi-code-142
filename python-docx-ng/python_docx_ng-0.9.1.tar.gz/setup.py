# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python-docx-ng',
 'python-docx-ng.dml',
 'python-docx-ng.enum',
 'python-docx-ng.image',
 'python-docx-ng.opc',
 'python-docx-ng.opc.parts',
 'python-docx-ng.oxml',
 'python-docx-ng.oxml.text',
 'python-docx-ng.parts',
 'python-docx-ng.styles',
 'python-docx-ng.text']

package_data = \
{'': ['*'],
 'python-docx-ng': ['templates/*',
                    'templates/default-docx-template/*',
                    'templates/default-docx-template/_rels/*',
                    'templates/default-docx-template/customXml/*',
                    'templates/default-docx-template/customXml/_rels/*',
                    'templates/default-docx-template/docProps/*',
                    'templates/default-docx-template/word/*',
                    'templates/default-docx-template/word/_rels/*',
                    'templates/default-docx-template/word/theme/*']}

install_requires = \
['behave>=1.2.6,<2.0.0', 'lxml>=4.9.1,<5.0.0']

setup_kwargs = {
    'name': 'python-docx-ng',
    'version': '0.9.1',
    'description': 'python-docx-ng is a Python library for creating and updating Microsoft Word (.docx) files.',
    'long_description': '# python-docx-ng\n\n*python-docx-ng* is a Python library for creating and updating Microsoft Word (.docx) files.\nIt was originally designed and developed by [scanny](https://github.com/scanny) as [python-docx](https://github.com/python-openxml/python-docx).\nAs he is not actively developing his repo and there are soo many useful pull requests, bringing together a more powerful tool.\nThis repo should merge a lot of those things and create a more powerful version, hopefully bearing the original structure of scanny in mind.\n\nMore information is available in the [python-docx-ng Documentation](https://python-docx.readthedocs.org/en/latest/).\n',
    'author': 'toxicphreAK',
    'author_email': 'pentesting.laboratories@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
