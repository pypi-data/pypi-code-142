# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uuid25']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'uuid25',
    'version': '0.1.1',
    'description': '25-digit case-insensitive UUID encoding',
    'long_description': '# Uuid25: 25-digit case-insensitive UUID encoding\n\n[![PyPI](https://img.shields.io/pypi/v/uuid25)](https://pypi.org/project/uuid25/)\n[![License](https://img.shields.io/pypi/l/uuid25)](https://github.com/uuid25/python/blob/main/LICENSE)\n\nUuid25 is an alternative UUID representation that shortens a UUID string to just\n25 digits using the case-insensitive Base36 encoding. This library provides\nfunctionality to convert from the conventional UUID formats to Uuid25 and vice\nversa.\n\n```python\nfrom uuid25 import Uuid25\n\n# convert from/to string\na = Uuid25.parse("8da942a4-1fbe-4ca6-852c-95c473229c7d")\nassert a.value == "8dx554y5rzerz1syhqsvsdw8t"\nassert a.to_hyphenated() == "8da942a4-1fbe-4ca6-852c-95c473229c7d"\n\n# convert from/to 128-bit byte array\nb = Uuid25.from_bytes(bytes([0xFF] * 16))\nassert b.value == "f5lxx1zz5pnorynqglhzmsp33"\nassert all([x == 0xFF for x in b.to_bytes()])\n\n# convert from/to other popular textual representations\nc = [\n    Uuid25.parse("e7a1d63b711744238988afcf12161878"),\n    Uuid25.parse("e7a1d63b-7117-4423-8988-afcf12161878"),\n    Uuid25.parse("{e7a1d63b-7117-4423-8988-afcf12161878}"),\n    Uuid25.parse("urn:uuid:e7a1d63b-7117-4423-8988-afcf12161878"),\n]\nassert all([x.value == "dpoadk8izg9y4tte7vy1xt94o" for x in c])\n\nd = Uuid25.parse("dpoadk8izg9y4tte7vy1xt94o")\nassert d.to_hex() == "e7a1d63b711744238988afcf12161878"\nassert d.to_hyphenated() == "e7a1d63b-7117-4423-8988-afcf12161878"\nassert d.to_braced() == "{e7a1d63b-7117-4423-8988-afcf12161878}"\nassert d.to_urn() == "urn:uuid:e7a1d63b-7117-4423-8988-afcf12161878"\n\n# convert from/to standard uuid module\'s UUID value\nimport uuid\n\nuuid_module = uuid.UUID("f38a6b1f-576f-4c22-8d4a-5f72613483f6")\ne = Uuid25.from_uuid(uuid_module)\nassert e.value == "ef1zh7jc64vprqez41vbwe9km"\nassert e.to_uuid() == uuid_module\n\n# generate UUIDv4 in Uuid25 format (backed by uuid module)\nimport uuid25\n\nprint(uuid25.gen_v4())  # e.g. "99wfqtl0z0yevxzpl4hv2dm5p"\n```\n\n## License\n\nLicensed under the Apache License, Version 2.0.\n',
    'author': 'LiosK',
    'author_email': 'contact@mail.liosk.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/uuid25/python',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
