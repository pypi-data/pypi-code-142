# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['documented']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'documented',
    'version': '0.1.3',
    'description': 'Templated docstrings for Python classes.',
    'long_description': '# documented\n\n[![Coverage](https://coveralls.io/repos/github/anatoly-scherbakov/documented/badge.svg?branch=master)](https://coveralls.io/github/anatoly-scherbakov/documented?branch=master)\n[![Python Version](https://img.shields.io/pypi/pyversions/documented.svg)](https://pypi.org/project/documented/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n![PyPI - License](https://img.shields.io/pypi/l/documented)\n\nTemplated docstrings for Python classes.\n\n## Features\n\n- Describe your business logic in docstrings of your classes and exceptions;\n- When printing an object or an exception, the library will substitute the placeholders in the docstring text with runtime values,\n- And you (or your user) will see a human-readable text.\n\n## Installation\n\n```bash\npip install documented\n```\n\n\n## Example\n\n```python\nfrom dataclasses import dataclass\nfrom documented import DocumentedError\n\n\n@dataclass\nclass InsufficientWizardryLevel(DocumentedError):\n    """\n    🧙 Your level of wizardry is insufficient ☹\n\n        Spell: {self.spell}\n        Minimum level required: {self.required_level}\n        Actual level: {self.actual_level} {self.comment}\n\n    Unseen University will be happy to assist in your training! 🎓\n    """\n\n    spell: str\n    required_level: int\n    actual_level: int\n\n    @property\n    def comment(self) -> str:\n        if self.actual_level <= 0:\n            return \'(You are Rincewind, right? Hi!)\'\n        else:\n            return \'\'\n\n\nraise InsufficientWizardryLevel(\n    spell=\'Animal transformation\',\n    required_level=8,\n    actual_level=0,\n)\n```\n\nwhich prints:\n\n```\n---------------------------------------------------------------------\nInsufficientWizardryLevel           Traceback (most recent call last)\n<ipython-input-1-d8ccdb953cf6> in <module>\n     27 \n     28 \n---> 29 raise InsufficientWizardryLevel(\n     30     spell=\'Animal transformation\',\n     31     required_level=8,\n\nInsufficientWizardryLevel: \n🧙 Your level of wizardry is insufficient ☹\n\n    Spell: Animal transformation\n    Minimum level required: 8\n    Actual level: 0 (You are Rincewind, right? Hi!)\n\nUnseen University will be happy to assist in your training! 🎓\n```\n\nFor more examples, see: https://anatoly-scherbakov.github.io/documented/\n\nThis project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package).\n',
    'author': 'Anatoly Scherbakov',
    'author_email': 'altaisoft@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anatoly-scherbakov/documented',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
