# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linefolio', 'linefolio.tests', 'linefolio.tests.test_data']

package_data = \
{'': ['*'], 'linefolio': ['examples/*']}

install_requires = \
['empyrical>=0.5.5,<0.6.0',
 'ipython>=8.7.0,<9.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pytz>=2022.6,<2023.0',
 'quantrocket-moonshot>=2.8.0.1,<3.0.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'seaborn>=0.12.1,<0.13.0']

setup_kwargs = {
    'name': 'linefolio',
    'version': '1.8.0',
    'description': 'Backtest performance analysis and charting for MoonLine, but with pyfolio.',
    'long_description': '![pyfolio](https://media.quantopian.com/logos/open_source/pyfolio-logo-03.png "pyfolio")\n\n# pyfolio\n\n[![Join the chat at https://gitter.im/quantopian/pyfolio](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/quantopian/pyfolio?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n[![build status](https://travis-ci.org/quantopian/pyfolio.png?branch=master)](https://travis-ci.org/quantopian/pyfolio)\n\npyfolio is a Python library for performance and risk analysis of\nfinancial portfolios developed by\n[Quantopian Inc](https://www.quantopian.com). It works well with the\n[Zipline](https://www.zipline.io/) open source backtesting library.\nQuantopian also offers a [fully managed service for professionals](https://factset.quantopian.com)\nthat includes Zipline, Alphalens, Pyfolio, FactSet data, and more.\n\nAt the core of pyfolio is a so-called tear sheet that consists of\nvarious individual plots that provide a comprehensive image of the\nperformance of a trading algorithm. Here\'s an example of a simple tear\nsheet analyzing a strategy:\n\n![simple tear 0](https://github.com/quantopian/pyfolio/raw/master/docs/simple_tear_0.png "Example tear sheet created from a Zipline algo")\n![simple tear 1](https://github.com/quantopian/pyfolio/raw/master/docs/simple_tear_1.png "Example tear sheet created from a Zipline algo")\n\nAlso see [slides of a talk about\npyfolio](https://nbviewer.jupyter.org/format/slides/github/quantopian/pyfolio/blob/master/pyfolio/examples/pyfolio_talk_slides.ipynb#/).\n\n## Installation\n\nTo install pyfolio, run:\n\n```bash\npip install pyfolio\n```\n\n#### Development\n\nFor development, you may want to use a [virtual environment](https://docs.python-guide.org/en/latest/dev/virtualenvs/) to avoid dependency conflicts between pyfolio and other Python projects you have. To get set up with a virtual env, run:\n```bash\nmkvirtualenv pyfolio\n```\n\nNext, clone this git repository and run `python setup.py develop`\nand edit the library files directly.\n\n#### Matplotlib on OSX\n\nIf you are on OSX and using a non-framework build of Python, you may need to set your backend:\n``` bash\necho "backend: TkAgg" > ~/.matplotlib/matplotlibrc\n```\n\n## Usage\n\nA good way to get started is to run the pyfolio examples in\na [Jupyter notebook](https://jupyter.org/). To do this, you first want to\nstart a Jupyter notebook server:\n\n```bash\njupyter notebook\n```\n\nFrom the notebook list page, navigate to the pyfolio examples directory\nand open a notebook. Execute the code in a notebook cell by clicking on it\nand hitting Shift+Enter.\n\n\n## Questions?\n\nIf you find a bug, feel free to [open an issue](https://github.com/quantopian/pyfolio/issues) in this repository.\n\nYou can also join our [mailing list](https://groups.google.com/forum/#!forum/pyfolio) or\nour [Gitter channel](https://gitter.im/quantopian/pyfolio).\n\n## Support\n\nPlease [open an issue](https://github.com/quantopian/pyfolio/issues/new) for support.\n\n## Contributing\n\nIf you\'d like to contribute, a great place to look is the [issues marked with help-wanted](https://github.com/quantopian/pyfolio/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).\n\nFor a list of core developers and outside collaborators, see [the GitHub contributors list](https://github.com/quantopian/pyfolio/graphs/contributors).\n',
    'author': 'Tim Wedde',
    'author_email': 'tim.wedde@genzai.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
