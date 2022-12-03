# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['toyml',
 'toyml.classification',
 'toyml.clustering',
 'toyml.ensemble',
 'toyml.utils']

package_data = \
{'': ['*']}

extras_require = \
{'full': ['tqdm>=4.0.0,<5.0.0']}

setup_kwargs = {
    'name': 'toyml',
    'version': '0.2.0',
    'description': 'ToyML: Machine Learning from Scratch',
    'long_description': '<p align="center" style="font-size:40px; margin:0px 10px 0px 10px">\n    <em>ToyML</em>\n</p>\n<p align="center">\n    <em>Machine Learning from Scratch</em>\n</p>\n\n<p align="center">\n<a href="https://codecov.io/gh/shenxiangzhuang/ToyML" target="_blank">\n    <img src="https://codecov.io/gh/shenxiangzhuang/ToyML/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/toyml" target="_blank">\n    <img src="https://badge.fury.io/py/toyml.svg" alt="PyPI Package">\n</a>\n</p>\n\nThere are some machine learning algorithms implemented from scratch.\nLet\'s learn machine learning with simple toy code.\n\n\n# Installation\n```bash\npip install toyml\n```\n\n\n# Links\n- Documentation: [https://datahonor.com/toyml/](https://datahonor.com/toyml)\n- PyPi: [https://pypi.org/project/toyml/](https://pypi.org/project/toyml/)\n- Changelog: [https://datahonor.com/toyml/CHANGELOG/](https://datahonor.com/toyml/CHANGELOG)\n\n\n# RoadMap\n\n- [x] Clustering: DBSCAN, Hierarchical(Agnes&Diana), Kmeans\n- [x] Classification: KNN\n- [x] Ensemble: Boosting(AdaBoost)\n- [ ] Classification: NaiveBayes, DecisionTree, SVM\n- [ ] Association Analysis: Apriori\n- [ ] Ensemble: GBDT\n',
    'author': 'Xiangzhuang Shen',
    'author_email': 'datahonor@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://shenxiangzhuang.github.io/ToyML',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
