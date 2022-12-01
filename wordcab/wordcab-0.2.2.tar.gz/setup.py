# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wordcab', 'wordcab.core_objects']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'requests>=2.28.1', 'validators>=0.20.0']

entry_points = \
{'console_scripts': ['wordcab = wordcab.__main__:main']}

setup_kwargs = {
    'name': 'wordcab',
    'version': '0.2.2',
    'description': 'Wordcab Python SDK',
    'long_description': '# Wordcab Python\n\n[![PyPI](https://img.shields.io/pypi/v/wordcab.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/wordcab.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/wordcab)][python version]\n[![License](https://img.shields.io/pypi/l/wordcab)][license]\n\n[![Read the documentation at https://wordcab-python.readthedocs.io/](https://img.shields.io/readthedocs/wordcab-python/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/Wordcab/wordcab-python/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/Wordcab/wordcab-python/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/wordcab-python/\n[status]: https://pypi.org/project/wordcab-python/\n[python version]: https://pypi.org/project/wordcab-python\n[read the docs]: https://wordcab-python.readthedocs.io/\n[tests]: https://github.com/Wordcab/wordcab-python/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/Wordcab/wordcab-python\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Wordcab\n\n### What is Wordcab?\n\n**Summarize any business communications at scale with Wordcab\'s API.**\n\n**Wordcab** is a summarization service that provides a simple API to summarize any `audio`, `text`, or `JSON` file.\n\nIt also includes compatibility with famous transcripts platforms like [AssemblyAI](https://www.assemblyai.com/),\n[Deepgram](https://deepgram.com/), [Rev.ai](https://www.rev.ai/), [Otter.ai](https://otter.ai/), or\n[Sonix.ai](https://sonix.ai/).\n\n### Getting started\n\nYou can learn more about Wordcab services and pricing on [our website](https://wordcab.com/).\n\nIf you want to try out the API, you can [signup](https://wordcab.com/signup/) for a free account and start using the API\nright away.\n\n## Requirements\n\n- Os: Linux, Mac, Windows\n- Python 3.8+\n\n## Installation\n\nYou can install _Wordcab Python_ via [pip] from [PyPI]:\n\n```console\n$ pip install wordcab\n```\n\nStart using the API with any python script right away:\n\n```python\nfrom wordcab import get_stats\n\nstats = get_stats()\nprint(stats)\n```\n\n## Usage\n\n[<img src="https://cdn.loom.com/sessions/thumbnails/25150a30c593467fa1632145ff2dea6f-with-play.gif" width="50%">](https://www.loom.com/embed/25150a30c593467fa1632145ff2dea6f "Quick Python Package Demo")\n\nPlease see the [Documentation](https://wordcab-python.readthedocs.io/) for details.\n\n## Contributing\n\nContributions are very welcome. 🚀\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [Apache 2.0 license][license],\n_Wordcab Python SDK_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]\'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/Wordcab/wordcab-python/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/Wordcab/wordcab-python/blob/main/LICENSE\n[contributor guide]: https://github.com/Wordcab/wordcab-python/blob/main/CONTRIBUTING.md\n[command-line reference]: https://wordcab-python.readthedocs.io/en/latest/usage.html\n',
    'author': 'Wordcab',
    'author_email': 'info@wordcab.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Wordcab/wordcab-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
