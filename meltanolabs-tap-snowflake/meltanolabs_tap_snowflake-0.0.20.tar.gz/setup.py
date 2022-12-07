# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_snowflake', 'tap_snowflake.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.14.0,<0.15.0',
 'snowflake-connector-python>=2.8.0,<3.0.0',
 'snowflake-sqlalchemy>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['tap-snowflake = tap_snowflake.tap:TapSnowflake.cli']}

setup_kwargs = {
    'name': 'meltanolabs-tap-snowflake',
    'version': '0.0.20',
    'description': '`tap-snowflake` is a Singer tap for Snowflake, built with the Meltano SDK for Singer Taps.',
    'long_description': '# tap-snowflake\n\n`tap-snowflake` is a Singer tap for Snowflake.\n\nBuilt with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.\n\n## Installation\n\n```bash\npipx install git+https://github.com/MeltanoLabs/tap-snowflake.git\n```\n\n## Configuration\n\n### Accepted Config Options\n\nA full list of supported settings and capabilities for this\ntap is available by running:\n\n```bash\ntap-snowflake --about\n```\n\n### Configure using environment variables\n\nThis Singer tap will automatically import any environment variables within the working directory\'s\n`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching\nenvironment variable is set either in the terminal context or in the `.env` file.\n\n### Source Authentication and Authorization\n\nStandard `username` and `password` auth is supported.\n\n### Enabling Batch Messaging\n\nThis tap is built using the Meltano SDK and therefore supports a `BATCH` [message type](https://sdk.meltano.com/en/latest/batch.html), in\naddition to the `RECORD` messages of the Singer spec. This can be enabled either by adding the following to your `config.json`:\n\n```json\n{\n  // ...\n  "batch_config": {\n    "encoding": {\n      "format": "jsonl",\n      "compression": "gzip"\n    },\n    "storage": {\n      "root": "file://tests/core/resources",\n      "prefix": "test-batch"\n    }\n  }\n}\n```\n\nor its equivalent to your `meltano.yml`\n\n```yaml\nconfig:\n  plugins:\n    extractors:\n      - name: tap-snowflake\n        config:\n          batch_config:\n            encoding:\n              format: jsonl\n              compression: gzip\n            storage:\n              root: "file://tests/core/resources"\n              prefix: test-batch\n```\n\n**Note:** This variant of `tap-snowflake` does not yet support the `INCREMENTAL` replication strategy in `BATCH` mode. Follow [here](https://github.com/meltano/sdk/issues/976#issuecomment-1257848119) for updates.\n\n## Usage\n\nYou can easily run `tap-snowflake` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Tap Directly\n\n```bash\ntap-snowflake --version\ntap-snowflake --help\ntap-snowflake --config CONFIG --discover > ./catalog.json\n```\n\n## Developer Resources\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `tap_snowflake/tests` subfolder and\nthen run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `tap-snowflake` CLI interface directly using `poetry run`:\n\n```bash\npoetry run tap-snowflake --help\n```\n\n### Testing with [Meltano](https://www.meltano.com)\n\n_**Note:** This tap will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd tap-snowflake\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke tap-snowflake --version\n# OR run a test `elt` pipeline:\nmeltano elt tap-snowflake target-jsonl\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to\ndevelop your own taps and targets.\n',
    'author': 'Ken Payne',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
