# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['uncertainty_rejection']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2', 'numpy>=1.23.5', 'scipy>=1.9.3', 'tabulate>=0.9.0']

setup_kwargs = {
    'name': 'uncertainty-rejection',
    'version': '0.2.0',
    'description': 'Analysis of uncertainty estimates for classification with rejection.',
    'long_description': '# uncertainty-rejection\n\n<p align="center">\n<a href="https://pypi.org/project/uncertainty-rejection/">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/uncertainty_rejection">\n    </a>\n<img src="https://github.com/arthur-thuy/uncertainty-rejection/actions/workflows/ci-cd.yml/badge.svg" />\n<a href=\'https://uncertainty-rejection.readthedocs.io/en/latest/\'>\n        <img src=\'https://img.shields.io/readthedocs/uncertainty-rejection\' alt=\'Documentation Status\' />\n    </a>\n<a href="https://codecov.io/gh/arthur-thuy/uncertainty-rejection" > \n <img src="https://codecov.io/gh/arthur-thuy/uncertainty-rejection/branch/main/graph/badge.svg?token=QQ7U6XO64X"/> \n </a>\n</p>\n\nAnalysis of uncertainty estimates for classification with rejection.\n\n## Installation\n\n```bash\n$ pip install uncertainty-rejection\n```\n\n## Documentation\n\nThe documentation is deployed to [uncertainty-rejection.readthedocs.io](http://uncertainty-rejection.readthedocs.io/).\n\n## Examples\n\nAn example notebook is provided, which can be found in the ["Example usage" section](https://uncertainty-rejection.readthedocs.io/en/latest/example.html) of the documentation.\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`uncertainty-rejection` was created by Arthur Thuy. It is licensed under the terms of the Apache License 2.0 license.\n\n## Credits\n\n`uncertainty-rejection` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Arthur Thuy',
    'author_email': 'arthur.thuy@ugent.be',
    'maintainer': 'Arthur Thuy',
    'maintainer_email': 'arthur.thuy@ugent.be',
    'url': 'https://github.com/arthur-thuy/uncertainty-rejection',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
