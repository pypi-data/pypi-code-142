# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['protenc', 'protenc.console']

package_data = \
{'': ['*']}

install_requires = \
['biopython>=1.80,<2.0',
 'humanfriendly>=10.0,<11.0',
 'json-stream>=2.1.1,<3.0.0',
 'lmdb>=1.3.0,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'sentencepiece>=0.1.97,<0.2.0',
 'tqdm>=4.64.1,<5.0.0',
 'transformers>=4.24.0,<5.0.0']

entry_points = \
{'console_scripts': ['protenc = protenc.console.extract:entrypoint']}

setup_kwargs = {
    'name': 'protenc',
    'version': '0.1.1',
    'description': 'Extract protein embeddings from pretrained models.',
    'long_description': "ProtEnc: generate protein embeddings the easy way\n=======\n\n[ProtEnc](https://github.com/kklemon/ProtEnc) aims to simplify extraction of protein embeddings from various pre-trained models by providing simple APIs and bulk generation scripts for the ever-growing jungle of protein language models (pLMs). Currently, supported models are:\n\n* [ProtTrans](https://github.com/agemagician/ProtTrans) family\n* [ESM](https://github.com/facebookresearch/esm)\n* AlphaFold (coming soon™)\n\n**Note:** the project is work in progress.\n\nMotivation\n----------\n\n\n\nUsage\n-----\n\n### Installation\n\n```bash\npip install protenc\n```\n\n**Note:** while ProtEnc depends on [pytorch](https://pytorch.org/), it is not part of the formal dependencies. \nThis is due to the large number of different pytorch distributions which may mismatch with the target environment.\n\n### Python API\n\n```python\nimport protenc\nimport torch\n\n# List available models\nprint(protenc.list_models())\n\n# Instantiate a model\nmodel = protenc.get_model('esm2_t33_650M_UR50D')\n\nproteins = [\n  'MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG',\n  'KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE'\n]\n\nbatch = model.prepare_sequences(proteins)\n\n# Use GPU if available\nif torch.cuda.is_available():\n  model = model.to('cuda')\n  batch = protenc.utils.to_device(batch, 'cuda')\n\nfor embed in model(batch):\n  # Embeddings have shape [L, D] where L is the sequence length and D the \n  # embedding dimensionality.\n  print(embed.shape)\n  \n  # Derive a single per-protein embedding vector by averaging along the \n  # sequence dimension\n  embed.mean(0)\n```\n\n### Command-line interface\n\nAfter installation, use the `protenc` shell command for bulk generation and export of protein embeddings.\n\n```bash\nprotenc <path-to-protein-sequences> <path-to-output> --model_name=<name-of-model>\n```\n\nBy default, input and output formats are inferred from the file extensions.\n\nRun\n\n```bash\nprotenc --help\n```\n\nfor a detailed usage description.\n\n**Example**\n\nGenerate protein embeddings using the ESM2 650M model for sequences provided in a [FASTA](https://en.wikipedia.org/wiki/FASTA_format) file and write embeddings to an [LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database):\n\n```bash\nprotenc proteins.fasta embeddings.lmdb --model_name=esm2_t33_650M_UR50D\n```\n\nThe generated embeddings will be stored in a lmdb key-value store and can be easily accessed using the `read_from_lmdb` utility function:\n\n```python\nfrom protenc.utils import read_from_lmdb\n\nfor label, embed in read_from_lmdb('embeddings.lmdb'):\n    print(label, embed)\n```\n\n**Features**\n\nInput formats:\n* CSV\n* JSON\n* [FASTA](https://en.wikipedia.org/wiki/FASTA_format)\n\nOutput format:\n* [LMDB](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database)\n* [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) (coming soon)\n\nGeneral:\n* Multi-GPU inference with (`--data_parallel`)\n* FP16 inference (`--amp`)\n\nDevelopment\n-----------\n\nClone the repository:\n\n```bash\ngit clone git+https://github.com/kklemon/protenc.git\n```\n\nInstall dependencies via [Poetry](https://python-poetry.org/):\n\n```bash\npoetry install\n```\n\nContribution\n------------\n\nHave feature ideas or found a bug? Love to see support for a new model? Feel free to [create an issue](https://github.com/kklemon/ProtEnc/issues/new).\n\nTodo\n----\n\n- [ ] Support for more input formats\n  - [X] CSV\n  - [ ] Parquet\n  - [X] FASTA\n  - [X] JSON\n- [ ] Support for more output formats\n  - [X] LMDB\n  - [ ] HDF5\n  - [ ] DataFrame\n  - [ ] Pickle\n- [ ] Large models support\n  - [ ] Model offloading\n  - [ ] Sharding\n- [ ] Support for more protein language models\n  - [X] Whole ProtTrans family\n  - [X] Whole ESM family\n  - [ ] AlphaFold (?)\n- [X] Implement all remaining TODOs in code\n- [ ] Distributed inference\n- [ ] Maybe support some sort of optimized inference such as quantization\n  - This may be up to the model providers\n- [ ] Improve documentation\n- [ ] Support translation of gene sequences\n- [ ] Add tests. We need tests!!!",
    'author': 'Kristian Klemon',
    'author_email': 'kristian.klemon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
