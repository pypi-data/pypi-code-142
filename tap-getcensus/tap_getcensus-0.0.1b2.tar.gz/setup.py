# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_getcensus']

package_data = \
{'': ['*']}

install_requires = \
['singer-sdk==0.14.0']

entry_points = \
{'console_scripts': ['tap-getcensus = tap_getcensus.tap:TapCensus.cli']}

setup_kwargs = {
    'name': 'tap-getcensus',
    'version': '0.0.1b2',
    'description': 'Singer tap for the Census Operational Analytics Platform, built with the Meltano SDK for Singer Taps.',
    'long_description': '<div align="center">\n\n# tap-getcensus\n\n<div>\n  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/tap-getcensus/main">\n    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/tap-getcensus/main.svg"/>\n  </a>\n  <a href="https://github.com/edgarrmondragon/tap-getcensus/blob/main/LICENSE">\n    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/tap-getcensus"/>\n  </a>\n</div>\n\nSinger Tap for the [Census Operational Analytics Platform](https://www.getcensus.com/). Built with the [Meltano Singer SDK](https://sdk.meltano.com).\n\n</div>\n\n## Capabilities\n\n* `catalog`\n* `state`\n* `discover`\n* `about`\n* `stream-maps`\n* `schema-flattening`\n\n## Settings\n\n| Setting             | Required | Default | Description |\n|:--------------------|:--------:|:-------:|:------------|\n| api_token           | True     | None    | Auth token for getcensus.com API |\n| stream_maps         | False    | None    | Config object for stream maps capability. |\n| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |\n| flattening_enabled  | False    | None    | \'True\' to enable schema flattening and automatically expand nested properties. |\n| flattening_max_depth| False    | None    | The max depth to flatten schemas. |\n\nA full list of supported settings and capabilities is available by running: `tap-getcensus --about`\n\n## Streams\n\n| Stream                | Replication Method | Replication Key | Primary Key | Documentation |\n|:----------------------|:------------------:|:---------------:|:-----------:|:-------------:|\n| `syncs`               | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/syncs#get-syncs |\n| `sync_runs`           | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/sync-runs#get-syncs-id-sync_runs |\n| `destinations`        | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/destinations#get-destinations |\n| `destination_objects` | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/destination-objects#get-destinations-id-objects |\n| `sources`             | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/sources#get-sources |\n| `source_objects`      | Full Table         | None            | id          | https://docs.getcensus.com/basics/api/source-objects#get-sources-id-objects |\n\nThe full catalog is available by running: `tap-getcensus --discover`\n\n### Source Authentication and Authorization\n\nSee the [API docs](https://docs.getcensus.com/basics/api#getting-api-access).\n\n## Usage\n\nYou can easily run `tap-getcensus` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-getcensus --version\ntap-getcensus --help\ntap-getcensus --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tests` subfolder and then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-getcensus` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-getcensus --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-getcensus\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-getcensus --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-getcensus target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to\ndevelop your own taps and targets.\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'Edgar Ramírez-Mondragón',
    'maintainer_email': 'edgarrm358@gmail.com',
    'url': 'https://github.com/edgarrmondragon/tap-getcensus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)
