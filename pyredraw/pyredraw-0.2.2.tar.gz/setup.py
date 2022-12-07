# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyredraw']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2',
 'numpy==1.23.5',
 'scipy==1.8.1',
 'statsmodels>=0.13.5,<0.14.0']

setup_kwargs = {
    'name': 'pyredraw',
    'version': '0.2.2',
    'description': 'A python package for resampling statistical operations',
    'long_description': '# pyredraw\n\nA python package for resampling statistical operations\n\n## Installation\n\n```bash\n$ pip install pyredraw\n```\nPackage available on PyPI at https://pypi.org/project/pyredraw/\n\n## Usage\n\n- For example usage see `pyredraw/docs/example.ipynb` with documentation available at https://pyredraw.readthedocs.io/en/stable/\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pyredraw` was created by Elizabeth H. Camp. It is licensed under the terms of the MIT license.\n\n## Credits\n\nA big thank you goes to Tomas Beuzan and Tiffany Timbers for their book Python Packages which can be found at https://py-pkgs.org . This resource was invaluable in creating `pyredraw` \n',
    'author': 'Elizabeth H. Camp',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
