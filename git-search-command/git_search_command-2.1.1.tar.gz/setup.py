# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gsc',
 'gsc.core',
 'gsc.data',
 'gsc.data.repository',
 'gsc.data.request',
 'gsc.data.response',
 'gsc.di',
 'gsc.domain.entities',
 'gsc.domain.use_cases',
 'gsc.presentation',
 'gsc.presentation.command_line',
 'gsc.presentation.observer']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3',
 'dependency-injector>=4.0,<5.0',
 'jsonpickle>=2.1.0',
 'python-dotenv>=0.19.2',
 'requests>=2.26.0',
 'rx>=3.2.0',
 'tabulate>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['gsc = gsc:main']}

setup_kwargs = {
    'name': 'git-search-command',
    'version': '2.1.1',
    'description': 'A simple tool to search the content in GitLab and GitHub.',
    'long_description': '# GIT SEARCH COMMAND\n\n[![PyPI](https://img.shields.io/pypi/v/git-search-command?label=PyPi&logo=pypi&logoColor=white)](https://pypi.org/project/git-search-command/)\n[![Last commit](https://img.shields.io/github/last-commit/jamesnguyen46/git-search-command?label=Last%20Commit&logo=github&logoColor=white&color=yellow)](https://github.com/jamesnguyen46/git-search-command/commits/)\n[![Coverage](https://img.shields.io/codecov/c/github/jamesnguyen46/git-search-command?token=HO0BAT95VI&label=Coverage&logo=codecov&logoColor=white)](https://codecov.io/gh/jamesnguyen46/git-search-command)\n[![Github Action](https://img.shields.io/github/workflow/status/jamesnguyen46/git-search-command/Push%20&%20Pull%20Request?label=CI&logo=github-actions&logoColor=white)](https://github.com/jamesnguyen46/git-search-command/actions/workflows/push_pull_request.yml)\n[![License](https://img.shields.io/badge/license-Apache-orange?label=License&logo=apache&logoColor=white)](https://github.com/jamesnguyen46/git-search-command/blob/main/LICENSE)\n\nA simple tool to search the content in your GitLab project or GitHub repositories.\n\n> This project has been implemented for PERSONAL USE. If you want more advanced features like creating issue, pull request ... may be refer to use [GLab](https://gitlab.com/gitlab-org/cli) or [GitHub CLI](https://github.com/cli/cli)\n>\n> ## If this project is helpful for you, show your love ❤️ by putting a ⭐ on this project 😉.\n\n## Prerequisites\n\n1. Install [Python3.7+](https://www.python.org/downloads/).\n2. Create a personal access token on [GitLab](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html) or [GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).\n\n## Installation\n\n```\npython -m pip install --upgrade pip\npython -m pip install git-search-command\n```\n\n## Usage\n\n### Environment\n\nAfter finishing the installation you need to create new environment for searching\n\n```\ngsc gl env --new <environment_name>\n```\n\nThen input your host name and personal token as following\n\n![gsc_setup_env](https://user-images.githubusercontent.com/9126025/205210447-517c3fcc-6b5b-4d39-8c4d-aa89e1dc7ecc.gif)\n\n### Search in GitLab\n\nDefault is to search all projects that you owned.\n\n```\ngsc gl search <keywork>\n```\n\n![gsc_gl_search](https://user-images.githubusercontent.com/9126025/205210438-274af890-4dc3-498b-8cc0-a01621d275ab.gif)\n\nSearch in a specific project\n\n```\ngsc gl search <keywork> --project <project_id>\n```\n\nSearch in a specific group\n\n```\ngsc gl search <keywork> --group <group_id_or_group_path>\n```\n\n### Search in GitHub\n\nDefault is to search all repositories that you owned, not fork repository.\n\n```\ngsc gh search <keywork>\n```\n\n![gsc_gh_search](https://user-images.githubusercontent.com/9126025/205210430-1d495ebf-1538-413e-b3af-a60aeb144603.gif)\n\nSearch in a specific repository\n\n```\ngsc gh search <keywork> --repository <repository_full_name>\n```\n\n### See more\n\nRead the [wiki](https://github.com/jamesnguyen46/git-search-command/wiki) for the detail of `gsc` commands.\n\n## License\n\n```\nCopyright (C) 2022 James Nguyen\n\n   Licensed under the Apache License, Version 2.0 (the "License");\n   you may not use this file except in compliance with the License.\n   You may obtain a copy of the License at\n\n       http://www.apache.org/licenses/LICENSE-2.0\n\n   Unless required by applicable law or agreed to in writing, software\n   distributed under the License is distributed on an "AS IS" BASIS,\n   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n   See the License for the specific language governing permissions and\n   limitations under the License.\n```\n',
    'author': 'jamesnguyen46',
    'author_email': 'thachnguyen1989@gmail.com',
    'maintainer': 'jamesnguyen46',
    'maintainer_email': 'thachnguyen1989@gmail.com',
    'url': 'https://github.com/jamesnguyen46/git-search-command',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
