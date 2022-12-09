# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbibbi']

package_data = \
{'': ['*']}

modules = \
['__init__', 'py']
setup_kwargs = {
    'name': 'bbibbi',
    'version': '0.1.4',
    'description': 'My own very simple python service locator',
    'long_description': 'bbibbi\n======\n\nIt\'s a simple service locator that I made for use.\n\n\n.. end-of-readme-intro\n\nInstallation\n------------\n\n::\n\n    pip install bbibbi\n\n\nUsage\n--------\n::\n\n    from bbibbi import container, Symbol\n\n    SERVICE_SYMBOL = Symbol("SomeService")\n\n    class Service:\n        def ten(self) -> int:\n            return 10\n\n    container.register(SERVICE_SYMBOL, Service())\n\n    service: Service = container.get(SERVICE_SYMBOL)\n    assert service.ten() == 10\n\n',
    'author': 'sagnol',
    'author_email': 'samcom@naver.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sagnol/bbibbi',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
