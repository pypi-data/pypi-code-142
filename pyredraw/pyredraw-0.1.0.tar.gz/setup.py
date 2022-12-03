# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyredraw']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2']

setup_kwargs = {
    'name': 'pyredraw',
    'version': '0.1.0',
    'description': 'A python package for resampling statistical operations',
    'long_description': '# pyredraw\n\nA python package for resampling statistical operations\n\n## Installation\n\n```bash\n$ pip install pyredraw\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pyredraw` was created by Elizabeth H. Camp. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pyredraw` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Elizabeth H. Camp',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
