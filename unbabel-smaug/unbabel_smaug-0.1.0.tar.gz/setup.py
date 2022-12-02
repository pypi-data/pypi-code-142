# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smaug',
 'smaug.cli',
 'smaug.mask',
 'smaug.model',
 'smaug.random',
 'smaug.transform',
 'smaug.validation']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'nltk>=3.7,<4.0',
 'numpy>=1.21.4,<2.0.0',
 'packaging>=21.3,<22.0',
 'pandas>=1.3.4,<2.0.0',
 'sentencepiece==0.1.96',
 'stanza>=1.3.0,<2.0.0',
 'torch>=1.8.2,<2.0.0',
 'transformers>=4.15.0,<5.0.0']

entry_points = \
{'console_scripts': ['augment = smaug.cli:augment']}

setup_kwargs = {
    'name': 'unbabel-smaug',
    'version': '0.1.0',
    'description': 'Sentence-level Multilingual Augmentation',
    'long_description': '# SMAUG: Sentence-level Multilingual AUGmentation\n\n`smaug` is a package for multilingual data augmentation. It offers transformations focused on changing specific aspects of sentences, such as Named Entities, Numbers, etc.\n\n# Usage\n\nThe `smaug` package can be used as a command line interface (CLI) or by directly importing and calling the package Python API. To use `smaug`, first install it by following these [instructions](#install).\n\n## Command Line Interface\n\nThe CLI offers a way to read, transform, validate and write perturbed sentences to files. For more information, see the [full details](CLI.md).\n\n### Single transform\n\nTo apply a single transform to a set of sentences, execute the following command:\n\n```\n$ augment io-read-lines -p <input_file> -l <input_lang_code> <transf_name> io-write-json -p <output_file>\n```\n\n> `<transf_name>` is the name of the transform to apply (see this [section](OPERATIONS.md#transforms) for a list of available transforms).\n>\n> `<input_file>` is a text file with one sentence per line.\n>\n> `<input_lang_code>` is a two character language code for the input sentences.\n>\n> `<output_file>` is a json file to be created with the transformed sentences.\n\n### Multiple Transforms\n\nTo apply multiple transforms, just specify them in arbitrary order between the read and write operations:\n\n```\n$ augment io-read-lines -p <input_file> -l <input_lang_code> <transf_name_1> <transf_name_2> ... io-write-json -p <output_file>\n```\n\n### Multiple Input Files\n\nTo read from multiple input files, also specify them in arbitrary order:\n\n```\n$ augment io-read-lines -p <input_file_1> -l <input_lang_code_1> read-lines -p <input_file_2> -l <input_lang_code_2> ... <transf_name_1> <transf_name_2> ... io-write-json -p <output_file>\n```\n\n### Configuration File\n\nTo facilitate the previous operations, it is possible to specify the entire pipeline from a [configuration file](CLI.md#configuration-file-specification):\n\n```\n$ augment --cfg <path_to_config_file>\n```\n\nTODO\n\n# Install\n\nTo install this package, execute the following steps:\n\n* Install the [poetry](https://python-poetry.org/docs/#installation) tool for dependency management.\n\n* Clone this git repository and install the project.\n\n```\n$ git clone https://github.com/DuarteMRAlves/smaug.git\n$ cd smaug\n$ poetry install\n```',
    'author': 'Duarte Alves',
    'author_email': 'duartemalves@tecnico.ulisboa.pt',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Unbabel/smaug',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
