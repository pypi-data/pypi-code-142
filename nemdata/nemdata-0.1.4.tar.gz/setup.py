# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nemdata']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pyarrow>=10.0.1,<11.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['nemdata = nemdata.cli:cli']}

setup_kwargs = {
    'name': 'nemdata',
    'version': '0.1.4',
    'description': "Simple CLI for downloading data for Australia's NEM from AEMO.",
    'long_description': '# nem-data\n\nA simple & opinionated Python command line tool to access Australian National Energy Market (NEM) data provided by the Australian Energy Market Operator (AEMO).\n\nIt is designed for use by researchers & data scientists - this tool supports my personal research work.  It is not designed for production use - see [NEMOSIS](https://github.com/UNSW-CEEM/NEMOSIS) for a production grade package.\n\nSee [A hackers guide to AEMO & NEM data](https://adgefficiency.com/hackers-aemo/) for more on context the data provided by AEMO.\n\n\n## Setup\n\nInstall as editable package:\n\n```bash\n$ make setup\n```\n\n\n## Use\n\n```shell-session\n$ nemdata --help\nUsage: nemdata [OPTIONS]\n\n  nemdata is a tool to access NEM data from AEMO.\n\nOptions:\n  -s, --start TEXT    start date (YYYY-MM)\n  -e, --end TEXT      end date (incusive) (YYYY-MM)\n  -r, --report TEXT   nemde, predispatch, unit-scada, trading-price\n  --help              Show this message and exit.\n```\n\n\nTo download NEMDE data:\n\n```bash\n$ nemdata -r nemde --start 2018-01 --end 2018-03\n```\n\nTo download trading price data:\n\n```python\n$ nemdata -r trading-price -s 2018-01 -e 2018-03\n```\n\nSupport the following datasets from MMSDM:\n\n```python\nreports = {\n    \'trading-price\': \'TRADINGPRICE\',\n    \'unit-scada\': \'UNIT_SCADA\',\n    \'predispatch\': "PREDISPATCHPRICE"\n}\n```\n\n\n## Output Data\n\nData is downloaded into into `$HOME/nem-data/data/`:\n\n```shell-session\n$ nemdata -r trading-price -s 2020-01 -e 2020-02\n$ tree ~/nem-data\n/Users/adam/nem-data\n└── data\n    └── trading-price\n        ├── 2020-01\n        │\xa0\xa0 ├── PUBLIC_DVD_TRADINGPRICE_202001010000.CSV\n        │\xa0\xa0 ├── clean.csv\n        │\xa0\xa0 ├── clean.parquet\n        │\xa0\xa0 └── raw.zip\n        └── 2020-02\n            ├── PUBLIC_DVD_TRADINGPRICE_202002010000.CSV\n            ├── clean.csv\n            ├── clean.parquet\n            └── raw.zip\n\n4 directories, 8 files\n```\n\nA few things happen during data processing:\n\n- the top & bottom rows of the raw CSV are removed,\n- `interval-start` and `interval-end` columns are added,\n- for `trading-price`, all data is resampled to a 5 minute frequency (both before and after the 30 to 5 minute settlement interval change).\n',
    'author': 'Adam Green',
    'author_email': 'adam.green@adgefficiency.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
