# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xcodelocalize']

package_data = \
{'': ['*']}

install_requires = \
['mtranslate>=1.8,<2.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['xcodelocalize = xcodelocalize.main:run']}

setup_kwargs = {
    'name': 'xcodelocalize',
    'version': '1.0.0',
    'description': 'Tool for automatic search and localization of .strings files',
    'long_description': '# XCodeLocalize\n\n## Requirments \n\nPython3.9+\n\n## Installation\n\n### Using pip:\n```\npip3 install xcodelocalize \n```\n\n## Usage\n\n### Prepare a project\n\nGo to the project settings, add the desired localization languages. Create localization files for all selected languages.\n\n### Localize\n\n`cd` to project root folder and run\n\n```\nxcodelocalize [OPTIONS]\n```\n\nor\n\n```\npython3 -m xcodelocalize [OPTIONS]\n```\n\n### Options\n\n* `--base-language`: code of the language from which all strings will be translated. _[default: \'en\']_\n\n* `--override / --no-override`: a boolean value that indicates whether strings that already exist in the file will be translated. Retranslate if `override`, skip if `no-override`. _[default: no-override]_\n\n* `--file`: Names of the strings files to be translated. Multiple files can be specified. If not specified, all files will be translated. _[default: None]_ \n```\nxcodelocalize --file Info\nxcodelocalize --file Info --file MainStoryboard --file Localizable \n```\n\n* `--key`: Keys of the strings to be translated. Multiple keys can be specified. If not specified, all keys will be translated. _[default: None]_\n\n* `--language`: Language codes of the strings files to be translated. Multiple language codes can be specified. If not specified, all files will be translated. _[default: None]_\n\n* `--log-level`: One from [progress|errors|group|string].  _[default: group]_\n\n* `--help`: Show info\n\n## Features:\n\n* The tool looks for .strings files in the current directory recursively, grouping and translating fully automatically. You can even run it in the root directory and localize all your projects at once.\n\n* Regular .strings, Info.plist, storyboards and intentdefinition files are supported.\n\n* Formated strings with %@ are supported.\n\n* Multiline strings are supported.\n\n* Key and value must **not contain double quotes `"`**. Other quotes are supported.\n\n* Comments are supported and will be copied to all files. Comments must **not contain substrings in localizable strings format with comment, such as `/*[comment]*/ "[key]" = "[value]";`**.\n\n## Automation\n\nYou can go to `Target -> Build Phases -> New Run Script Phase` in your xcode project and paste `xcodelocalize` there. It will localize necessary strings during build and your localization files will always be up to date.\n',
    'author': 'MarkParker5',
    'author_email': 'markparker.it@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/xcodelocalize/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
