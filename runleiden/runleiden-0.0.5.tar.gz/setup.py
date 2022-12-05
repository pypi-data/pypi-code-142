# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['runleiden']

package_data = \
{'': ['*']}

install_requires = \
['leidenalg>=0.9.0,<0.10.0', 'structlog>=22.1.0,<23.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['runleiden = runleiden.runleiden:entry_point']}

setup_kwargs = {
    'name': 'runleiden',
    'version': '0.0.5',
    'description': 'Wrapper over leidenalg',
    'long_description': 'runleiden\n================\n\nWrapper over `leidenalg`.\n\n## Install\n\n```bash\npoetry install\npoetry shell # activate virtualenv\n```\n\n## Run Script\n\n```bash\nrunleiden -i input_edgelist.txt -r resolution_value -o output_communities.txt\n```',
    'author': 'runeblaze',
    'author_email': 'runeblaze@excite.co.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
