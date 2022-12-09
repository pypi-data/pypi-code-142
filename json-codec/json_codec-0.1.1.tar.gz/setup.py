# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json_codec', 'json_codec.codecs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'json-codec',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Json Codec\n\nIt\'s a simple library to encode and decode json to strict python types using dataclasses and builtin python types.\n\n## Installation\n\n```bash\npip install json-codec\n\npoetry add json-codec\n```\n\n## Usage\n\n### Parse a simple primitive type\n\n```python\nfrom json_codec import decode\nimport json\n\nassert decode(json.loads("true"), bool) is True\nassert decode(json.loads("false"), bool) is False\nassert decode(json.loads("null"), Optional[bool]) is None\nassert decode(json.loads("1"), int) == 1\nassert decode(json.loads("1"), Decimal) == Decimal("1")\nassert decode(json.loads(\'"1.1"\'), Decimal) == Decimal("1.1")\nassert decode(json.loads(\'"1.1"\'), float) == 1.1\nassert decode(json.loads(\'"1.1"\'), str) == "1.1"\n\nassert decode(json.loads(\'[1,1]\'), List[int]) == [1, 1]\n```\n\n### Parse a dataclass\n\n```python\nfrom dataclasses import dataclass\nfrom json_codec import decode\n\n@dataclass(frozen=True)\nclass User:\n    name: str\n    age: int\n\nassert decode({"name": "John", "age": 30}, User) == User(name="John", age=30)\n\n\n@dataclass\nclass Dummy:\n    text_list: List[str]\n    text_dict: Dict[str, Decimal]\n    optional_text: Optional[str]\n\ndummy_json_text = """\n{\n    "text_list": ["a", "b", "c"],\n    "text_dict": {\n        "a": 1.0,\n        "b": 2,\n        "c": "3.3",\n        "d": 2.2\n    },\n    "optional_text": "hello"\n}\n"""\n\ndummy_json = json.loads(dummy_json_text)\n\nparsed = decode(dummy_json, Dummy)\n\nassert parsed.text_list == ["a", "b", "c"]\nassert parsed.text_dict["a"] == Decimal("1.0")\nassert parsed.text_dict["b"] == Decimal("2.0")\nassert parsed.text_dict["c"] == Decimal("3.3")\nassert parsed.text_dict["d"].quantize(Decimal("1.0")) == Decimal("2.2")\nassert parsed.optional_text == "hello"\n```\n\n### Parse a dataclass with a nested dataclass\n\n```python\n @dataclass\nclass NestedDummy:\n    text: str\n    number: Decimal\n\n    boolean: bool\n\n@dataclass\nclass Dummy:\n    text_list: List[str]\n    text_dict: Dict[str, Decimal]\n    nested: NestedDummy\n\ndummy_json_text = """\n{\n\n    "text_list": ["a", "b", "c"],\n    "text_dict": {\n        "a": 1.0,\n        "b": 2,\n        "c": "3.3",\n        "d": 2.2\n    },\n    "nested": {\n        "text": "hello",\n        "number": 1.1,\n        "boolean": true\n    }\n}\n"""\n\ndummy_json = json.loads(dummy_json_text)\n\nparsed = decode(dummy_json, Dummy)\n\nassert parsed.text_list == ["a", "b", "c"]\nassert parsed.text_dict["a"] == Decimal("1.0")\nassert parsed.text_dict["b"] == Decimal("2.0")\nassert parsed.text_dict["c"] == Decimal("3.3")\nassert parsed.text_dict["d"].quantize(Decimal("1.0")) == Decimal("2.2")\nassert parsed.nested.text == "hello"\nassert parsed.nested.number.quantize(Decimal("1.0")) == Decimal("1.1")\nassert parsed.nested.boolean is True\n```\n\n### Parse a newtype\n\n```python\nfrom json_codec import decode\nfrom typing import NewType\n\nUserId = NewType("UserId", int)\n\nassert decode(json.loads("1"), UserId) == UserId(1)\nassert isinstance(decode(json.loads("1"), UserId), UserId)\n\n```',
    'author': 'Lucas Silva',
    'author_email': 'lucas76leonardo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
