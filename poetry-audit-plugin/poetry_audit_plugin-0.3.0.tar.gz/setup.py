# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_audit_plugin']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0,<2.0.0', 'safety>=2.2.0,<3.0.0']

entry_points = \
{'poetry.application.plugin': ['poetry-audit-plugin = '
                               'poetry_audit_plugin.plugin:AuditApplicationPlugin']}

setup_kwargs = {
    'name': 'poetry-audit-plugin',
    'version': '0.3.0',
    'description': 'Poetry plugin for checking security vulnerabilities in dependencies',
    'long_description': "# Poetry Audit Plugin\n\nPoetry plugin for checking security vulnerabilities in dependencies based on [safety](https://github.com/pyupio/safety).\n\n```\n$ poetry audit\nScanning 19 packages...\n\n  • ansible-runner     installed 1.1.2  affected <1.3.1   CVE PVE-2021-36995\n  • ansible-tower-cli  installed 3.1.8  affected <3.2.0   CVE CVE-2020-1733 \n  • jinja2             installed 2.0    affected <2.11.3  CVE CVE-2020-28493\n\n3 vulnerabilities found\n```\n\n## Installation\n\nThe easiest way to install the `export` plugin is via the `plugin add` command of Poetry.\n\n```bash\npoetry plugin add poetry-audit-plugin\n```\n\nIf you used `pipx` to install Poetry you can add the plugin via the `pipx inject` command.\n\n```bash\npipx inject poetry poetry-audit-plugin\n```\n\nOtherwise, if you used `pip` to install Poetry you can add the plugin packages via the `pip install` command.\n\n```bash\npip install poetry-audit-plugin\n```\n\n## Available options\n\n* `--json`: Export the result in JSON format.\n\n* `--ignore-code`: Ignore some vulnerabilities IDs. Receive a list of IDs. For example:\n```bash\npoetry audit --ignore-code=CVE-2022-42969,CVE-2020-10684\n```\n\n* `--ignore-package`: Ignore some packages. Receive a list of packages. For example:\n```bash\npoetry audit --json --ignore-package=py,ansible-tower-cli\n```\n## Exit codes\n\n`poetry audit` will exit with a code indicating its status.\n\n* `0`: Vulnerabilities were not found.\n* `1`: One or more vulnerabilities were found.\n\n## Develop poetry-audit-plugin\n\nYou can read this document to setup an environment to develop poetry-audit-plugin.\n\nFirst step is to install Poetry. Please read [official document](https://python-poetry.org/docs/) and install Poetry in your machine.\n\nThen, you can install dependencies of poetry-audit-plugin with the following command.\n\n```sh\npoetry install\n```\n\nOnce you've done it, you can start developing poetry-audit-plugin. You can use test assets for the testing.\n\n```sh\ncd tests/assets/no_vulnerabilities\npoetry audit\n```\n\nPlease lint, format, and test your changes before creating pull request to keep the quality.\n\n```sh\n./scripts/lint.sh\n./scripts/format.sh\n./scripts/test.sh\n```\n\n## Contribution\n\nHelp is always appreciated. Please feel free to create issue and pull request!\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n",
    'author': 'opeco17',
    'author_email': 'opeco17@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/opeco17/poetry-audit-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
