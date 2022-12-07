# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_shortcut']

package_data = \
{'': ['*']}

install_requires = \
['singer-sdk==0.14.0', 'toolz==0.12.0']

entry_points = \
{'console_scripts': ['tap-shortcut = tap_shortcut.tap:TapShortcut.cli']}

setup_kwargs = {
    'name': 'tap-shortcut',
    'version': '0.0.1a1',
    'description': '`tap-shortcut` is a Singer tap for Shortcut, built with the Meltano SDK for Singer Taps.',
    'long_description': '<div align="center">\n\n# tap-shortcut\n\n<div>\n  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/tap-shortcut/main">\n    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/tap-shortcut/main.svg"/>\n  </a>\n  <a href="https://github.com/edgarrmondragon/tap-shortcut/blob/main/LICENSE">\n    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/tap-shortcut"/>\n  </a>\n</div>\n\nSinger tap for Shortcut. Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.\n\n</div>\n\n## Capabilities\n\n* `catalog`\n* `state`\n* `discover`\n* `about`\n* `stream-maps`\n\n## Settings\n\n| Setting | Required | Default | Description    |\n|:--------|:--------:|:-------:|:---------------|\n| token   | True     | None    | Shortcut Token |\n\nA full list of supported settings and capabilities is available by running: `tap-shortcut --about`\n\n### Source Authentication and Authorization\n\nSee https://developer.shortcut.com/api/rest/v3#Authentication.\n\n## Usage\n\nYou can easily run `tap-shortcut` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-shortcut --version\ntap-shortcut --help\ntap-shortcut --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tests` subfolder and then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-shortcut` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-shortcut --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-shortcut\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-shortcut --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-shortcut target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to\ndevelop your own taps and targets.\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/edgarrmondragon/tap-shortcut',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)
