# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudeventful']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'cloudeventful',
    'version': '2.1.2',
    'description': 'Broker agnostic library to associate JSON Schemas to message broker topics.',
    'long_description': '<!--suppress HtmlDeprecatedAttribute -->\n<div align=center>\n  <h1>Cloud Eventful</h1>\n  <h3>Broker agnostic library to associate JSON Schemas to message broker topics.</h3>\n  <img src="https://img.shields.io/badge/License-MIT-blue.svg"\n   height="20"\n   alt="License: MIT">\n  <img src="https://img.shields.io/badge/code%20style-black-000000.svg"\n   height="20"\n   alt="Code style: black">\n  <img src="https://img.shields.io/pypi/v/cloudeventful.svg"\n   height="20"\n   alt="PyPI version">\n  <img src="https://img.shields.io/badge/coverage-100%25-success"\n   height="20"\n   alt="Code Coverage">\n</div>\n\n## Install\n\nCloud Eventful is on PyPI and can be installed with:\n\n```shell\npoetry add cloudeventful\n```\n\nor\n\n```shell\npip install cloudeventful\n```\n\n## Usage\n\nThis library provides a `CloudEventful` class which can be used to generate\n[CloudEvents](https://cloudevents.io/) and associate\n[Pydantic](https://pydantic-docs.helpmanual.io/) models as the cloud event `data` field\non a per-topic basis.\n\n### Model Registration\n\nA model is associated with a pattern describing the topics it may be published to using\nthe `data_model` decorator.\n\n```python\nimport re\n\nfrom cloudeventful import CloudEventful\nfrom pydantic import BaseModel\n\nce = CloudEventful(api_version="1.0.0", default_source="my/event/server")\n\n\n@ce.data_model(re.compile(r"/.*/coffee"))\nclass Coffee(BaseModel):\n    flavor: str\n```\n\n### Cloud Event Generation\n\nOnce data models are registered, CloudEvent objects can be generated with an instance of\nthe generated model as the CloudEvent `data` property.\n\n```pycon\n>>> ce.event(Coffee(flavor="mocha"))\nCloudEvent[ModelType](id=\'9b21a718-9dc1-4b56-a4ea-4e9911bc8ca6\', source=\'my/event/server\', specversion=\'1.0\', type=\'Coffee\', data=Coffee(flavor=\'mocha\'), datacontenttype=\'application/json\', dataschema=\'/Coffee\', subject=\'Coffee\', time=datetime.datetime(2022, 11, 19, 15, 33, 6, 39795))\n```\n\n### Publish\n\nA publish function can be registered with a `CloudEventful` instance to enforce topic\nintegrity at run time. This is done by setting the `publish_function` property on a\n`CloudEventful` instance.\n\nA publish function must accept at least a topic arg as a str and a data arg as a\nregistered data model.\n\nThen, the `CloudEventful` publish function can be used to wrap data models in a\nCloudEvent and publish them as JSON strings. Keyword args will be passed to the\nregistered publish function.\n\n## Example using MQTT with Paho\n\n```python\nimport re\n\nfrom cloudeventful import CloudEventful\nimport paho.mqtt.client as mqtt\nfrom pydantic import BaseModel\n\nserver_id = "my/event/server"\n\nclient = mqtt.Client(server_id)\nclient.connect("127.0.0.1")\n\nce = CloudEventful(\n    api_version="1.0.0",\n    default_source=server_id,\n    publish_function=client.publish,\n    default_topic_factory=lambda m: f"/api/v1/{type(m).__name__.lower()}"\n)\n\n\n@ce.data_model(re.compile(r"/.*/coffee"))\nclass Coffee(BaseModel):\n    flavor: str\n\n\n@ce.data_model(re.compile(r"/.*/pen"))\nclass Pen(BaseModel):\n    color: str\n\n\n# Publish a data model wrapped in a cloud event.\nce.publish(Coffee(flavor="mocha"))\n# Raise `ValueError` because topic does not match pattern of this model.\nce.publish(Pen(color="black"))\n```\n\n## Support The Developer\n\n<a href="https://www.buymeacoffee.com/mburkard" target="_blank">\n  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png"\n       width="217"\n       height="60"\n       alt="Buy Me A Coffee">\n</a>\n',
    'author': 'Matthew Burkard',
    'author_email': 'matthewjburkard@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/mburkard/cloud-eventful',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
