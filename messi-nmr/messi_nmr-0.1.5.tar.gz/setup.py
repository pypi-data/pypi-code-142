# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['messi_nmr']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.5',
 'openpyxl>=3.0.10',
 'pandas>=1.5.2',
 'scikit-learn>=1.1.3',
 'scipy>=1.9.3',
 'sklearn>=0.0.post1',
 'tk>=0.1.0']

entry_points = \
{'console_scripts': ['messi = messi_nmr.messi_nmr:main'],
 'messi.main': ['messi = messi_nmr.messi_nmr:main']}

setup_kwargs = {
    'name': 'messi-nmr',
    'version': '0.1.5',
    'description': 'Multi Ensamble Strategy for Structural Identification (MESSI). Developed by Sarotti Lab',
    'long_description': '# messi_nmr\n\nMulti Ensamble Strategy for Structural Identification (MESSI). Developed by Sarotti Lab\n\n## Installation\n\n```bash\n$ pip install messi_nmr\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`messi_nmr` was created by María M. Zanardi & Ariel M. Sarotti. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`messi_nmr` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'María M. Zanardi & Ariel M. Sarotti',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
