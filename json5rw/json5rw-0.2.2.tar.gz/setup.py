# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json5rw']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'json5rw',
    'version': '0.2.2',
    'description': 'A tool for JSON5 I/O',
    'long_description': '# `json5rw` - A JSON5 parsing tool\n\nThis tool supports loading and dumping JSON 5 content\n\n## Supported syntax\n\nCurrently, the following are supported:\n\n- Comments\n    - `//`\n    - `/**/`\n- Different numerals\n    - Hex (`0xABC`)\n    - Int (`100`)\n    - Float (`12.34`)\n    - NaN (`NaN`, `nan`)\n    - Infinity (`Infinity`, `-Infinity`)\n- Trailing commas\n\n*Note: Unquoted keys are not supported*',
    'author': 'Andy Zhang',
    'author_email': 'andy@nwsoft.tk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
