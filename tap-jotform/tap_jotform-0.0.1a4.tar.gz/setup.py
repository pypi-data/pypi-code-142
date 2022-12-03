# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_jotform']

package_data = \
{'': ['*']}

install_requires = \
['colorama==0.4.6',
 'requests-cache==0.9.7',
 'singer-sdk==0.14.0',
 'structlog==22.3.0']

entry_points = \
{'console_scripts': ['tap-jotform = tap_jotform.tap:TapJotform.cli']}

setup_kwargs = {
    'name': 'tap-jotform',
    'version': '0.0.1a4',
    'description': 'Singer tap for Jotform, built with the Meltano SDK for Singer Taps.',
    'long_description': '# `tap-jotform`\n\nSinger Tap for Jotform.\n\nBuilt with the [Meltano Singer SDK](https://sdk.meltano.com).\n\n## Capabilities\n\n* `catalog`\n* `state`\n* `discover`\n* `about`\n* `stream-maps`\n* `schema-flattening`\n\n## Settings\n\n| Setting             | Required | Default | Description |\n|:--------------------|:--------:|:-------:|:------------|\n| api_key             | True     | None    | Authentication key. See https://api.jotform.com/docs/#authentication |\n| api_url             | False    | https://api.jotform.com | API Base URL |\n| user_agent          | False    | tap-jotform/0.0.1 | User-Agent header |\n| start_date          | False    | None    | Start date for data collection |\n| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |\n| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |\n| flattening_enabled  | False    | None    | \'True\' to enable schema flattening and automatically expand nested properties. |\n| flattening_max_depth| False    | None    | The max depth to flatten schemas. |\n\nA full list of supported settings and capabilities is available by running: `tap-jotform --about`\n\n### Source Authentication and Authorization\n\nTo generate an API key, follow the instructions in https://api.jotform.com/docs/#gettingstarted.\n\n## Usage\n\nYou can easily run `tap-jotform` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-jotform --version\ntap-jotform --help\ntap-jotform --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tap_jotform/tests` subfolder and\n  then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-jotform` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-jotform --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-jotform\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-jotform --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-jotform target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to\ndevelop your own taps and targets.\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'Edgar Ramírez-Mondragón',
    'maintainer_email': 'edgarrm358@gmail.com',
    'url': 'https://github.com/edgarrmondragon/tap-jotform',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
