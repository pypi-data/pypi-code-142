# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sampo',
 'sampo.generator',
 'sampo.generator.config',
 'sampo.generator.enviroment',
 'sampo.generator.pipeline',
 'sampo.metrics',
 'sampo.metrics.resources_in_time',
 'sampo.scheduler',
 'sampo.scheduler.genetic',
 'sampo.scheduler.heft',
 'sampo.scheduler.heft_between',
 'sampo.scheduler.resource',
 'sampo.scheduler.topological',
 'sampo.scheduler.utils',
 'sampo.schemas',
 'sampo.structurator',
 'sampo.utilities',
 'sampo.utilities.generation',
 'sampo.utilities.sampler',
 'sampo.utilities.visualization']

package_data = \
{'': ['*']}

install_requires = \
['blis>=0.7.7,<0.8.0',
 'catalogue>=2.0.7,<2.1.0',
 'catboost>=1.0.5,<1.1.0',
 'certifi>=2021.10.8,<2021.11.0',
 'charset-normalizer>=2.0.12,<2.1.0',
 'click>=8.1.3,<8.2.0',
 'cycler>=0.11.0,<0.12.0',
 'cymem>=2.0.6,<2.1.0',
 'dash>=2.4.1,<2.5.0',
 'dataclasses>=0.6,<1.0',
 'deap>=1.3.1,<1.4.0',
 'flask>=2.1.2,<2.2.0',
 'fonttools>=4.33.3,<4.34.0',
 'graphviz>=0.20,<1.0',
 'idna>=3.3,<4.0',
 'importlib-metadata>=4.11.3,<4.12.0',
 'ipython>=8.6.0,<9.0.0',
 'itsdangerous>=2.1.2,<2.2.0',
 'jinja2>=3.1.2,<3.2.0',
 'joblib>=1.1.0,<1.2.0',
 'kiwisolver>=1.4.2,<1.5.0',
 'langcodes>=3.3.0,<3.4.0',
 'markupsafe>=2.1.1,<2.2.0',
 'matplotlib>=3.5.1,<3.6.0',
 'murmurhash>=1.0.7,<1.1.0',
 'numpy-indexed>=0.3.5,<0.4.0',
 'numpy>=1.22.3,<1.23.0',
 'packaging>=21.3,<22.0',
 'pandas>=1.4.1,<1.5.0',
 'pathy>=0.6.1,<0.7.0',
 'pillow>=9.1.0,<9.2.0',
 'plotly>=5.8.0,<5.9.0',
 'preshed>=3.0.6,<3.1.0',
 'pydantic>=1.8.2,<1.9.0',
 'pyparsing>=3.0.8,<3.1.0',
 'pytest>=7.1.2,<7.2.0',
 'python-dateutil>=2.8.2,<2.9.0',
 'pytz>=2022.1,<2023.0',
 'reportlab>=3.5.67,<3.6.0',
 'requests>=2.27.1,<2.28.0',
 'scikit-learn>=1.0.2,<1.1.0',
 'scipy>=1.8.1,<1.9.0',
 'seaborn>=0.11.2,<0.12.0',
 'setuptools>=58.0.4,<58.1.0',
 'six>=1.16.0,<1.17.0',
 'smart-open>=5.2.1,<5.3.0',
 'sortedcontainers>=2.4.0,<2.5.0',
 'spacy-legacy>=3.0.9,<3.1.0',
 'spacy-loggers>=1.0.2,<1.1.0',
 'srsly>=2.4.3,<2.5.0',
 'tenacity>=8.0.1,<8.1.0',
 'thinc>=8.0.15,<8.1.0',
 'threadpoolctl>=3.1.0,<3.2.0',
 'toposort>=1.7,<2.0',
 'tqdm>=4.64.0,<4.65.0',
 'typer>=0.4.1,<0.5.0',
 'typing-extensions>=4.2.0,<4.3.0',
 'urllib3>=1.26.9,<1.27.0',
 'wasabi>=0.9.1,<0.10.0',
 'werkzeug>=2.1.2,<2.2.0',
 'zipp>=3.8.0,<3.9.0']

setup_kwargs = {
    'name': 'sampo',
    'version': '0.1.0.44',
    'description': '',
    'long_description': '# SAMPO — Scheduler for Adaptive Manufacturing Processes Optimization\n\n## Описание планировщика\n\nПланировщик для адаптивной оптимизации производственных процессов включает в себя набор алгоритмов интеллектуального анализа и построения расписаний задач производственных процессов с учетом ресурсных и прочих ограничений, накладываемых предметной областью.\n\nОн позволяет эффективно планировать производственные задачи и назначать ресурсы, оптимизируя результат планирования по требуемым метрикам.\n',
    'author': 'iAirLab',
    'author_email': 'iairlab@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
