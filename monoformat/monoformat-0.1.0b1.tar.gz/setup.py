# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['monoformat']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0', 'isort>=5.10.1,<6.0.0', 'node-edge>=0.1.0b2,<0.2.0']

entry_points = \
{'console_scripts': ['monoformat = monoformat.__main__:__main__']}

setup_kwargs = {
    'name': 'monoformat',
    'version': '0.1.0b1',
    'description': 'A tool that formats all kinds of languages consistently',
    'long_description': '# Monoformat\n\nOpinionated and "zero config" formatters like Black and Prettier are amazing in\nthe sense that they remove any need for thinking about formatting. However, they\nstill require you to:\n\n-   Be used separately (one is Python and the other is Node)\n-   Be configured for the language version and so forth\n\nMonoformat does this automatically. You can only use the language version that\nmonoformat allows and you can configure literally nothing except which files\nit\'s going to reformat and which it\'s not.\n\n## Installation\n\nMonoformat is available on PyPI:\n\n```bash\npip install monoformat\n```\n\n## Usage\n\nMonoformat is a command line tool. You can run it with:\n\n```bash\nmonoformat .\n```\n\nThis will reformat all files in the current directory and its subdirectories.\n\nIt will take care to avoid `.git` and other special directories. There is a\ndefault pattern embedded but you can change it with the `--do-not-enter` flag,\nwhich is a pattern matching folder or file names you don\'t want to consider.\n\n## Supported languages\n\nMonoformat supports the following languages:\n\n-   **Python** (Black)\n-   **JavaScript** (Prettier)\n-   **TypeScript** (Prettier)\n-   **JSON** (Prettier)\n-   **Markdown** (Prettier)\n-   **YAML** (Prettier)\n-   **HTML** (Prettier)\n-   **CSS** (Prettier)\n-   **SCSS** (Prettier)\n-   **Vue** (Prettier)\n-   **Svelte** (Prettier)\n-   **PHP** (Prettier)\n',
    'author': 'Rémy Sanchez',
    'author_email': 'remy.sanchez@hyperthese.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Xowap/Monoformat',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
