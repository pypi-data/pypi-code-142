# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['micropack']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'micropack',
    'version': '0.1.0',
    'description': 'Lightweight JSON serialisation and diff-patching tool for bandwitdth constained applications',
    'long_description': '<img width=80% \nsrc="https://user-images.githubusercontent.com/29259177/203023707-0a5a84eb-de45-482b-a8e5-d6b22c4f09df.png"\nstyle="margin-left: auto; margin-right: auto;display: block;">\n\n###\n Lightweight JSON serialisation and diff-patching tool for bandwitdth constained applications\n\n![image](https://user-images.githubusercontent.com/29259177/203046086-1c4e36f3-8a81-42b9-bed0-232f970ed90a.png)\n',
    'author': 'Bernard Greyling',
    'author_email': 'bpgreyling@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
