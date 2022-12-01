# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ukrdc_stats', 'ukrdc_stats.calculators', 'ukrdc_stats.models']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.40,<2.0.0',
 'freezegun>=1.2.2,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'ukrdc-sqla>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'ukrdc-stats',
    'version': '0.4.1',
    'description': 'A package to produce stats from the ukrdc database to be displayed on the dashboard',
    'long_description': '# Dashboard Statistics Library\n\nLibrary for generating statistics for the UKRDC dashboard\n\n## Installation\n\n`pip install ukrdc-stats`\n\n## Basic usage\n\nStatistics calculations require an SQLAlchemy session with a connection to the UKRDC3 database.\nIn this example, we use `ukrdc3_session`, and calculate for the unit code "TEST_UNIT".\n\n```python\nfrom ukrdc_stats import DemographicStatsCalculator\n\ndemographics = DemographicStatsCalculator(ukrdc3, "TEST_UNIT").extract_stats()\n```\n\nEach calculator returns multiple stats from the same cohort, and each of those includes basic metadata required for rendering and plotting the data.\n',
    'author': 'Philip Main',
    'author_email': 'Philip.Main@renalregistry.nhs.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/renalreg/dashboard-stats',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
