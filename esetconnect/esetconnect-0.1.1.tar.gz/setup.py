# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['esetconnect', 'esetconnect.models', 'esetconnect.urls']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'esetconnect',
    'version': '0.1.1',
    'description': '',
    'long_description': '# ESET Connect\n\n## API Docs\nhttp://epcpublicapi-test.westeurope.cloudapp.azure.com/swagger/\n\n## Quickstart\n\n### Install\n```bash\npip install esetconnect\n```\n\n### Get detections\n```python\nfrom esetconnect import EsetConnect\n\nUSERNAME = "username"\nPASSWORD = "password"\n\nwith EsetConnect(USERNAME, PASSWORD) as ec:\n    for detection in ec.get_detections().detections:\n        print(detection.json())\n```\n\n```json\n{\n   "category":"DETECTION_CATEGORY_UNSPECIFIED",\n   "context":{\n      "circumstances":"Event occurred on a modified file.",\n      "device_uuid":"83c7522f-f4a7-4a80-a055-8e1329201129",\n      "process":{\n         "path":"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe"\n      },\n      "user_name":"DESKTOP-7DAP322\\\\username"\n   },\n   "display_name":"Eicar",\n   "network_communication":null,\n   "object_hash_sha1":"3395856CE81F2B7382DEE72602F798B642F14140",\n   "object_name":"file:///C:/Users/username/AppData/Local/Temp/2f7545df-d894-4768-8741-944d7ef059f6.tmp",\n   "object_type_name":"File",\n   "object_url":"",\n   "occur_time":"2022-12-07T09:26:13",\n   "responses":{\n      "description":null,\n      "device_restart_required":null,\n      "display_name":null,\n      "protection_name":null\n   },\n   "severity_level":"SEVERITY_LEVEL_MEDIUM",\n   "type_name":"nil",\n   "uuid":"ec879237-d1c3-3742-ecab-05fed9ea9a58"\n}\n```\n',
    'author': 'Donny Maasland',
    'author_email': 'donny@unauthorizedaccess.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
