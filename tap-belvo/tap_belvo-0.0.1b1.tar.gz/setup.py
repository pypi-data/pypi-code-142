# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_belvo', 'tap_belvo.openapi', 'tap_belvo.streams']

package_data = \
{'': ['*']}

install_requires = \
['belvo-python>=0.35.0,<0.36.0',
 'requests-cache>=0.9.7,<0.10.0',
 'singer-sdk==0.15.0']

entry_points = \
{'console_scripts': ['tap-belvo = tap_belvo.tap:TapBelvo.cli']}

setup_kwargs = {
    'name': 'tap-belvo',
    'version': '0.0.1b1',
    'description': '`tap-belvo` is a Singer tap for Belvo, built with the Meltano SDK for Singer Taps.',
    'long_description': '# `tap-belvo`\n\nSinger tap for Belvo.\n\nBuilt with the [Meltano Singer SDK](https://sdk.meltano.com).\n\n## Capabilities\n\n* `catalog`\n* `state`\n* `discover`\n* `about`\n* `stream-maps`\n* `schema-flattening`\n\n## Settings\n\n| Setting             | Required | Default | Description |\n|:--------------------|:--------:|:-------:|:------------|\n| secret_id           | True     | None    | Belvo API secret ID. |\n| password            | True     | None    | Belvo API password. |\n| start_date          | False    | None    | Earliest datetime to get data from |\n| base_url            | False    | https://development.belvo.com | Base URL for the Belvo API |\n| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |\n| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |\n| flattening_enabled  | False    | None    | \'True\' to enable schema flattening and automatically expand nested properties. |\n| flattening_max_depth| False    | None    | The max depth to flatten schemas. |\n\nA full list of supported settings and capabilities is available by running: `tap-belvo --about`\n\n### Source Authentication and Authorization\n\n- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.\n\n## Usage\n\nYou can easily run `tap-belvo` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-belvo --version\ntap-belvo --help\ntap-belvo --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tests` subfolder and then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-belvo` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-belvo --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-belvo\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-belvo --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-belvo target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to\ndevelop your own taps and targets.\n',
    'author': 'Edgar Ramírez-Mondragón',
    'author_email': 'edgarrm358@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/edgarrmondragon/tap-belvo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.12',
}


setup(**setup_kwargs)
