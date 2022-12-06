# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['panoptisch']

package_data = \
{'': ['*']}

install_requires = \
['anytree>=2.8.0,<3.0.0']

entry_points = \
{'console_scripts': ['panoptisch = panoptisch:main']}

setup_kwargs = {
    'name': 'panoptisch',
    'version': '0.1.1',
    'description': 'A recursive Python dependency scanner.',
    'long_description': " ## Panoptisch: A recursive dependency scanner for Python projects\n\n####  ⚠️🚨 Early stage! May not work as expected 🚨⚠️\n#### What?\nPanoptisch scans your Python file or module to find it's imports (aka dependencies) and recursively does so for all dependencies and sub-dependencies.\nIt then generates a dependency tree in JSON for you to parse and enforce import policies.\nImports are resolved by mimicing Python's import system. It's completely static besides the importing of modules to find the location of its source file(s).\n\n##### Please NOTE:\nThere are known **limitations and issues** at this stage. Please read this before using Panoptisch.  \nSee: ``LIMITATIONS.md`` [LINK](LIMITATIONS.md).\n\n\n#### Motivation\nI was not able to find a proper dependency scanner for Python. Panoptisch was born out of the need to accurately verify dependency usage accross an entire project.  \nIt's aim is to generate a JSON report that can be parsed and evaluated to **assert import policies**.  \nFor example, you may want to restrict ``os``, ``socket``, ``sys`` and ``importlib`` imports to selected packages.\n\n\n#### Usage\n\n1. Install ``Panoptisch`` in the same virtual environment as your project, this is important!  \n```\npip install panoptisch\n```\n\n2. Use\n```\nusage: panoptisch <module>\n\npositional arguments:\n  module                Name of module or file you wish to scan.\n\noptions:\n  -h, --help            show this help message and exit.\n  --show-stdlib-dir     Prints the automatically resolved stdlib directory.\n  --max-depth MAX_DEPTH\n                        Maximum dependency depth.\n  --out OUT             File to output report.\n  --auto-stdlib-dir     Ignore stdlib modules by automatically resolving their path. MAY BE BUGGY. Try running panoptisch <module_name> --show-stdlib-dir to see the directory before using this.\n  --stdlib-dir STDLIB_DIR Ignore stdlib modules by providing their path.\n  --omit-not-found      Do not include modules that could not be resolved in report.\n```\nA typical run may be\n```\n$ panoptisch <module or file> --max-depth 5 --omit-not-found\n```\n3. See report\n```\n$ more out.json\n```\n#### LICENSE\nAll work is licensed under the [GNU General Public License Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html).\n\n#### Contributing\nFeedback, contributions and issues welcome. \n\n",
    'author': 'aarnav',
    'author_email': 'aarnavbos@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/R9295/panoptisch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
