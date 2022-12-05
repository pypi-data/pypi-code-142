# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['smpp_gateway', 'smpp_gateway.management.commands', 'smpp_gateway.migrations']

package_data = \
{'': ['*']}

install_requires = \
['RapidSMS>=2.0', 'django>=3.2,<4.0', 'psycopg2>=2.8', 'smpplib>=2.2']

setup_kwargs = {
    'name': 'smpp-gateway',
    'version': '1.0.1',
    'description': '',
    'long_description': '# rapidsms-smpp-gateway\n\nA [RapidSMS](https://rapidsms.readthedocs.io/en/latest/) SMPP gateway.\n\n## Management commands\n\n### `smpp_client`\n\nStart an SMPP client instance:\n\n```shell\npython manage.py smpp_client smppsim\n```\n\nExample configuration using environment variables:\n\n```shell\nexport PGDATABASE=libya_elections\nexport DATABASE_URL=postgresql://localhost/$PGDATABASE\nexport SMPPLIB_HOST=localhost\nexport SMPPLIB_PORT=2775\nexport SMPPLIB_SYSTEM_ID=smppclient1\nexport SMPPLIB_PASSWORD=password\nexport SMPPLIB_SUBMIT_SM_PARAMS=\'{"foo": "bar"}\'\n```\n\n### `listen_mo_messages`\n\nListen for mobile-originated (MO) messages:\n\n```shell\npython manage.py listen_mo_messages --channel new_mo_msg\n```\n\n## Publish\n\n1. Update `pyproject.toml` with the version number\n2. Update `CHANGES.md` with release notes\n3. Create a new release and tag on GitHub. A `publish` Github Actions workflow is configured to run on tag creation.\n\nOr use Poetry\'s [publish](https://python-poetry.org/docs/cli/#publish) command:\n   ```sh\n   poetry config pypi-token.pypi <get-from-pypi>\n   poetry build\n   poetry publish\n   ```\n',
    'author': 'Caktus Group',
    'author_email': 'team@caktusgroup.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/caktus/rapidsms-smpp-gateway',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
