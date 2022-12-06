# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pheval', 'pheval.implementations', 'pheval.runners']

package_data = \
{'': ['*']}

install_requires = \
['class-resolver>=0.3.10,<0.4.0',
 'click>=8.1.3',
 'deprecation>=2.1.0',
 'jaydebeapi>=1.2.3',
 'pandas>=1.5.1',
 'tqdm>=4.64.1']

entry_points = \
{'console_scripts': ['pheval = pheval.cli:pheval',
                     'pheval-utils = pheval.cli:pheval_utils']}

setup_kwargs = {
    'name': 'pheval',
    'version': '0.1.0',
    'description': '',
    'long_description': '# PhEval - Phenotypic Inference Evaluation Framework\n\nThere is currently no empirical framework to evaluate the performance of phenotype matching and prioritization tools, much needed to guide tuning for cross species inference. Many algorithms are evaluated using simulations, which may fail to capture real-world scenarios. This gap presents a number of problems: it is difficult to optimize algorithms if we do not know which choices lead to better results; performance may be sensitive to factors that are subject to change, such as ontology structure or annotation completeness. We will develop a modular Phenotypic Inference Evaluation Framework, PhEval and use it to optimize our own algorithms, as well as deliver it as a community resource.\n\n',
    'author': 'Nico Matentzoglu',
    'author_email': 'nicolas.matentzoglu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
