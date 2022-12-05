# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docx',
 'docx.dml',
 'docx.enum',
 'docx.image',
 'docx.opc',
 'docx.opc.parts',
 'docx.oxml',
 'docx.oxml.text',
 'docx.parts',
 'docx.styles',
 'docx.text']

package_data = \
{'': ['*'],
 'docx': ['templates/*',
          'templates/default-docx-template/*',
          'templates/default-docx-template/_rels/*',
          'templates/default-docx-template/docProps/*',
          'templates/default-docx-template/word/*',
          'templates/default-docx-template/word/_rels/*',
          'templates/default-docx-template/word/theme/*']}

install_requires = \
['behave>=1.2.6,<2.0.0', 'lxml>=4.9.1,<5.0.0']

setup_kwargs = {
    'name': 'python-docx-ng',
    'version': '0.9.2',
    'description': 'python-docx-ng is a Python library for creating and updating Microsoft Word (.docx) files.',
    'long_description': '# python-docx-ng\n\n*python-docx-ng* is a Python library for creating and updating Microsoft Word (.docx) files.\nIt was originally designed and developed by [scanny](https://github.com/scanny) as [python-docx](https://github.com/python-openxml/python-docx).\nAs he is not actively developing his repo and there are soo many useful pull requests, bringing together a more powerful tool.\nThis repo should merge a lot of those things and create a more powerful version, hopefully bearing the original structure of scanny in mind.\n\nMore information is available in the [python-docx-ng Documentation](https://python-docx.readthedocs.org/en/latest/).\n\n## Features\n\n+ [x] Word 16 (Office 2019) Template\n+ [x] Faster & improved tables (#1)\n+ [x] SVG support (#4)\n+ [x] Font scaling (#6)\n+ [x] Outline level (#7) - shows outline in navigation (e.g. Word or PDF application - not affecting the document itself)\n+ [x] RGB color font highlighting (#14)\n+ [x] Hyperlink text (#16)\n+ [x] `.docm` file support (#19) - enables marco documents\n+ [x] Form fields & AltChunk support (#20)\n+ [x] Custom namespaces (#21)\n+ [x] Performance improvements\n  + Paragraph.text (#3)\n  + Cache for table cells (#8)\n+ [x] Fixes\n  + add_picture (#10) - fix next_id to support multiple pictures\n  + `Heading 1` key error due to style capitalization (e.g. in LibreOffice) (#12)\n  + Fix XPath for sectPr in document (#15)\n  + Reproducible documents (#17) - same binary output with same data\n\n## Roadmap\n\n+ [ ] Document all functionallities building a new sample document with *all* (most) features included\n+ [ ] Setup new docs\n+ [ ] Add missing tests\n',
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
