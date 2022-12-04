# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studentresume']

package_data = \
{'': ['*'], 'studentresume': ['fonts/*', 'themes/*']}

install_requires = \
['jsonschema>=4.17.3,<5.0.0',
 'reportlab>=3.6.12,<4.0.0',
 'rich>=12.6.0,<13.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['studentresume = studentresume.run:app']}

setup_kwargs = {
    'name': 'studentresume',
    'version': '0.8.2',
    'description': 'Student Resume Generator Python Package',
    'long_description': '# studentresume\n\n---\n\n## Installation\n\nPlease first create a venv:\n\nFor windows users:\n\n```console\npython -m venv [VENV_NAME]\n```\n\nto activate:\n\n```console\n.\\venv\\scripts\\activate\n```\n\n---\n\nfor linux/mac users\n\n```console\nvirtualenv venv --python=python3\n```\n\nto activate:\n\n```console\nsource venv/bin/activate\n```\n\n---\n\n## Usage\n\n## To generate a resume\n\n```console\nstudentresume [OPTIONS] [RESUME_JSON] [THEME_JSON]\n```\n\nFor a detailed help message and optional flags, please use:\n\n```console\nstudentresume --help\n```\n\n---\n\n## Additional info for contributors\n\nClone the repo:\n\n```console\ngit clone git@github.com:open-uofa/studentresume.git\n```\n\nNavigate to the repo:\n\n```console\ncd studentresume\n```\n\nInstall the package using [Poetry](https://python-poetry.org/) (preferred):\n\n```console\npoetry install\n```\n\n\nstudentresume stands on the backs of giants [ReportLab](https://docs.reportlab.com/reportlab/userguide), [Typer](https://typer.tiangolo.com/), [rich](https://docs.reportlab.com/reportlab/userguide), and [NerdFonts](https://www.nerdfonts.com/#home)\n\n## License\n\n---\n\nThis project is licenced under the terms of the MIT license\n',
    'author': 'Diana Le',
    'author_email': 'dble@ualberta.ca',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://studentresume.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
