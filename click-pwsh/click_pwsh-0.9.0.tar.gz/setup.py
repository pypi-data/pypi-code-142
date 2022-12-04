# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['click_pwsh']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0']

setup_kwargs = {
    'name': 'click-pwsh',
    'version': '0.9.0',
    'description': 'A click extension to support shell completion for PowerShell 7',
    'long_description': "# PS> click-pwsh\n\nA [click](https://github.com/pallets/click) extension to support shell completion for **[PowerShell 7](https://github.com/PowerShell/PowerShell)**.\n\nThis extension is written based on click **8.x** (i.e., the rewritten click's completion system). Be aware of your click version before using it.\n\nHope it can provide smooth experiences for Windows users. d(`･∀･)b\n\n## Installation\n\nYou can get the package from PyPI:\n\n```bash\nPS> pip install click-pwsh\n```\n\n## Quickstart\n\nAdd the following code at the top of your script:\n\n```python\nfrom click_pwsh import support_pwsh_shell_completion\nsupport_pwsh_shell_completion()\n```\n\nAnd run the following command to install the shell completion:\n\n```bash\nPS> python -m click_pwsh install foo-bar\nComplete.\n```\n\nwhere `foo-bar` is your command name.\n\nThen ... all done. Re-open PowerShell 7 and enjoy the shell completion!\n",
    'author': 'Yu-Kai Lin',
    'author_email': 'stephen359595@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StephLin/click-pwsh',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
