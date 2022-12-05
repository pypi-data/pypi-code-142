# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['norske_kommuner']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'norske-kommuner',
    'version': '0.1.1',
    'description': 'Pydantic models on Norwegian municipalities (Norske kommuner).',
    'long_description': '# Norske Kommuner\n![PyPI - Status](https://img.shields.io/pypi/status/norske-kommuner)\n[![Download Stats](https://img.shields.io/pypi/dm/norske-kommuner)](https://pypistats.org/packages/poetry)\n\nPydantic models on Norwegian municipalities (Norske kommuner).\n\n```python\nfrom norske_kommuner import kommuner, get_kommune_by_nr\n\n#  Loop over all kommuner:\nfor kommune in kommuner.values():\n    print(kommune)\n\n#  Get kommunenummer\nprint (kommuner[\'Stavanger\'].kommunenummer) # 1103\n\n# Can also get kommune by kommunenr\nprint(get_kommune_by_nr(\'1103\')) #  Stavanger\n\n# Each kommune is a pydantic model and have pydantic functionality like exporting to json\nprint(kommuner[\'Stavanger\'].json())\n\n```\n\nLast line will output\n```json\n{\n    "avgrensningsboks": {\n        "coordinates":  [[[5.49903313381, 58.884658939559], [5.49903313381, 59.312103554166], [6.131310442607, 59.312103554166], [6.131310442607, 58.884658939559], [5.49903313381, 58.884658939559]]],\n        "crs": {\n            "properties": {\n                "name": "EPSG:4258"\n            },\n            "type": "name"\n        },\n        "type": "Polygon"\n    },\n    "fylkesnavn": "Rogaland",\n    "fylkesnummer": "11",\n    "gyldigeNavn": [\n        {\n            "navn": "Stavanger",\n            "prioritet": 1,\n            "sprak": "Norwegian"\n        },\n        {\n            "navn": null,\n            "prioritet": 2,\n            "sprak": null\n        },\n        {\n            "navn": null,\n            "prioritet": 3,\n            "sprak": null\n        }\n    ],\n    "kommunenavn": "Stavanger",\n    "kommunenavnNorsk": "Stavanger",\n    "kommunenummer": "1103",\n    "punktIOmrade": {\n        "coordinates": [\n            5.712610778068,\n            59.10201328799\n        ],\n        "crs": {\n            "properties": {\n                "name": "EPSG:4258"\n            },\n            "type": "name"\n        },\n        "type": "Point"\n    },\n    "samiskForvaltningsomrade": false\n}\n```\n\n>Uses data and models from "[Åpent API fra Kartverket for administrative enheter](https://ws.geonorge.no/kommuneinfo/v1/)"',
    'author': 'Anders Steen',
    'author_email': 'anders.steen@knowit.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AndersSteenNilsen/norske-kommuner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
