# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['koo_api']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['format = scripts:format', 'tests = scripts:test']}

setup_kwargs = {
    'name': 'koo-api',
    'version': '0.0.2',
    'description': 'API client wrapper for Koo micro-blogging platform',
    'long_description': '> Work in progress!\n\n# Koo API\n\nThis is a basic api wrapper for [Koo](https://www.kooapp.com/).\n\n# Use\n## Install\n```bash\npip install koo-api\n```\n\n## Usage\n\n```python\nfrom koo_api import KooAccount, KooAccountNotFoundException\n\nuser = KooAccount("felipeneto")\nfor post in user.get_koos():\n    print(post.content)\n```\n\n\n# Development\n\n\nThis is the standard workflow:\n\n1. Clone this repo.\nBefore anything:\n\n```bash\npip install poetry\npoetry install\n```\n\n2. Create a new branch, add your changes and tests.\n```bash\ngit checkout my-new-feature\n```\n\n3. Run linting check and tests with: `poetry run tests`\n4. If it is all ok format it with: `poetry run format`\n4. Commit and open a pull request and request a review from one of the autors.\n\n\n# TODO\n\n- [] ??\n- [] ??\n- [] ??\n- [] ??\n',
    'author': 'loudercake',
    'author_email': 'jxzk@protonmail.com',
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
