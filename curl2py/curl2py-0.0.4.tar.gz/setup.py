# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['curl2py']

package_data = \
{'': ['*']}

install_requires = \
['Werkzeug>=2.2.2,<3.0.0', 'requests>=2.28.1,<3.0.0', 'six>=1.16.0,<2.0.0']

entry_points = \
{'console_scripts': ['curl2py = curl2py:main']}

setup_kwargs = {
    'name': 'curl2py',
    'version': '0.0.4',
    'description': 'A certbot plugin for DNSPod',
    'long_description': 'curl2py: conver cURL command to python-requests code\n====================================================\n\n\n.. code:: bash\n\n    curl2py curl www.sina.com\n',
    'author': 'codeif',
    'author_email': 'me@codeif.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/codeif/curl2py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
