# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schemamodels']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'schemamodels',
    'version': '0.3.0a0',
    'description': 'Dynamically create useful data classes from JSON schemas',
    'long_description': '# Schema Models\n\n![PyPI](https://img.shields.io/pypi/v/schemamodels?style=for-the-badge) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/schemamodels?style=for-the-badge)\n\nDynamically created data classes from JSON schemas\n\n\nUse this library to quickly turn a JSON Schema and turn into a Python dataclass that you can immediately consume.\n\n\n## Installation\n\nInstall this package using the usual suspects.\n\n```\npip install schemamodels\n```\n\n## Usage\n\nAssuming you have a JSON schema like:\n\n```json\n    {\n        "$id": "https://schema.dev/fake-schema.schema.json",\n        "$schema": "http://json-schema.org/draft-07/schema#",\n        "title": "fake-schema",\n        "description": "Blue Blah",\n        "type": "object",\n        "properties": {\n            "property_a": {\n              "default": 5,\n              "type": "integer"\n            },\n            "property_b": {\n              "type": "string"\n            }\n        }\n    }\n```\n\n```python\nfrom schemamodels import SchemaModelFactory\n\n\nschema_string = \'..\'\nmy_json_schema = json.loads(schema_string)\n\nfactory = SchemaModelFactory()\nfactory.register(my_json_schema)\n```\n\n\nUse your new dataclass\n\n```python\nfrom schemamodels.dynamic import FakeSchema\n\nyour_data_instance = FakeSchema(property_a="hello")\n\n```\n\n## Rationale\n\n### The JSON Schema can come from anywhere\n\nRegardless of where the JSON schema originated, it only needs to be valid for the Draft version you care about. There are a number of libraries better suited validating a JSON Schema document. A user of this library would obtain a JSON Schema document using their prefered method (filesystem, remote), then pass it to this library.\n\n\n### Just-enough validation\n\nAt this time, I\'m not interested in validating a JSON Schema. However, there are some basic checks I\'d like to have performed _every time_ create a new instance of a object that\'s designed to _hold_ my data. Also, questions about the quality of the data is out of scope.\n\nI want to have the confidence that the data has a structure the adhears to the rules provided by a JSON Schema.\n\nI want to be sure that the dictionary exported by these data classes would pass validation checks. The specific tool used to validate an instance of data against the original JSON Schema shouldn\'t matter.\n\n### I\'m tired of writing Python classes by hand\n\nWhile I like using Python-classes to write Python declaratively, I think letting JSON Schema drive the data models creates an opportunity to automate.\n\nWhen I have a valid JSON Schema, I can create a new Python dataclass with zero or one-line of code.\n',
    'author': "'Jurnell Cockhren'",
    'author_email': 'jurnell@civichacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
