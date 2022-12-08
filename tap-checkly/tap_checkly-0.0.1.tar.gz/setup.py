# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_checkly']

package_data = \
{'': ['*']}

install_requires = \
['singer-sdk>=0.14.0,<0.15.0']

entry_points = \
{'console_scripts': ['tap-checkly = tap_checkly.tap:TapCheckly.cli']}

setup_kwargs = {
    'name': 'tap-checkly',
    'version': '0.0.1',
    'description': 'Singer tap for Checkly, built with the Meltano SDK for Singer Taps.',
    'long_description': '<div align="center">\n\n# tap-checkly\n\n<div>\n  <a href="https://results.pre-commit.ci/latest/github/edgarrmondragon/tap-checkly/main">\n    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/edgarrmondragon/tap-checkly/main.svg"/>\n  </a>\n  <a href="https://github.com/edgarrmondragon/tap-checkly/blob/main/LICENSE">\n    <img alt="License" src="https://img.shields.io/github/license/edgarrmondragon/tap-checkly"/>\n  </a>\n</div>\n\nSinger Tap for [Checkly](https://www.checklyhq.com/). Built with the [Meltano Singer SDK](https://sdk.meltano.com).\n\n</div>\n\n## Capabilities\n\n* `catalog`\n* `state`\n* `discover`\n* `about`\n* `stream-maps`\n* `schema-flattening`\n\n## Settings\n\n| Setting             | Required | Default | Description |\n|:--------------------|:--------:|:-------:|:------------|\n| account_id          | True     | None    | Checkly Account ID |\n| token               | True     | None    | API Token for Checkly |\n| start_date          | False    | None    | Earliest datetime to get data from |\n| include_paid_streams| False    |       0 | Include streams that require a paid Checkly plan |\n| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |\n| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |\n| flattening_enabled  | False    | None    | \'True\' to enable schema flattening and automatically expand nested properties. |\n| flattening_max_depth| False    | None    | The max depth to flatten schemas. |\n\nA full list of supported settings and capabilities is available by running: `tap-checkly --about`\n\n## API Coverage\n\n| API Endpoint                  | Supported | Notes                     |\n| :---------------------------- | :-------: | :------------------------ |\n| `/v1/alert-channels`          |    ✅     |                            |\n| `/v1/alert-notifications`     |    ✅     |  Payment required          |\n| `/v1/checks`                  |    ✅     |                            |\n| `/v1/check-alerts`            |    ✅     |                            |\n| `/v1/check-groups`            |    ✅     |                            |\n| `/v1/check-results/{checkId}` |    N/A    | [Heavily rate-limited][1] |\n| `/v1/dashboards`              |    ✅     |                            |\n| `/v1/locations`               |    ✅     |                            |\n| `/v1/maintenance-windows`     |    ✅     |                            |\n| `/v1/private-locations`       |    ✅     |                            |\n| `/v1/runtimes`                |    ✅     |                            |\n| `/v1/snippets`                |    ✅     |                            |\n| `/v1/variables`               |    ✅     |                            |\n\nA full list of supported settings and capabilities is available by running: `tap-checkly --about`\n\n### Source Authentication and Authorization\n\n## Usage\n\nYou can easily run `tap-checkly` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-checkly --version\ntap-checkly --help\ntap-checkly --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tests` subfolder and then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-checkly` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-checkly --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created.\nInstall Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-checkly\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-checkly --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-checkly target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to develop your own taps and targets.\n\n[1]: https://developers.checklyhq.com/reference/getv1checkresultscheckid\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'Edgar Ramírez-Mondragón',
    'maintainer_email': 'edgarrm358@gmail.com',
    'url': 'https://github.com/edgarrmondragon/tap-checkly',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)
