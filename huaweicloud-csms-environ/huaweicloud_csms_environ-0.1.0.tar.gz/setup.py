# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['csms']

package_data = \
{'': ['*']}

install_requires = \
['huaweicloudsdkcsms>=3.1.0,<4.0.0']

setup_kwargs = {
    'name': 'huaweicloud-csms-environ',
    'version': '0.1.0',
    'description': '',
    'long_description': "# huaweicloud-csms-environ\n\n[![GitHub](https://img.shields.io/github/license/C0D1UM/huaweicloud-csms-environ)](https://github.com/C0D1UM/huaweicloud-csms-environ/blob/main/LICENSE)\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/C0D1UM/huaweicloud-csms-environ/CI)](https://github.com/C0D1UM/huaweicloud-csms-environ/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/C0D1UM/huaweicloud-csms-environ/branch/main/graph/badge.svg?token=PN19DJ3SDF)](https://codecov.io/gh/C0D1UM/huaweicloud-csms-environ)\n[![PyPI](https://img.shields.io/pypi/v/huaweicloud-csms-environ)](https://pypi.org/project/huaweicloud-csms-environ/)  \n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/huaweicloud-csms-environ)](https://github.com/C0D1UM/huaweicloud-csms-environ)\n\n## Installation\n\n```bash\npip install huaweicloud-csms-environ\n```\n\n## Sample Usage\n\n```python\nimport csms\n\n# basic\ncsms.load_env('secret-name', region='ap-southeast-2')\n\n# project id instead of region\ncsms.load_env('secret-name', project_id='project-id')\n\n# using pure environment variables\ncsms.load_env()\n\n# no environment variables\ncsms.load_env(\n   'secret_name',\n   access_key='access-key',\n   secret_key='secret-key',\n   region='ap-southeast-2',\n)\n```\n\n## Environment Variables\n\n| Key                          | SDK | Description                    |\n| ---------------------------- | --- | ------------------------------ |\n| `HUAWEICLOUD_SDK_AK`         | Yes | Access key of Huawei Cloud IAM |\n| `HUAWEICLOUD_SDK_SK`         | Yes | Secret key of Huawei Cloud IAM |\n| `HUAWEICLOUD_SDK_PROJECT_ID` | Yes | Huawei Cloud project ID        |\n| `HUAWEICLOUD_REGION`         | No  | Huawei Cloud region            |\n| `HUAWEICLOUD_SECRET_NAME`    | No  | CSMS secret name               |\n\n> For more SDK variables, please see [this](https://github.com/huaweicloud/huaweicloud-sdk-python-v3#241-environment-variables-top).\n\n## Development\n\n### Requirements\n\n- Docker\n- Python\n- Poetry\n\n### Linting\n\n```bash\nmake lint\n```\n\n### Testing\n\n```bash\nmake test\n```\n\n### Fix Formatting\n\n```bash\nmake yapf\n```\n",
    'author': 'CODIUM',
    'author_email': 'support@codium.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/C0D1UM/huaweicloud-csms-environ',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
