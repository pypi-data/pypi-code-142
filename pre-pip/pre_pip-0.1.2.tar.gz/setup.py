# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pre_pip']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['pre-pip = pre_pip.cli:cli']}

setup_kwargs = {
    'name': 'pre-pip',
    'version': '0.1.2',
    'description': 'Run some python before your pip commands.',
    'long_description': '<p align="center" style="height: 3em;">\n    <img src="pre-pip.svg" alt="pre-pip" align="center"></img>\n</p>\n<p align="center">\n    <em>Run some python code just before your pip commands.</em>\n</p>\n\n<p align="center">\n<a href="https://github.com/RatulMaharaj/pre-pip/actions/workflows/python-test-zsh.yml" target="_blank">\n    <img src="https://github.com/RatulMaharaj/pre-pip/actions/workflows/python-test-zsh.yml/badge.svg" alt="pytest zsh">\n</a>\n<a href="https://github.com/RatulMaharaj/pre-pip/actions/workflows/python-test-bash.yml" target="_blank">\n    <img src="https://github.com/RatulMaharaj/pre-pip/actions/workflows/python-test-bash.yml/badge.svg" alt="pytest bash">\n</a>\n<a href="https://pypi.org/project/pre-pip" target="_blank">\n    <img src="https://img.shields.io/pypi/v/pre-pip?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n</p>\n\n<hr/>\n\n### Use cases\n\n- Before installing a package, check it against a list of known malicious packages.\n- Upgrade pip automatically before installing a package.\n- Inject pip proxy settings into the environment before installing a package.\n\nYou can use it to run any custom python code before a pip command is executed.\n\n### Supported shells\n\nThe following shells are currently supported:\n\n- `zsh`\n- `bash`\n\nI\'m currently working on adding support for `powershell` and will thereafter look at `fish`.\n\nContributions for any other shells are welcome.\n\n### Installation\n\n```sh\npip install pre-pip\n```\n\nThere is potential to make this `pipx` installable.\n\n### Usage\n\nInstall `pre-pip` into your `.*rc` file using:\n\n```sh\npre-pip install\n```\n\n### Register a custom demo hook\n\nCreate a new file called `hook.py` in your current directory with the following content:\n\n```python\n# hook.py\nfrom rich import print as rprint\n\n\ndef main(args):\n    rprint(\n        f"This [italic green]pre-pip[/italic green] hook received: [italic cyan]{args}[/italic cyan]",\n    )\n\n```\n\nRegister the hook using:\n\n```sh\npre-pip add hook.py\n```\n\nYou can view the list of registered hooks using:\n\n```sh\npre-pip list\n```\n\n### Uninstall\n\nUninstall `pre-pip` using:\n\n```sh\npre-pip uninstall\n```\n\nThis will remove the `pre-pip` hook from your `.*rc` file as well as all registered hooks.\n\nTo remove the pre-pip package, use:\n\n```sh\npip uninstall pre-pip\n```\n\n### License\n\n[MIT](LICENSE)\n',
    'author': 'Ratul Maharaj',
    'author_email': 'ratulmaharaj@looped.co.za',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
