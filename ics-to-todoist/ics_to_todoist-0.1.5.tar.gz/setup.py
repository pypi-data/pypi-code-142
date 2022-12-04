# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ics_to_todoist', 'ics_to_todoist.models']

package_data = \
{'': ['*']}

install_requires = \
['ics>=0.7.2,<0.8.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'todoist-python>=8.1.3,<9.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['ics-to-todoist = ics_to_todoist.__main__:app']}

setup_kwargs = {
    'name': 'ics-to-todoist',
    'version': '0.1.5',
    'description': 'A command line tool to convert entries from an .ics file to tasks in Todoist.',
    'long_description': '# ics-to-todoist\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ics-to-todoist?color=red)\n![PyPI - License](https://img.shields.io/pypi/l/ics-to-todoist?color=blue)\n[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)\n[![mypy: checked](https://img.shields.io/badge/mypy-checked-blue)](http://mypy-lang.org)\n[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)\n[![Tests](https://github.com/gaborschulz/ics-to-todoist/actions/workflows/pytest.yml/badge.svg)](https://github.com/gaborschulz/ics-to-todoist/actions/workflows/pytest.yml)\n[![Coverage](https://raw.githubusercontent.com/gaborschulz/ics-to-todoist/main/coverage.svg)](https://github.com/gaborschulz/ics-to-todoist)\n[![PyPI](https://img.shields.io/pypi/v/ics-to-todoist)](https://pypi.org/project/ics-to-todoist/)\n\n## Summary\n\nA command line tool to convert entries from an `.ics` file to tasks in Todoist.\n\n## Getting Started\n\nGetting started is quite simple:  \n\n`pipx install ics-to-todoist`\n\n## Documentation\n\nThe documentation is available here: https://ics-to-todoist.gaborschulz.com.\n\n## Legal info\n\nThis app is not created by, affiliated with, or supported by Doist.\n\n## Copyright\n\nCopyright Gabor Schulz, 2022\n',
    'author': 'Gabor Schulz',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gaborschulz.github.io/ics-to-todoist/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
