# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfeyn2', 'pyfeyn2.render', 'pyfeyn2.render.pyx']

package_data = \
{'': ['*']}

install_requires = \
['Wand',
 'dot2tex',
 'matplotlib',
 'numpy',
 'particle',
 'pydot',
 'pylatex',
 'pyx>=0.12',
 'xsdata[cli,lxml,soap]']

setup_kwargs = {
    'name': 'pyfeyn2',
    'version': '2.0.3',
    'description': 'PyFeyn is a package which makes drawing Feynman diagrams simple and programmatic.  Feynman diagrams are important constructs in perturbative field theory, so being able to draw them in a programmatic fashion is important if attempting to enumerate a large number of diagram configurations is important. The output quality of PyFeyn diagrams (into PDF or EPS formats) is very high, and special effects can be obtained by using constructs from PyX, which PyFeyn is based around',
    'long_description': "# PyFeyn2\n\nForked from https://pyfeyn.hepforge.org/\n\nPyFeyn is a Python-language based system for drawing Feynman diagrams. It was inspired by the C++ FeynDiagram system, and aims to provide the same functionality and quality of output as that, with the added benefits of a modern interpreted language, an improved interface and output direct to both EPS and PDF. Behind the scenes, PyFeyn uses the excellent PyX system - you can use PyX constructs in PyFeyn diagrams if you want, too.\n\n## Dependencies\n\n-   libmagickwand-dev (to display pdfs in a jupyter-notebook, might require a policy change of the imagemagick config for PDFs, see Troubleshooting)\n-   latexmk\n-   (feynmp-auto/feynmf)\n\n## Installation\n\n```sh\npoerty install --with docs --with dev\npoetry shell\n```\n\n## Documentation\n\n-   <https://pyfeyn2.readthedocs.io/en/stable/>\n-   <https://apn-pucky.github.io/pyfeyn2/index.html>\n\n## Troubleshooting\n\n-   [ImageMagick security policy 'PDF' blocking conversion]( https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion )\n\n## Development\n\n\n### package/python structure:\n\n-   <https://mathspp.com/blog/how-to-create-a-python-package-in-2022>\n-   <https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/>\n",
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
