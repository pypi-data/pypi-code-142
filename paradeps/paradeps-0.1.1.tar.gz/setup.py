# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['paradeps']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['deps = deps.__main__:main']}

setup_kwargs = {
    'name': 'paradeps',
    'version': '0.1.1',
    'description': 'Resolves dependencies into tiers suitable for parallel work',
    'long_description': '# paradeps\n\n## Overview\n\nThis resolves dependencies into parallelizable execution tiers.  For example, given the inputs:\n\n    a, b, c, d, f\n\nWhere a and b depend on f, this will return:\n\n    [{c,d,f}, {a,b}]\n\n\n## Requirements\n\nPython 3.10+\n\n\n## Installation\n\n    pip install paradeps\n\nOr download the *.whl files and install it with `pip install *.whl`.\n\n\n## Usage\n\n    from paradeps import Dependent\n\n    class Item(Dep):\n       ...\n\n    def process_items_in_parallel(items):\n       ...\n\n    items = [Item() for i in range(5)]\n\n    items[0].add_dependency(items[2])\n    items[2].add_dependency(items[4])\n\n    tiers = resolve_deps(items)\n\n    for tier in tiers:\n        process_items_in_parallel(tier)\n\n\n## License\n\nReleased under the terms of Affero GPL version 3.0 only.  See `LICENSE.txt` for further details.\n\n\n## Authors / Contact\n\nEmail mailto::leebraid@gmail.com[mailto::leebraid@gmail.com].\n\n',
    'author': 'Lee Braiden',
    'author_email': 'leebraid@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
