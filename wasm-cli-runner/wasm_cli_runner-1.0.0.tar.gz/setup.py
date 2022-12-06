# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wasm_cli_runner']

package_data = \
{'': ['*']}

install_requires = \
['wasmtime>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'wasm-cli-runner',
    'version': '1.0.0',
    'description': 'Run WebAssembly Binary and Text files in the command line.',
    'long_description': '# WASM CLI Runner\n\nRun WebAssembly Binary or Text files (`.wat` or `.wasm`) directly from the command line.\n\nImported functions to WebAssembly are at the moment:\n- "print" (`(import "" "print" (func $print (param i32)))`)\n\nTo run a WebAssembly file, use:\n```\nwasm_cli_runner test.wat\n```\n\n\n## Installation\n\n\n### Via pip\n\n```\npip install wasm_cli_runner\n```\n\n### From source\n\nTo run this program from the code directly, [`python`](https://www.python.org/) and [`poetry`](https://python-poetry.org/) (`pip install poetry`) are required. Clone or download the repository.\n\nTo install all the dependencies, use your command line and navigate to the directory where this `README` file is located in. Then run\n\n```bash\npoetry install\n```\n\n## Execution\n\nTo execute the program use\n```bash\npoetry run python -m wasm_cli_runner\n```\n',
    'author': 'miile7',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
