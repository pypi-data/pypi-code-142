# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['announcer']

package_data = \
{'': ['*']}

install_requires = \
['mistletoe>=0.7.1,<0.9.0', 'requests>=2.19,<3.0']

entry_points = \
{'console_scripts': ['announce = announcer.__init__:main']}

setup_kwargs = {
    'name': 'announcer',
    'version': '4.0.1',
    'description': 'Announce changes in keepachangelog-style CHANGELOG.md files to Slack and Microsoft Teams',
    'long_description': '[![Github build](https://img.shields.io/github/workflow/status/metaswitch/announcer/Announcer)](https://github.com/Metaswitch/announcer)\n[![pypi version](https://img.shields.io/pypi/v/announcer)](https://pypi.org/project/announcer/)\n[![docker pulls](https://img.shields.io/docker/pulls/metaswitch/announcer)](https://hub.docker.com/r/metaswitch/announcer)\n\n# announcer\n\nThis tool:\n* takes an [keepachangelog](https://keepachangelog.com/en/1.0.0/)-style CHANGELOG.md file\n* extracts all changes for a particular version\n* and sends a formatted message to a Slack or Microsoft Teams webhook.\n\nIt is available as a Python package, or as a Docker container for use in CI.\n\n## Installation\n\nInstall this tool using pip:\n\n```\npip install announcer\n```\n\n## Tool usage\n\n```\nusage: announce [-h] (--webhook WEBHOOK | --slackhook WEBHOOK) [--target {slack,teams}] --changelogversion CHANGELOGVERSION --changelogfile CHANGELOGFILE --projectname PROJECTNAME [--username USERNAME] [--iconurl ICONURL | --iconemoji ICONEMOJI]\n\nAnnounce CHANGELOG changes on Slack and Microsoft Teams\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --webhook WEBHOOK     The incoming webhook URL\n  --slackhook WEBHOOK   The incoming webhook URL. (Deprecated)\n  --target {slack,teams}\n                        The type of announcement that should be sent to the webhook\n  --changelogversion CHANGELOGVERSION\n                        The changelog version to announce (e.g. 1.0.0)\n  --changelogfile CHANGELOGFILE\n                        The file containing changelog details (e.g. CHANGELOG.md)\n  --projectname PROJECTNAME\n                        The name of the project to announce (e.g. announcer)\n  --username USERNAME   The username that the announcement will be made as (e.g. announcer). Valid for: Slack\n  --iconurl ICONURL     A URL to use for the user icon in the announcement. Valid for: Slack\n  --iconemoji ICONEMOJI\n                        An emoji code to use for the user icon in the announcement (e.g. party_parrot). Valid for: Slack\n```\n\n## Gitlab Usage\n\nAnnouncer builds and publishes a Docker image that you can integrate into your `.gitlab-ci.yml`:\n\n```\nannounce:\n  stage: announce\n  image: metaswitch/announcer:4.0.1\n  script:\n   - announce --webhook <webhook address>\n              --changelogversion $CI_COMMIT_REF_NAME\n              --changelogfile <CHANGELOG.md file>\n              --projectname <Project name>\n              --iconemoji party_parrot\n  only:\n    - tags\n```\n',
    'author': 'Max Dymond',
    'author_email': 'max.dymond@metaswitch.com',
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
