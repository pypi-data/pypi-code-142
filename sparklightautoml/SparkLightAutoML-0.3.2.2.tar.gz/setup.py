# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparklightautoml',
 'sparklightautoml.automl',
 'sparklightautoml.automl.presets',
 'sparklightautoml.dataset',
 'sparklightautoml.ml_algo',
 'sparklightautoml.pipelines',
 'sparklightautoml.pipelines.features',
 'sparklightautoml.pipelines.ml',
 'sparklightautoml.pipelines.selection',
 'sparklightautoml.reader',
 'sparklightautoml.report',
 'sparklightautoml.tasks',
 'sparklightautoml.tasks.losses',
 'sparklightautoml.transformers',
 'sparklightautoml.transformers.scala_wrappers',
 'sparklightautoml.validation']

package_data = \
{'': ['*'], 'sparklightautoml.report': ['spark_report_templates/*']}

install_requires = \
['hdfs>=2.7.0,<3.0.0',
 'lightautoml==0.3.7.1',
 'onnxmltools>=1.11.0,<2.0.0',
 'poetry-core>=1.0.0,<2.0.0',
 'pyarrow>=1.0.0',
 'pyspark==3.2.3',
 'synapseml==0.9.5',
 'toposort==1.7']

setup_kwargs = {
    'name': 'sparklightautoml',
    'version': '0.3.2.2',
    'description': 'Spark-based distribution version of fast and customizable framework for automatic ML model creation (AutoML)',
    'long_description': '# SLAMA: LightAutoML on Spark\n\nSLAMA is a version of [LightAutoML library](https://github.com/AILab-MLTools/LightAutoML) modified to run in distributed mode with Apache Spark framework.\n\nIt requires:\n1. Python 3.9\n2. PySpark 3.2+ (installed as a dependency)\n3. [Synapse ML library](https://microsoft.github.io/SynapseML/)\n   (It will be downloaded by Spark automatically)\n   \nCurrently, only tabular Preset is supported. See demo with spark-based tabular automl \npreset in [examples/spark/tabular-preset-automl.py](https://github.com/fonhorst/LightAutoML_Spark/blob/distributed/master/examples/spark/tabular-preset-automl.py). \nFor further information check docs in the root of the project containing dedicated SLAMA section. \n\n<a name="apache"></a>\n# License\nThis project is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/fonhorst/LightAutoML_Spark/blob/distributed/master/LICENSE) file for more details.\n\n\n# Installation\nFirst of all you need to install [git](https://git-scm.com/downloads) and [poetry](https://python-poetry.org/docs/#installation).\n\n```bash\n\n# Load LAMA source code\ngit clone https://github.com/fonhorst/LightAutoML_Spark.git\n\ncd LightAutoML/\n\n# !!!Choose only one item!!!\n\n# 1. Global installation: Don\'t create virtual environment\npoetry config virtualenvs.create false --local\n\n# 2. Recommended: Create virtual environment inside your project directory\npoetry config virtualenvs.in-project true\n\n# For more information read poetry docs\n\n# Install LAMA\npoetry lock\npoetry install\n```',
    'author': 'Alexander Ryzhkov',
    'author_email': 'alexmryzhkov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://lightautoml.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
