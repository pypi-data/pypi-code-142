# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kinguin_client', 'kinguin_client.clients']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kinguin-client',
    'version': '0.1.2',
    'description': 'Python API wrapper for Kinguin',
    'long_description': '# kinguin-client\n\nA tiny API wrapper in Python for Kinguin e-commerce API ([Kinguin-eCommerce-API](https://github.com/kinguinltdhk/Kinguin-eCommerce-API))\n\n## Installation\n\n`pip install kinguin-client`\n\n## Basic Usage\n\n```\nfrom kinguin_client import Kinguin\n\nclient = Kinguin(api_key="API_KEY")\n\nclient.balance().get()\n{\'balance\': 0}\n\nclient.orders().get()\n{\'results\': [], \'item_count\': 0}\n```\n\n## License\n\nMIT\n',
    'author': 'rr00bbiinn',
    'author_email': 'robin@itlandslaget.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rr00bbiinn/kinguin-client',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
