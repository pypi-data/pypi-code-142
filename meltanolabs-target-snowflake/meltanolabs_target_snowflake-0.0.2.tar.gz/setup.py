# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['target_snowflake', 'target_snowflake.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.13.0,<0.14.0',
 'snowflake-sqlalchemy>=1.4.1,<2.0.0']

entry_points = \
{'console_scripts': ['target-snowflake = '
                     'target_snowflake.target:TargetSnowflake.cli']}

setup_kwargs = {
    'name': 'meltanolabs-target-snowflake',
    'version': '0.0.2',
    'description': '`target-snowflake` is a Singer target for Snowflake, built with the Meltano SDK for Singer Targets.',
    'long_description': '# target-snowflake\n\n`target-snowflake` is a Singer target for Snowflake.\n\nBuild with the [Meltano Target SDK](https://sdk.meltano.com).\n\n## Installation\n\n- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.\n\n```bash\npipx install target-snowflake\n```\n\n## Configuration\n\n### Accepted Config Options\n\n- [ ] `Developer TODO:` Provide a list of config options accepted by the target.\n\nA full list of supported settings and capabilities for this\ntarget is available by running:\n\n```bash\ntarget-snowflake --about\n```\n\n### Configure using environment variables\n\nThis Singer target will automatically import any environment variables within the working directory\'s\n`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching\nenvironment variable is set either in the terminal context or in the `.env` file.\n\n### Source Authentication and Authorization\n\n- [ ] `Developer TODO:` If your target requires special access on the source system, or any special authentication requirements, provide those here.\n\n## Usage\n\nYou can easily run `target-snowflake` by itself or in a pipeline using [Meltano](https://meltano.com/).\n\n### Executing the Target Directly\n\n```bash\ntarget-snowflake --version\ntarget-snowflake --help\n# Test using the "Carbon Intensity" sample:\ntap-carbon-intensity | target-snowflake --config /path/to/target-snowflake-config.json\n```\n\n## Developer Resources\n\n- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.\n\n### Initialize your Development Environment\n\n```bash\npipx install poetry\npoetry install\n```\n\n### Create and Run Tests\n\nCreate tests within the `target_snowflake/tests` subfolder and\n  then run:\n\n```bash\npoetry run pytest\n```\n\nYou can also test the `target-snowflake` CLI interface directly using `poetry run`:\n\n```bash\npoetry run target-snowflake --help\n```\n\n### Testing with [Meltano](https://meltano.com/)\n\n_**Note:** This target will work in any Singer environment and does not require Meltano.\nExamples here are for convenience and to streamline end-to-end orchestration scenarios._\n\nYour project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in\nthe file.\n\nNext, install Meltano (if you haven\'t already) and any needed plugins:\n\n```bash\n# Install meltano\npipx install meltano\n# Initialize meltano within this directory\ncd target-snowflake\nmeltano install\n```\n\nNow you can test and orchestrate using Meltano:\n\n```bash\n# Test invocation:\nmeltano invoke target-snowflake --version\n# OR run a test `elt` pipeline with the Carbon Intensity sample tap:\nmeltano elt tap-carbon-intensity target-snowflake\n```\n\n### SDK Dev Guide\n\nSee the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the Meltano SDK to\ndevelop your own Singer taps and targets.\n',
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
