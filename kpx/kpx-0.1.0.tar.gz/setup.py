# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['kpx']
install_requires = \
['boto3>=1.26,<2.0',
 'configparser>=5.3.0,<6.0.0',
 'prettytable>=3.5.0,<4.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['kpx = kpx:app']}

setup_kwargs = {
    'name': 'kpx',
    'version': '0.1.0',
    'description': 'AWS config and credentials manager',
    'long_description': '# Install\n\n```bash\npip install -U kpx --index-url https://gitlab.com/api/v4/projects/24038501/packages/pypi/simple\n```\n',
    'author': 'Bogdan Rizac',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
