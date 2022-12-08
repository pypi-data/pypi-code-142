# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stratosphere',
 'stratosphere.store',
 'stratosphere.store.db',
 'stratosphere.utils']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=2.2.0,<3.0.0',
 'colorama>=0.4.6,<0.5.0',
 'joblib>=1.2.0,<2.0.0',
 'pandas>=1.5.1,<2.0.0',
 'sqlalchemy-utils>=0.38.3,<0.39.0',
 'sqlalchemy>=1.4.44,<2.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'ulid-py>=1.1.0,<2.0.0']

extras_require = \
{'complete': ['tabulate>=0.9.0,<0.10.0',
              'ipywidgets>=8.0.2,<9.0.0',
              'scikit-learn>=1.1.3,<2.0.0',
              'dask[complete]>=2022.11.0,<2023.0.0'],
 'dask': ['dask[complete]>=2022.11.0,<2023.0.0'],
 'pgsql': ['psycopg2-binary>=2.9.5,<3.0.0']}

setup_kwargs = {
    'name': 'stratosphere',
    'version': '0.1.62',
    'description': 'A lightweight experimentation toolkit for data scientists.',
    'long_description': '# Stratosphere\n\n*A lightweight experimentation toolkit for data scientists.*\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/stratosphere)\n![PyPI - License](https://img.shields.io/pypi/l/stratosphere)\n![PyPI - Version](https://img.shields.io/pypi/v/stratosphere)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/stratosphere)\n![PyPI - Installs](https://img.shields.io/pypi/dm/stratosphere)\n![Black - Code style](https://img.shields.io/badge/code%20style-black-000000.svg)\n[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dkKBwhm4L_MMoWWtfD0FAFgTFP1BV40c)\n[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/elehcimd/stratosphere/HEAD)\n\nDesigned to be accessibile, fast and robust. `stratosphere` lets you:\n\n1. **Define** programmatically your experiments\n2. **Execute** them in parallel with different backends\n3. **Track** their real-time metrics and final results\n4. **Store** them as serialized objects and tabular data in your database(s)\n5. **Query** them with the best-suited interface: SQL, Pandas and Python\n\nHow is it possible?\n\n* **Fast and light**: [Try it now with JupyterLite](https://github.com/elehcimd/stratosphere/blob/main/doc/JUPYTERLITE.md), it runs entirely in the browser\n* **Built on top of solid components**: [SQLAlchemy](https://www.sqlalchemy.org/), [SQLite](https://www.sqlite.org/), [Pandas](https://pandas.pydata.org/), [Joblib](https://joblib.readthedocs.io/en/latest/) and [Dask](https://www.dask.org/)\n* **Designed for data accessibility**: Use it where you need it. For example, you can experiment in-memory, persist locally, replicate tables on [render.com](https://render.com), and publish results on [preset.io](https://preset.io) (all free tiers!)\n\n![Stratosphere](https://raw.githubusercontent.com/elehcimd/stratosphere/b6993093ae617b98bcabf5d1d3153a7c3e1383a5/logo.png)\n\n## Installation\n\nOn `Python >= 3.8.0`:\n\n* With PyPI: `pip install "stratosphere[complete]" --upgrade` # Install everything\n* With Poetry: `poetry add stratosphere@latest --extras complete` # Install everything\n\nOn `Python 3.7.13-15` with [Google Colab](https://colab.research.google.com/) or \n[Binder](https://mybinder.org), execute the following at the beginning of the notebook:\n\n```\n# Install dependencies\n!pip install pandas joblib sqlalchemy sqlalchemy-utils ulid-py cloudpickle colorama tqdm --upgrade\n\n# Install [complete] extras, required to run the tutorial\n!pip install tabulate scikit-learn dask[complete] --upgrade\n\n# Install the latest stratosphere version, ignoring the python version and dependencies\n!pip install stratosphere --upgrade --ignore-requires-python --no-dependencies\n\n# Resolve ContextualVersionConflict errors, due to broken dependencies\nimport importlib\nimport pkg_resources\nimportlib.reload(pkg_resources)\n```\n\nYou can also install only the `stratosphere` library (dropping the `[complete]` extras).\nModules like `stratosphere.utils.dask`, `stratosphere.utils.metrics`, and `stratosphere.utils.widgets`\nwon\'t work until you also install `dask[complete]`, `scikit-learn`, and `ipywidgets`, respectively.\nThese extras are required to run some of the tutorial notebooks.\n\n## Documentation\n\n* In the [intro notebook](https://github.com/elehcimd/stratosphere/blob/main/doc/JUPYTERLITE.md), you\'ll be exposed to the key concepts. It runs entirely in the browser.\n* In the [tutorial notebooks](./notebooks/), you\'ll cover the advanced topics. Working locally, on Colab and on Binder.\n\n\n## Project pages\n\n* [PyPI](https://pypi.org/project/stratosphere/)\n* [Github](https://github.com/elehcimd/stratosphere)\n\n## License\n\nThis project is licensed under the terms of the [BSD 3-Clause License](https://github.com/elehcimd/stratosphere/blob/main/LICENSE).\n\n## Development\n\nSee the [development](https://github.com/elehcimd/stratosphere/blob/main/docs/DEVELOPMENT.md) page.\n\n## Contributing\n\nWork in progress!\n',
    'author': 'Michele Dallachiesa',
    'author_email': 'michele.dallachiesa@sigforge.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/elehcimd/stratosphere',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.0,<3.11',
}


setup(**setup_kwargs)
