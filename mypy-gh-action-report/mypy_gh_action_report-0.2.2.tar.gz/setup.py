# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mypy_gh_action_report', 'mypy_gh_action_report.converters']

package_data = \
{'': ['*']}

install_requires = \
['github-action-utils>=1.1.0,<2.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['mypy-gh-action-report = '
                     'mypy_gh_action_report.main:execute']}

setup_kwargs = {
    'name': 'mypy-gh-action-report',
    'version': '0.2.2',
    'description': 'Notify Mypy output via GitHub Workflow Commands',
    'long_description': '[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mypy-gh-action-report.svg)](https://pypi.python.org/pypi/mypy-gh-action-report/)\n[![PyPI](https://img.shields.io/pypi/v/mypy-gh-action-report.svg)](https://pypi.python.org/pypi/mypy-gh-action-report/)\n\n# mypy-gh-action-report\n\nNotify Mypy output via [GitHub Workflow Commands](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions)\n\n## Installation\n\n```bash\npip install mypy-gh-action-report\n```\n\n## Docs\n\nAvailable [here](https://bc291.github.io/mypy-gh-action-report/)\n\n## Thanks\n\n- [github-action-utils](https://github.com/saadmk11/github-action-utils)\n- [typer](https://github.com/tiangolo/typer)\n',
    'author': 'Błażej Cyrzon',
    'author_email': 'blazej.cyrzon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
