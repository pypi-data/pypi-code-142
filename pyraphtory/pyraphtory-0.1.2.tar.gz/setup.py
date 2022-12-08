# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyraphtory',
 'pyraphtory.algorithms',
 'pyraphtory.scala',
 'pyraphtory.scala.implicits']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=0.4',
 'jpype1>=1.4.1',
 'pandas>=1.4.3',
 'parsy>=2.0,<3',
 'pemja>=0.2.6',
 'py4j>=0.10,<0.11',
 'pyraphtory_jvm>=0.2.0a9',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['jre_install = pyraphtory.jre:check_dl_java_ivy',
                     'raphtory-standalone = pyraphtory.cli:standalone']}

setup_kwargs = {
    'name': 'pyraphtory',
    'version': '0.1.2',
    'description': 'Raphtory - Temporal Graph Analytics Platform. This is the Python version of the library.',
    'long_description': '# Getting started with `pyraphtory`\n\nBuild and install instructions can be found on the [docs](https://docs.raphtory.com/)\n\n## Links\n\n- PyPi https://pypi.org/project/pyraphtory/\n- Github https://github.com/Raphtory/Raphtory/\n- Website https://raphtory.github.io/\n- Slack https://raphtory.slack.com\n- Documentation https://raphtory.readthedocs.io/\n- Bug reports/Feature request https://github.com/raphtory/raphtory/issues',
    'author': 'Fabian Murariu',
    'author_email': 'admin@pometry.com',
    'maintainer': 'Pometry',
    'maintainer_email': 'admin@pometry.com',
    'url': 'https://raphtory.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.13,<3.11',
}


setup(**setup_kwargs)
