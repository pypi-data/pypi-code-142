# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.gus', 'src.impacts']

package_data = \
{'': ['*'], 'src.gus': ['inputs/*', 'outputs/trees_yearly.json']}

install_requires = \
['fuzzywuzzy>=0.18.0,<0.19.0',
 'ipython>=7.27.0,<8.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'mesa>=0.8.9,<0.9.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.3,<2.0.0',
 'portray>=1.7.0,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'termcolor>=2.1.1,<3.0.0']

setup_kwargs = {
    'name': 'pygus',
    'version': '0.1.8',
    'description': 'Green Urban Scenarios - A digital twin representation, simulation of urban forests and their impact analysis.',
    'long_description': '# gus\nGreen Urban Scenarios - A digital twin representation, simulation of urban forests and their impact analysis.\n\n## install GUS from Test-PyPi\n\n```\nimport sys\n!{sys.executable} -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple gus==0.1.7\n```\n',
    'author': 'Bulent Ozel',
    'author_email': 'bulent@lucidminds.ai',
    'maintainer': 'Oguzhan Yayla',
    'maintainer_email': 'oguzhan@lucidminds.ai',
    'url': 'https://github.com/lucidmindsai/gus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
