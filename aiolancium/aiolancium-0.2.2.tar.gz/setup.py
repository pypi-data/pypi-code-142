# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiolancium',
 'aiolancium.interfaces',
 'aiolancium.resources',
 'aiolancium.utilities']

package_data = \
{'': ['*']}

install_requires = \
['jsonref>=1.0.0,<2.0.0', 'pyjwt<=2.4.0', 'simple-rest-client==0.5.4']

extras_require = \
{'doc': ['sphinx-rtd-theme>=1.1.1,<2.0.0',
         'sphinxcontrib-contentui>=0.2.5,<0.3.0',
         'sphinx==4.3.1'],
 'test': ['flake8-bugbear==22.9.23',
          'black<=22.8.0',
          'aioresponses>=0.7.3,<0.8.0',
          'flake8>=5.0.4,<6.0.0']}

setup_kwargs = {
    'name': 'aiolancium',
    'version': '0.2.2',
    'description': 'AsyncIO Client for Lancium',
    'long_description': '[![Build Status](https://github.com/giffels/aiolancium/actions/workflows/unittests.yaml/badge.svg)](https://github.com/giffels/aiolancium/actions/workflows/unittests.yaml)\n[![Verification](https://github.com/giffels/aiolancium/actions/workflows/verification.yaml/badge.svg)](https://github.com/giffels/aiolancium/actions/workflows/verification.yaml)\n[![codecov](https://codecov.io/gh/giffels/aiolancium/branch/main/graph/badge.svg)](https://codecov.io/gh/giffels/aiolancium)\n[![Documentation Status](https://readthedocs.org/projects/aiolancium/badge/?version=latest)](https://aiolancium.readthedocs.io/en/latest/?badge=latest)\n[![PyPI version](https://badge.fury.io/py/aiolancium.svg)](https://badge.fury.io/py/aiolancium)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiolancium.svg?style=flat-square)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/giffels/aiolancium/blob/master/LICENSE)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# aiolancium\n\naiolancium is a simplistic python REST client for the Lancium Compute REST API utilizing asyncio. The client itself has\nbeen developed against the [Lancium Compute REST API documentation](https://lancium.github.io/compute-api-docs/api.html).\n\n## Installation\naiolancium can be installed via [PyPi](https://pypi.org/) using\n\n```bash\npip install aiolancium\n```\n\n## How to use aiolancium\n\n```python\nfrom aiolancium.auth import Authenticator\nfrom aiolancium.client import LanciumClient\n\n# Authenticate yourself against the API and refresh your token if necessary\nauth = Authenticator(api_key="<your_api_key>")\n\n# Initialise the actual client\nclient = LanciumClient(api_url="https://portal.lancium.com/api/v1/", auth=auth)\n\n# List details about the `lancium/ubuntu` container\nawait client.images.list_image("lancium/ubuntu")\n\n# Create your hellow world first job.\njob = {"job": {"name": "GridKa Test Job",\n                   "qos": "high",\n                   "image": "lancium/ubuntu",\n                   "command_line": \'echo "Hello World"\',\n                   "max_run_time": 600}}\n\nawait client.jobs.create_job(**job)\n\n# Show all your jobs and their status in Lancium compute\njobs = await client.jobs.show_jobs()\n\nfor job in jobs["jobs"]:\n    # Retrieve the stdout/stdin output of your finished jobs\n    await client.jobs.download_job_output(job["id"], "stdout.txt")\n    await client.jobs.download_job_output(job["id"], "stderr.txt")\n    \n    # or download them to disk\n    await client.download_file_helper("stdout.txt", "stdout.txt", job["id"])\n    await client.download_file_helper("stderr.txt", "stderr.txt", job["id"])\n\n# Delete all your jobs in Lancium compute\nfor job in jobs["jobs"]:\n    await client.jobs.delete_job(id=job["id"])\n```\n\nIn order to simplify file uploads and downloads to/from the Lancium compute platform, an upload/download helper method \nhas been added to the client. \nThe upload helper takes care of reading a file in binary format and uploading it in 32 MB chunks (default) to the \nLancium persistent storage. The download helper downloads a file from the Lancium persistent storage to the local disks.\nThe download helper also supports the download of jobs outputs (stdout.txt, stderr.txt) to local disk (see example \nabove).\nUnfortunately, streaming of data is not support by the underlying `simple-rest-client`. Thus, the entire file is \ndownloaded to memory before writing to the disk.\n\n```python\nfrom aiolancium.auth import Authenticator\nfrom aiolancium.client import LanciumClient\n\n# Authenticate yourself against the API and refresh your token if necessary\nauth = Authenticator(api_key="<your_api_key>")\n\n# Initialise the actual client\nclient = LanciumClient(api_url="https://portal.lancium.com/api/v1/", auth=auth)\n\n# Upload /bin/bash to /test on the Lancium persistent storage\nawait client.upload_file_helper(path="test", source="/bin/bash")\n\n# Get information about the uploaded file\nawait client.data.get_file_info("/test")\n\n# Download the file again\nawait client.download_file_helper("/test", destination="test_downloaded_again")\n\n# Delete the uploaded file again, the \narg = {"file-path": "/test"}\nawait client.data.delete_data_item(**arg)\n\n# Alternative approach to delete the uploaded file\nawait client.data.delete_data_item("/test")\n```\n',
    'author': 'Manuel Giffels',
    'author_email': 'giffels@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
