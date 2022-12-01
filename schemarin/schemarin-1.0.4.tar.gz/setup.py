# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['schemarin', 'schemarin.schemes.tools']

package_data = \
{'': ['*'],
 'schemarin': ['schemes/*',
               'schemes/.github/*',
               'schemes/Xresources/*',
               'schemes/alacritty/*',
               'schemes/backgrounds/*',
               'schemes/dynamic-colors/*',
               'schemes/electerm/*',
               'schemes/freebsd_vt/*',
               'schemes/kitty/*',
               'schemes/konsole/*',
               'schemes/lxterminal/*',
               'schemes/mobaxterm/*',
               'schemes/pantheonterminal/*',
               'schemes/putty/*',
               'schemes/remmina/*',
               'schemes/royalts/*',
               'schemes/schemes/*',
               'schemes/screenshots/*',
               'schemes/terminal/*',
               'schemes/terminator/*',
               'schemes/termite/*',
               'schemes/tilda/*',
               'schemes/vscode/*',
               'schemes/wezterm/*',
               'schemes/windowsterminal/*',
               'schemes/xfce4terminal/*',
               'schemes/xrdb/*'],
 'schemarin.schemes.tools': ['templates/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'colorama>=0.4.6,<0.5.0',
 'colour>=0.1.5,<0.2.0',
 'halo>=0.0.31,<0.0.32',
 'inflect>=6.0.2,<7.0.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'loctocat>=1.0.2,<2.0.0',
 'path>=16.5.0,<17.0.0',
 'pygit2>=1.11.1,<2.0.0',
 'pygithub>=1.57,<2.0',
 'pyperclip>=1.8.2,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'validators>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['schemarin = schemarin.schemarin:cli']}

setup_kwargs = {
    'name': 'schemarin',
    'version': '1.0.4',
    'description': 'A color scheme manager for iTerm2',
    'long_description': "# Schemarin\n\nSchemarin is a color scheme manager for [iTerm2](https://iterm2.com) that should really be installed with \n[Homebrew](https://brew.sh) rather than pip.\n\n```bash\nbrew tap celsiusnarhwal/htt\nbrew install schemarin\n```\n\nSchemarin is published on PyPI **for technical reasons only** and is not intended to be installed with pip or other\nPython package managers.\n\nFor more information, [check out Schemarin's GitHub repository](https://schemarin.celsiusnarhwal.dev).",
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://schemarin.celsiusnarhwal.dev',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
