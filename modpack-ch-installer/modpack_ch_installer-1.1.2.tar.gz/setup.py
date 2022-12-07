# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['modpack_ch_installer']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['mci = modpack_ch_installer.main:cli',
                     'modpackchinstaller = modpack_ch_installer.main:cli']}

setup_kwargs = {
    'name': 'modpack-ch-installer',
    'version': '1.1.2',
    'description': '',
    'long_description': '# modpack_ch_installer\n###### The simple way to install a modpack server\n\n## Install\n\n`pip install modpack-ch-installer`\n\n## Usage \n\n```\nUsage: modpackchinstaller [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  install\n  update\n\n**mci also works\n```',
    'author': 'Spencer',
    'author_email': '75862693+TacoMonkey11@users.noreply.github.com',
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
