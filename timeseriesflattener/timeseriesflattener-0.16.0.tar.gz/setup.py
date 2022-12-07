# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['timeseriesflattener',
 'timeseriesflattener.feature_cache',
 'timeseriesflattener.testing']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.41,<1.5.42',
 'catalogue>=2.0.0,<2.1.0',
 'coloredlogs>14.0.0,<15.1.0',
 'dask>=2022.9.0,<2022.12.0',
 'deepchecks>=0.8.0,<0.10.0',
 'dill>=0.3.0,<0.3.6',
 'frozendict>=2.3.4,<2.4.0',
 'jupyter>=1.0.0,<1.1.0',
 'numpy>=1.23.3,<1.23.6',
 'pandas>=1.4.0,<1.6.0',
 'protobuf<=3.20.3',
 'psutil>=5.9.1,<6.0.0',
 'psycopmlutils>=0.2.4,<0.3.0',
 'pyarrow>=9.0.0,<9.1.0',
 'pydantic>=1.9.0,<1.10.0',
 'pyodbc>=4.0.34,<4.0.36',
 'scikit-learn>=1.1.2,<1.1.3',
 'scipy>=1.8.0,<1.9.4',
 'skimpy>=0.0.7,<0.1.0',
 'srsly>=2.4.4,<2.4.6',
 'wandb>=0.12.0,<0.13.5',
 'wasabi>=0.9.1,<0.10.2']

setup_kwargs = {
    'name': 'timeseriesflattener',
    'version': '0.16.0',
    'description': 'A package for converting time series data from e.g. electronic health records into wide format data.',
    'long_description': '<a href="https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener"><img src="https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/blob/main/docs/_static/icon.png?raw=true" width="220" align="right"/></a>\n\n# Time-series Flattener\n\n![python versions](https://img.shields.io/badge/Python-%3E=3.10-blue)\n[![Code style: black](https://img.shields.io/badge/Code%20Style-Black-black)](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)\n[![github actions pytest](https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/actions/workflows/main_test_and_release.yml/badge.svg)](https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/actions)\n[![PyPI version](https://badge.fury.io/py/timeseriesflattener.svg)](https://pypi.org/project/timeseriesflattener/)\n\n## Roadmap\nRoadmap is tracked on our [kanban board](https://github.com/orgs/Aarhus-Psychiatry-Research/projects/11/views/1).\n\n## 🔧 Installation\nTo get started using timeseriesflattener simply install it using pip by running the following line in your terminal:\n\n```\npip install timeseriesflattener\n```\n\n## 📖 Documentation\n\n| Documentation          |                                                                                              |\n| ---------------------- | -------------------------------------------------------------------------------------------- |\n| 🎛 **[API References]** | The detailed reference for timeseriesflattener\'s API. Including function documentation |\n| 🙋 **[FAQ]**            | Frequently asked question                                                                    |\n\n[api references]: https://Aarhus-Psychiatry-Research.github.io/timeseriesflattener/\n[FAQ]: https://Aarhus-Psychiatry-Research.github.io/timeseriesflattener/faq.html\n\n## 💬 Where to ask questions\n\n| Type                           |                        |\n| ------------------------------ | ---------------------- |\n| 🚨 **Bug Reports**              | [GitHub Issue Tracker] |\n| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker] |\n| 👩\u200d💻 **Usage Questions**          | [GitHub Discussions]   |\n| 🗯 **General Discussion**       | [GitHub Discussions]   |\n\n[github issue tracker]: https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/issues\n[github discussions]: https://github.com/Aarhus-Psychiatry-Research/timeseriesflattener/discussions\n\n\n## 🎓 Projects\nPSYCOP projects which use `timeseriesflattener`. Note that some of these projects have yet to be published and are thus private.\n\n| Project                 | Publications |                                                                                                                                                                                                                                       |\n| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| **[Type 2 Diabetes]**   |              | Prediction of type 2 diabetes among patients with visits to psychiatric hospital departments                                                                                                                                          |\n| **[Cancer]**            |              | Prediction of Cancer among patients with visits to psychiatric hospital departments                                                                                                                                                   |\n| **[COPD]**              |              | Prediction of Chronic obstructive pulmonary disease (COPD) among patients with visits to psychiatric hospital departments                                                                                                             |\n| **[Forced admissions]** |              | Prediction of forced admissions of patients to the psychiatric hospital departments. Encompasses two seperate projects: 1. Prediciting at time of discharge for inpatient admissions. 2. Predicting day before outpatient admissions. |\n| **[Coersion]**          |              | Prediction of coercion among patients admittied to the hospital psychiatric department. Encompasses predicting mechanical restraint, sedative medication and manual restraint 48 hours before coercion occurs.                        |\n\n\n[Type 2 diabetes]: https://github.com/Aarhus-Psychiatry-Research/psycop-t2d\n[Cancer]: https://github.com/Aarhus-Psychiatry-Research/psycop-cancer\n[COPD]: https://github.com/Aarhus-Psychiatry-Research/psycop-copd\n[Forced admissions]: https://github.com/Aarhus-Psychiatry-Research/psycop-forced-admissions\n[Coersion]: https://github.com/Aarhus-Psychiatry-Research/pyscop-coercion\n',
    'author': 'Martin Bernstorff',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
