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

extras_require = \
{'dev': ['pytest',
         'pytest-cov',
         'pytest-profiling',
         'pytest-line-profiler-apn>=0.1.3',
         'ipython',
         'jupyterlab'],
 'docs': ['Sphinx',
          'sphinx-rtd-theme',
          'sphinxcontrib-napoleon',
          'nbsphinx',
          'jupyter-sphinx',
          'sphinx-autoapi',
          'sphinx_autobuild',
          'sphinx_math_dollar']}

setup_kwargs = {
    'name': 'pyfeyn2',
    'version': '2.0.0',
    'description': 'PyFeyn is a package which makes drawing Feynman diagrams simple and programmatic.  Feynman diagrams are important constructs in perturbative field theory, so being able to draw them in a programmatic fashion is important if attempting to enumerate a large number of diagram configurations is important. The output quality of PyFeyn diagrams (into PDF or EPS formats) is very high, and special effects can be obtained by using constructs from PyX, which PyFeyn is based around',
    'long_description': '# PyFeyn2\n\nForked from https://pyfeyn.hepforge.org/\n\n## Dependencies\n\n* libmagickwand-dev\n* latexmk\n\n## Installation\n\n```sh\npoerty install --extras docs --extras dev\npoetry shell\n```\n\n## Development\n\n\n### package/python structure:\n\n* https://mathspp.com/blog/how-to-create-a-python-package-in-2022\n* https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
