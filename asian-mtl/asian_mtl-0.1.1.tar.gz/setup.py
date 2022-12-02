# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asian_mtl', 'asian_mtl.evaluation', 'asian_mtl.models']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.21.40,<2.0.0',
 'botocore>=1.24.43,<2.0.0',
 'dacite>=1.6.0,<2.0.0',
 'datasets>=2.1.0,<3.0.0',
 'gdown>=4.4.0,<5.0.0',
 'optimum>=1.1.0,<2.0.0',
 'psutil>=5.9.4,<6.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'pyquery>=1.4.3,<2.0.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'torch>=1.11.0,<2.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'transformers>=4.18.0,<5.0.0']

setup_kwargs = {
    'name': 'asian-mtl',
    'version': '0.1.1',
    'description': 'Seamlessly translate your novels with deep learning models.',
    'long_description': "# `asian_mtl`\n\nThis repository contains the code and documentation for the machine translation models used for EasierMTL's API.\n\nImproved version of the models in the original repository: [EasierMTL/chinese-translation-app](https://github.com/EasierMTL/chinese-translation-app/tree/main/server/chinese_translation_api)\n\n## Supported Translators\n\nAll translators support dynamic quantization! [Our benchmarks](#benchmarks) indicate that they 2x inference speeds, while losing <1% BLEU.\n\n- `ChineseToEnglishTranslator()`\n- `EnglishToChineseTranslator()`\n\n## Getting Started\n\n```bash\npip install asian_mtl\n```\n\nAnd you're good to go!\n\nIf you are contributing, run:\n\n```bash\n# https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option\n\npoetry config virtualenvs.in-project true\n\n# shows the name of the current environment\npoetry env list\n\npoetry install\n```\n\n## Usage\n\nWhen you are using quantized models in this repository, make sure to set `torch.set_num_threads(1)`. This is not set under-the-hood because it could interfere with user setups in an invasive way.\n\nNot doing so will make the quantized models slower than their vanilla counterparts.\n\n## Evaluation\n\nSee [`scripts`](./scripts) for evaluation scripts.\n\nTo run the scripts, simply run:\n\n```bash\n# Running with CLI and config with BERT\npython ./scripts/evaluation/eval.py -c ./scripts/evaluation/configs/helsinki.yaml\n```\n\nChange the config [`helsinki.yaml`](./scripts/evaluation/configs/helsinki.yaml) to use quantized or your specific use case.\n\n### Benchmarks\n\nHere are some basic benchmarks of models in this repository:\n\n| Model                      | Quantized? | N   | BLEU  | Runtime |\n| -------------------------- | ---------- | --- | ----- | ------- |\n| Helsinki-NLP/opus-mt-zh-en | No         | 100 | 0.319 | 27s     |\n|                            | Yes        | 100 | 0.306 | 13.5s   |\n\nThe benchmarks described in the [docs](./docs/evaluation/EVALUATION_REG.md) are a little out-of-date.\n",
    'author': 'Joseph Chen',
    'author_email': 'jchen42703@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EasierMTL/asian_mtl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
