# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guarddog',
 'guarddog.analyzer',
 'guarddog.analyzer.metadata',
 'guarddog.scanners',
 'guarddog.utils']

package_data = \
{'': ['*'],
 'guarddog.analyzer': ['sourcecode/*'],
 'guarddog.analyzer.metadata': ['resources/*']}

install_requires = \
['attrs==21.4.0',
 'boltons==21.0.0',
 'bracex==2.3.post1',
 'charset-normalizer==2.1.0',
 'click-option-group==0.5.3',
 'click==8.1.3',
 'colorama==0.4.5',
 'defusedxml==0.7.1',
 'docker==6.0.0b1',
 'face==20.1.1',
 'flake8>=5.0.4,<6.0.0',
 'glom==22.1.0',
 'idna==3.3',
 'jsonschema==4.9.1',
 'mypy-extensions==0.4.3',
 'pathos>=0.2.9,<0.3.0',
 'pathspec==0.9.0',
 'platformdirs==2.5.2',
 'pyparsing==3.0.9',
 'pytest>=7.1.2,<8.0.0',
 'python-dateutil==2.8.2',
 'python-dotenv==0.20.0',
 'python-lsp-jsonrpc==1.0.0',
 'python-whois>=0.8.0,<0.9.0',
 'requests==2.28.1',
 'semgrep==0.112.1',
 'setuptools>=65.6.3,<66.0.0',
 'six==1.16.0',
 'tarsafe>=0.0.4,<0.0.5',
 'termcolor>=2.1.0,<3.0.0',
 'tomli==2.0.1',
 'tqdm==4.64.0',
 'typing-extensions==4.3.0',
 'ujson==5.4.0',
 'urllib3==1.26.11',
 'wcmatch==8.4',
 'websocket-client==1.3.3']

entry_points = \
{'console_scripts': ['guarddog = guarddog.cli:cli']}

setup_kwargs = {
    'name': 'guarddog',
    'version': '0.1.9',
    'description': 'GuardDog is a CLI tool to Identify malicious PyPI packages',
    'long_description': '# GuardDog\n\nSee https://github.com/datadog/guarddog\n',
    'author': 'Ellen Wang',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DataDog/guarddog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
