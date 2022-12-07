# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simpletimer']

package_data = \
{'': ['*']}

install_requires = \
['confluent-kafka>=1.9.2,<2.0.0', 'kafka-python>=2.0.2,<3.0.0']

setup_kwargs = {
    'name': 'simpletimer-kafka',
    'version': '0.1.9',
    'description': '',
    'long_description': '# SimpleTimer\n\nA repo containing an object that be wrapped to record time taken for operations within\n\n## To Use\n\n- Install requirements using `pip install -r requirements.txt`\n- Import from the timer.py file the Stopwatch object and initialise it, setting it to _False_ if you do not wish to see a log of the time taken\n- Simply use a \'with\' statement with the object and add all operation inside of the statement\n\n## Stopwatch Example\n\n### Code\n\n```\nfrom timer import Stopwatch\nimport time\n\ntimer = Stopwatch(True)\n\nwith timer:\n    for x in range(10):\n        time.sleep(1)\n        print(x)\n```\n\n### Output\n\n```\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n[02/12/2022 04:03:30 PM] [INFO] Time taken to complete operations: 10.0755204s\n```\n\n## StopwatchKafka Example\n\n### Code\n\n```\nfrom timer.timer import StopwatchKafka\n\nimport time\n\ntimer = StopwatchKafka(kafka_topic="numtest")\n\n\nfor x in range(5):\n    with timer:\n        time.sleep(2)\n```\n\n### Output (from Kafka Consumer Side)\n\n```\n{\'time_taken\': 2.0093802999999997}\n{\'time_taken\': 2.0095709000000004}\n{\'time_taken\': 2.0142518000000003}\n{\'time_taken\': 2.0143922000000005}\n{\'time_taken\': 2.0023295999999995}\n```\n',
    'author': 'Mathias Ho',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
