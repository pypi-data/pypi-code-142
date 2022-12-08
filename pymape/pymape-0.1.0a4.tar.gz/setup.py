# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mape',
 'mape.remote',
 'mape.remote.influxdb',
 'mape.remote.redis',
 'mape.remote.rest']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'Rx>=3.2.0,<4.0.0',
 'aiohttp>=3.8.1,<4.0.0',
 'fastapi>=0.73,<0.74',
 'influxdb-client>=1.26.0,<2.0.0',
 'redis-purse>=0.25.0,<0.26.0',
 'uvicorn>=0.17.4,<0.18.0']

setup_kwargs = {
    'name': 'pymape',
    'version': '0.1.0a4',
    'description': 'Framework to develop Self-Adaptive system based on MAPE-K loop.',
    'long_description': '<p align="center">\n    <a href="https://pypi.org/project/pymape/"><img\n        src="https://img.shields.io/pypi/v/pymape?style=flat-square"\n        alt="PyPI Version"\n    /></a>\n    <a href="https://pypi.org/project/pymape/"><img\n        src="https://img.shields.io/pypi/pyversions/pymape?style=flat-square"\n        alt="Py Version"\n    /></a>\n    <a href="https://github.com/elbowz/pymape/issues"><img\n        src="https://img.shields.io/github/issues/elbowz/pymape.svg?style=flat-square"\n        alt="Issues"\n    /></a>\n    <a href="https://raw.githubusercontent.com/elbowz/PyMAPE/main/LICENSE"><img\n        src="https://img.shields.io/github/license/elbowz/pymape.svg?style=flat-square"\n        alt="GPL License"\n    /></a>\n    <a href="https://raw.githubusercontent.com/elbowz/PyMAPE/main/LICENSE"><img\n        src="https://img.shields.io/static/v1?label=Powered&message=RxPY&style=flat-square&color=informational"\n        alt="RxPY"\n    /></a>\n</p>\n\n<p align="center">\n    <img src="https://github.com/elbowz/PyMAPE/raw/main/docs/img/logo.png" alt="PyMAPE" width="400">\n    <h4 align="center">Distributed and decentralized MonitorAnalyzePlanExecute-Knowledge loops framework</h3>\n    <p align="center">\n        Framework to support the development and deployment of Autonomous (Self-Adaptive) Systems\n    </p>\n</p>\n<br />\n\n## Getting Started\n\n### Install\n\n```bash\npip install pymape\n```\n\nSee [Examples](https://github.com/elbowz/PyMAPE#examples) for play with some MAPE-K patterns.\n\n### Install for Developers and Contributors\n\n```bash\ngit clone https://github.com/elbowz/PyMAPE.git\ncd PyMAPE\npoetry install\n```\n*note:* you need to have already installed [poetry](https://python-poetry.org/)\n\nThen use `poetry shell` and/or `poetry run` (eg. `poetry run examples/coordinated-ambulance.py --speed 80`) to exec your script inside the development environment.\n\n### First loop (Ambulance)\n\n![ambulance diagram](https://github.com/elbowz/PyMAPE/raw/main/docs/img/mape-ambulance.png)\n\n```python\nimport mape\nfrom mape.loop import Loop\n\n""" MAPE Loop and elements definition """\nloop = Loop(uid=\'ambulance_emergency\')\n\n@loop.monitor\ndef detect(item, on_next, self):\n    if \'speed_limit\' in item:\n        # Local volatile knowledge\n        self.loop.k.speed_limit = item[\'speed_limit\']\n    elif \'emergency_detect\' in item:\n        on_next(item[\'emergency_detect\'])\n\n@loop.plan(ops_in=ops.distinct_until_changed())\nasync def policy(emergency, on_next, self):\n    if emergency is True:\n        self.last_speed_limit = self.loop.k.speed_limit\n        new_speed = max(self.last_speed_limit, self.emergency_speed)\n\n        on_next({\'speed\': new_speed})\n        on_next({\'siren\': True})\n    else:\n        on_next({\'speed\': self.last_speed_limit})\n        on_next({\'siren\': False})\n\npolicy.emergency_speed = 160\n\n@loop.execute\ndef exec(item: dict, on_next):\n    if \'speed\' in item:\n        ambulance.speed_limit = item[\'speed\']\n    if \'siren\' in item:\n        ambulance.siren = item[\'siren\']\n\nfor element in loop:\n    element.debug(Element.Debug.IN)\n\n""" MAPE Elements connection """\ndetect.subscribe(policy)\npolicy.subscribe(exec)\n\n# Starting monitor...\ndetect.start()\n```\n### Traversing\n\n```python\n# Iterate over loops and element\nfor loop in mape.app:\n    logger.debug(f"* {loop.uid}")\n    for element in loop:\n        logger.debug(f" - {element.uid}")\n\n# Get all Execute elements\n[element for element in loop_obj if isinstance(element, Execute)]\n\n# Different access way to loop/element through dot-notation (path)\nmape.app.loop_uid.element_uid\nmape.app[\'loop_uid.element_uid\']\n```\n\n## Docs\n\n### Slides\n\n[Introduction to PyMAPE](https://github.com/elbowz/PyMAPE/raw/main/docs/slides.pdf) with examples\n\n### Examples\n\nImplementation of the 5 decentralized (and distributed) MAPE patterns described in the paper:  \n["On Patterns for Decentralized Control in Self-Adaptive Systems", Danny Weyns](https://www.ics.uci.edu/~seal/publications/2012aSefSAS.pdf)\n\n* **Ambulance-Car Emergency** (Information Sharing and Coordinated Control)\n* **Average Speed Enforcement** (Master/Slave)\n* **Dynamic Carriageway** (Regional Planning)\n* **Cruise Control with Distance Hold** (Hierarchical Control)\n\nIf you want try some examples (path `examples/`), refer to section `# CLI EXAMPLES` inside the source code of each one.  \n\nThe examples need furthers requirements, please see [pyproject.toml](https://github.com/elbowz/PyMAPE/raw/main/pyproject.toml) or use poetry to [install them](https://github.com/elbowz/PyMAPE#install-for-developers-and-contributors).  \n\nYou also need a Redis and InfluxDB instance running, for example:\n\n```bash\ndocker run --name mape-redis -p 6379:6379  \\\n-v $(pwd)/docker/redis:/usr/local/etc/redis  \\\n--rm redis redis-server /usr/local/etc/redis/redis.conf\n```\n\n```bash\ndocker run --name mape-influxdb -p 8086:8086 \\\n-v $(pwd)/docker/influxdb/data:/var/lib/influxdb2 \\\n-v $(pwd)/docker/influxdb/conf:/etc/influxdb2 \\\n-e DOCKER_INFLUXDB_INIT_MODE=setup \\\n-e DOCKER_INFLUXDB_INIT_USERNAME=user \\\n-e DOCKER_INFLUXDB_INIT_PASSWORD=qwerty123456 \\\n-e DOCKER_INFLUXDB_INIT_ORG=univaq \\\n-e DOCKER_INFLUXDB_INIT_BUCKET=mape \\\n-e DOCKER_INFLUXDB_INIT_RETENTION=1w \\\n-e DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=<GENERATE_OR_TAKE_FROM_CONFIG_YAML> \\\n--rm influxdb:2.0\n```\n\nSee source for more information.',
    'author': 'Emanuele Palombo',
    'author_email': 'muttley.bd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://elbowz.github.io/PyMAPE/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
