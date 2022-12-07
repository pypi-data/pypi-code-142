# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['papermerge_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'papermerge-restapi-client>=1.0.19,<2.0.0']

entry_points = \
{'console_scripts': ['papermerge-cli = papermerge_cli.main:cli']}

setup_kwargs = {
    'name': 'papermerge-cli',
    'version': '0.2.2',
    'description': 'Command line utility for your Papermerge DMS instance',
    'long_description': "# Papermerge Cli\n\nCommand line utility which uses REST API to interact with your Papermerge DMS instance\n\n## Install\n\n    $ pip install papermerge-cli\n\n## Usage\n\nGet you REST API authentication token from your instance:\n\n    $ papermerge-cli --host=https://mydms.some-vps.com auth\n\nOr you can provide host as environment variable:\n\n    $ export PAPERMERGE_CLI__HOST=https://mydms.some-vps.com\n    $ papermerge-cli auth\n\nPapermerge Cli will prompt you for username and password. On successfull\nauthentication your REST API token will be displayed - now you can use\nthis token for all subsequent authentications.\n\nUse token for authentication by exporting token as PAPERMERGE_CLI__TOKEN environment\nvariable:\n\n    $ export PAPERMERGE_CLI__TOKEN=mytoken\n\n### list\n\nNow, with `PAPERMERGE_CLI__HOST` and `PAPERMERGE_CLI__TOKEN` environment variables\nset you can use list content of you home folder:\n\n    $ papermerge-cli list\n\nIn order to list content of specific folder (including inbox folder):\n\n    $ papermerge-cli list --parent-uuid=UUID-of-the-folder\n\n### me\n\nIn order to see current user details (current user UUID, home folder UUID, inbox folder UUID, username etc):\n\n    $ papermerge-cli me\n\n### pref-list\n\nList all preferences:\n\n    $ papermerge-cli pref-list\n\nList specific section of the preferences\n\n    $ papermerge-cli pref-list --section=ocr\n\nShow value of preference `trigger` from section `ocr`:\n\n    $ papermerge-cli pref-list --section=ocr --name=trigger\n\n### pref-update\n\nUpdate value of the preference `trigger` from section `ocr`:\n\n    $ papermerge-cli pref-update --section=ocr --name=trigger --value=auto\n\n\n### import\n\nRecursively imports folder from local filesystem. For example, in order\nto import recursively all documents from local folder:\n\n    $ papermerge-cli import /path/to/local/folder/\n\nYou can also import one single document\n\n    $ papermerge-cli import /path/to/some/document.pdf\n\n### search\n\nSearch for node (document or folder) by text or by tags:\n\n    $ papermerge-cli search -q apotheke\n\nReturns all documents (or folders with such title) containing OCRed text 'apotheke'.\n\nYou can search by tags only:\n\n    $ papermerge-cli search --tags important\n\nWill search for all documents (and folders) which were tagged with tag 'important'\nWhen multiple tags are provided, by default, will search for nodes with all mentioned tags:\n\n    $ papermerge-cli search --tags important,letters  # returns nodes with both tags important AND letters\n\nIn case you want to search for nodes with ANY of the provided tags, use `tags-op` parameter:\n\n    $ papermerge-cli search --tags important,letters --tags-op any\n\nFinally, `tags` and `q` may be combined:\n\n    $ papermerge-cli search --tags important -q apartment\n",
    'author': 'Eugen Ciur',
    'author_email': 'eugen@papermerge.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
