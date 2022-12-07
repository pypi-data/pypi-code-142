# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poltergeist']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poltergeist',
    'version': '0.2.1',
    'description': 'Experimental Rust-like error handling in Python, with type-safety in mind.',
    'long_description': '# poltergeist\n\n[![pypi](https://img.shields.io/pypi/v/poltergeist.svg)](https://pypi.python.org/pypi/poltergeist)\n[![versions](https://img.shields.io/pypi/pyversions/poltergeist.svg)](https://github.com/alexandermalyga/poltergeist)\n\nExperimental Rust-like error handling in Python, with type-safety in mind.\n\n## Installation\n\n```\npip install poltergeist\n```\n\n## Examples\n\nUse the provided `@poltergeist` decorator on any function:\n\n```python\nfrom pathlib import Path\nfrom poltergeist import Err, Ok, poltergeist\n\n@poltergeist(FileNotFoundError)\ndef read_text(path: Path) -> str:\n    return path.read_text()\n\nresult = read_text(Path("test.txt"))\n\n# Handle errors using structural pattern matching\nmatch result:\n    case Ok(content):\n        # Type-checkers know that content is a string,\n        # carried over from the return type of the original function.\n        print("File content:", content)\n    case Err(e):\n        # The exception type is also known\n        print("File not found:", e.filename)\n\n# Or directly get the returned value\n# This will raise the original exception, if there was one\ncontent = result.unwrap()\n```\n\nYou can also wrap errors yourself:\n\n```python\nfrom pathlib import Path\nfrom poltergeist import Err, Ok, Result\n\ndef read_text(path: Path) -> Result[str, FileNotFoundError]:\n    try:\n        return Ok(path.read_text())\n    except FileNotFoundError as e:\n        return Err(e)\n```\n\nBoth of these examples pass type checking and provide in-editor autocompletion.\n',
    'author': 'Alexander Malyga',
    'author_email': 'alexander@malyga.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexandermalyga/poltergeist',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
