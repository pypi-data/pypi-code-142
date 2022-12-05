# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jeeves_core']

package_data = \
{'': ['*']}

install_requires = \
['boltons>=21.0.0,<22.0.0',
 'documented>=0.1.1,<0.2.0',
 'flake8<4.0.0',
 'more-itertools>=9.0.0,<10.0.0',
 'python-benedict>=0.24.3,<0.25.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['j = jeeves_core.cli:app']}

setup_kwargs = {
    'name': 'jeeves-core',
    'version': '1.0.5',
    'description': 'Pythonic replacement for GNU Make: core',
    'long_description': '# jeeves-core\n\n[![Build Status](https://github.com/jeeves-sh/jeeves-core/workflows/test/badge.svg?branch=master&event=push)](https://github.com/jeeves-sh/jeeves-core/actions?query=workflow%3Atest)\n[![codecov](https://codecov.io/gh/jeeves-sh/jeeves-core/branch/master/graph/badge.svg)](https://codecov.io/gh/jeeves-sh/jeeves-core)\n[![Python Version](https://img.shields.io/pypi/pyversions/jeeves-core.svg)](https://pypi.org/project/jeeves-core/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\nPythonic replacement for GNU Make: core\n\n\n## Installation\n\n```bash\npip install jeeves-core\n```\n\n## License\n\n[MIT](https://github.com/jeeves-sh/jeeves-core/blob/master/LICENSE)\n\n\n## Credits\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [3690fd6acb8400994d4ef0f9f1ddccf478bbad9b](https://github.com/wemake-services/wemake-python-package/tree/3690fd6acb8400994d4ef0f9f1ddccf478bbad9b). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/3690fd6acb8400994d4ef0f9f1ddccf478bbad9b...master) since then.\n',
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jeeves-sh/jeeves-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
