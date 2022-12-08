# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['comdaan', 'comdaan_fetch']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=2.3.2,<2.4.0',
 'multiprocess>=0.70,<0.71',
 'networkx>=2.2,<2.3',
 'pandas>=1.4.4,<2.0.0',
 'python-gitlab>=1.11,<1.12',
 'scipy>=1.3,<1.4',
 'statsmodels==0.11.0']

entry_points = \
{'console_scripts': ['comdaan_fetch = comdaan_fetch:main']}

setup_kwargs = {
    'name': 'comdaan',
    'version': '0.1.7',
    'description': 'This is a suite of tools for conducting analysis from data produced by FOSS',
    'long_description': "ComDaAn: Community Data Analysis\n================================\n\nThis is a suite of tools for conducting analysis from data produced by FOSS\ncommunities. This is currently mainly focusing on git repositories.\n\nDependencies\n------------\nThe scripts in this repository depend on the following python modules:\n * pandas: https://pandas.pydata.org\n * networkx: https://networkx.github.io\n * bokeh: https://bokeh.pydata.org\n\nThey are commonly available via pip or your OS packaging system.\nYou can run `pipenv install` to install them in a pipenv managed virtualenv.\n\nIf you plan to develop on it we advise using `pipenv install -d` to also\nbring `black` which we use for the formatting. Make sure to run it on new\ncode before submitting your contribution.\n\nRunning\n-------\nThe scripts require you to provide at least one path to a checked-out git\nrepository. One than more path can be provided. The scripts also work with\ndirectories containing a tree of git repositories and will traverse them all.\nThis is a convenient way to analyze teams working across more than one\nrepository.\n\nFor a description of the other options, please run the scripts with the `--help`\nargument.\n\nAcknowledgment\n--------------\nThe git log parsing code is heavily based on code from Paul Adams' git-viz\nproject: https://github.com/therealpadams/git-viz\n\nThe ideas behind activity.py and network.py are also influenced by git-viz.\n\n",
    'author': 'communities. This is currently mainly focusing on git repositories.n',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
