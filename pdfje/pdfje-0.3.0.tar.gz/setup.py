# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pdfje']

package_data = \
{'': ['*']}

install_requires = \
['fonttools>=4.38.0,<5.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1,<5']}

setup_kwargs = {
    'name': 'pdfje',
    'version': '0.3.0',
    'description': 'Tiny PDF writer',
    'long_description': '🖍 pdf\'je\n=========\n\n.. image:: https://img.shields.io/pypi/v/pdfje.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/pdfje\n\n.. image:: https://img.shields.io/pypi/l/pdfje.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/pdfje\n\n.. image:: https://img.shields.io/pypi/pyversions/pdfje.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/pdfje\n\n.. image:: https://img.shields.io/readthedocs/pdfje.svg?style=flat-square\n   :target: http://pdfje.readthedocs.io/\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square\n   :target: https://github.com/psf/black\n\n-----\n\n  **pdf·je** [`🔉 <https://upload.wikimedia.org/wikipedia/commons/a/ac/Nl-pdf%27je.ogg>`_ PDF·yuh] (noun) Dutch for \'small PDF\'\n\nTiny library for writing simple PDFs.\n\nCurrently under development.\nThe API may change significantly until the 1.x release.\nLeave a ⭐️ on GitHub if you\'re interested how this develops!\n\n💁\u200d♂️ Why?\n----------\n\nThe most popular Python libraries for writing PDFs are quite old\nand inspired by Java and PHP. **pdf\'je** is a modern, Pythonic library with\na more declarative API.\n\n🚀 How does it work?\n--------------------\n\nGetting text on paper is super easy:\n\n.. code-block:: python\n\n  from pdfje import Document\n  Document("Olá Mundo!").write(\'hello.pdf\')\n\nbut you can of course do more:\n\n.. code-block:: python\n\n  from pdfje import Page, Text, Font\n\n  myfont = Font.from_path(\'path/to/MyFont.ttf\')\n  Document([\n      Page("""Simple is better than complex.\n              Complex is better than complicated."""),\n      Page(),\n      Page(Text("This text is bigger and fancier!", font=myfont, size=20))\n  ]).write(\'hello.pdf\')\n\n\nSee `the docs <https://pdfje.rtfd.io>`_ for a complete overview.\n\n👩\u200d⚕️ Is pdf\'je right for me?\n------------------------------\n\nTry it if you:\n\n- 🎯 Just want to get simple text into a PDF quickly\n- 🪄 Prefer coding in a declarative and Pythonic style\n- 🎁 Are looking for a lightweight, permissively licensed library\n- 🔭 Enjoy experimenting and contributing to something new\n\nLook elsewhere if you:\n\n- 🕸️ Want to turn HTML into PDF -- use ``wkhtmltopdf`` instead\n- 🔬 Need perfectly typeset documents -- use LaTeX instead\n- 🚚 Want lots of features -- use ``reportlab`` or ``fpdf2`` instead\n- ✂️  Need to parse or edit -- use ``PyPDF2`` or ``pdfsyntax`` instead\n\n🥘 So, what\'s cooking?\n----------------------\n\nThe following features are planned:\n\n- 📑 Automatic line/page breaks\n- 🎨 ``rich``-inspired styles and inline markup\n- 🖼️ Support for images\n- ✏️  Basic drawing operations\n- 🔗 Bookmarks and links\n\n🎁 Installation\n---------------\n\nIt\'s available on PyPI.\n\n.. code-block:: bash\n\n  pip install pdfje\n\n🛠️ Development\n--------------\n\n- Install dependencies with ``poetry install``.\n- To write output files during tests, use ``pytest --output-path=<outpur-dir>``\n',
    'author': 'Arie Bovenberg',
    'author_email': 'a.c.bovenberg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ariebovenberg/pdfje',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
