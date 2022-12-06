# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linechart']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.3,<2.0.0',
 'empyrical>=0.5.5,<0.6.0',
 'matplotlib>=3.6.2,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'quantrocket-client>=2.8.0.0,<3.0.0.0',
 'scipy>=1.9.3,<2.0.0',
 'seaborn>=0.12.1,<0.13.0']

setup_kwargs = {
    'name': 'linechart',
    'version': '1.10.0',
    'description': 'Backtest performance analysis and charting for MoonLine.',
    'long_description': '# Moonchart\nThis package provides backtest performance analysis and charting for [QuantRocket](https://www.quantrocket.com).\n\n## Example tear sheets\n\n### Moonshot backtest:\n\n![Moonchart tear sheet](https://github.com/quantrocket-llc/moonchart/raw/master/docs/tearsheet-details-example.jpg "Example tear sheet created from a Moonshot backtest")\n\n### 1-dimensional single-strategy parameter scan with Moonshot:\n\n![Moonchart 1-d parameter scan tear sheet](https://github.com/quantrocket-llc/moonchart/raw/master/docs/paramscan-1d-example.jpg "Example tear sheet created from a Moonshot 1-d parameter scan")\n\n### 1-dimensional multi-strategy parameter scan with Moonshot:\n\n![Moonchart 1-d multi-strategy parameter scan tear sheet](https://github.com/quantrocket-llc/moonchart/raw/master/docs/paramscan-1d-multistrat-example.jpg "Example tear sheet created from a Moonshot 1-d multi-strategy parameter scan")\n\n### 2-dimensional parameter scan with Moonshot:\n\n![Moonchart 2-d parameter scan tear sheet](https://github.com/quantrocket-llc/moonchart/raw/master/docs/paramscan-2d-example.jpg "Example tear sheet created from a Moonshot 2-d parameter scan")\n\n## Installation and Usage\n\nFor installation and usage documentation, please visit: https://www.quantrocket.com/docs/\n\n## License\n\nMoonchart is distributed under the Apache 2.0 License. See the LICENSE file in the release for details.\n',
    'author': 'Tim Wedde',
    'author_email': 'tim.wedde@genzai.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
