# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elfragmentador',
 'elfragmentador.config',
 'elfragmentador.data',
 'elfragmentador.model']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'lxml>=4.6.3,<5.0.0',
 'ms2ml>=0.0.29',
 'networkx>=2.8.8,<3.0.0',
 'numba>=0.56.2,<0.57.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.0.0,<2.0.0',
 'pyarrow>=9.0.0,<10.0.0',
 'pyteomics>=4.4.2,<5.0.0',
 'pytorch-lightning>=1.7.4,<2.0.0',
 'torchmetrics>=0.9.3,<0.10.0',
 'uniplot>=0.7.0,<0.8.0',
 'wandb>=0.13.0,<0.14.0']

extras_require = \
{':python_version >= "3.9" and python_version < "3.11"': ['torch>=1.12.0,<1.13.0']}

entry_points = \
{'console_scripts': ['elfragmentador = elfragmentador.cli:main_cli']}

setup_kwargs = {
    'name': 'elfragmentador',
    'version': '0.56.0',
    'description': 'Predicts peptide fragmentations using transformers',
    'long_description': '\n![Pypi version](https://img.shields.io/pypi/v/elfragmentador?style=flat-square)\n![Pypi Downloads](https://img.shields.io/pypi/dm/elfragmentador?style=flat-square)\n![Github Activity](https://img.shields.io/github/last-commit/jspaezp/elfragmentador?style=flat-square)\n![Python versions](https://img.shields.io/pypi/pyversions/elfragmentador?style=flat-square)\n![GitHub Actions](https://img.shields.io/github/workflow/status/jspaezp/elfragmentador/CI%20Testing/release?style=flat-square)\n![License](https://img.shields.io/pypi/l/elfragmentador?style=flat-square)\n\n\n# ElFragmentador\n\n## ElFragmentador\n\nThis repository attempts to implement a neural net that leverages the transformer architecture to predict peptide\nproperties (retention time and fragmentation).\n\n![](./docs/img/schematic.png)\n\n## Usage\n\nCurrently the documentation lives here: [https://jspaezp.github.io/elfragmentador/](https://jspaezp.github.io/elfragmentador/)\nPlease check out [The Quickstart guide](https://jspaezp.github.io/elfragmentador/quickstart) for usage instructions.\n\n![](./docs/img/spectrum.png)\n\n## Why transformers?\n\nBecause we can... Just kidding\n\nThe transformer architecture provides several benefits over the standard approach on fragment prediction (LSTM/RNN). On the training side it allows the parallel computation of whole sequences, whilst in LSTMs one element has to be passed at a time. In addition it gives the model itself a better chance to study the direct interactions between the elements that are being passed.\n\nOn the other hand, it allows a much better interpretability of the model, since the \'self-attention\' can be visualized on the input and in that way see what the model is focusing on while generating the prediction.\n\n## Inspiration for this project\n\nMany of the elements from this project are actually a combination of the principles shown in the [*Prosit* paper](https://www.nature.com/articles/s41592-019-0426-7) and the [Skyline poster](https://skyline.ms/_webdav/home/software/Skyline/%40files/2019-ASBMB-Rohde.pdf) on some of the elements to encode the peptides and the output fragment ions.\n\nOn the transformer side of things I must admit that many of the elements of this project are derived from [DETR:  End to end detection using transformers](https://github.com/facebookresearch/detr) in particular the trainable embeddings as an input for the decoder and some of the concepts discussed about it on [Yannic Kilcher\'s Youtube channel](https://youtu.be/T35ba_VXkMY) (which I highly recommend).\n\n## Why the name?\n\nTwo main reasons ... it translates to \'The fragmenter\' in spanish and the project intends to predict fragmentation. On the other hand ... The name was free in pypi.\n\n## Resources on transformers\n\n- An amazing illustrated guide to understand the transformer architecture: <http://jalammar.github.io/illustrated-transformer/>\n- Another amazing guide in video format exlpaining the architecture "Illustrated Guide to Transformers Neural Network: A step by step explanation": <https://www.youtube.com/watch?v=4Bdc55j80l8>\n- Full implementation of a transformer in pytorch with the explanation of each part: <https://nlp.seas.harvard.edu/2018/04/03/attention.html>\n- Official pytorch implementation of the transformer: <https://pytorch.org/docs/stable/generated/torch.nn.Transformer.html>\n\n## How fast is it?\n\nYou can check how fast the model is in you specific system.\nRight now the CLI tests the speed only on CPU (the model can be run in GPU).\n\nHere I will predict the fasta file for SARS-COV2\n\n```shell\npoetry run elfragmentador predict --fasta tests/data/fasta/uniprot-proteome_UP000464024_reviewed_yes.fasta --nce 32 --charges 2 --missed_cleavages 0 --min_length 20 --out foo.dlib\n```\n\n```\n...\n 99%|█████████▉| 1701/1721 [00:14<00:00, 118.30it/s]\n...\n```\n\n~100 predictions per second including pre-post processing and writting the enciclopeDIA library.\nOn a GPU it is closer to ~1000 preds/sec\n\n## How big is it?\n\nI have explored many variations on the model but currently the one distributed is only ~4mb. Models up to 200mb have been tried and they don\'t really give a big improvement in performance.\n\n## "Common" questions\n\n- What scale are the retention times predicted.\n  - Out of the model it uses a scaled version of the Biognosys retention time\n    scale, so if using the base model, you will need to multiply by 100 and then\n    you will get something compatible with the iRT kit.\n- Is it any good?\n  - Well ... yes but if you want to see if it is good for you own data I have\n    added an API to test the model on a spectral library (made with spectrast).\n    Just get a checkpoint of the model,\n    run the command: `elfragmentador_evaluate {your_checkpoint.ckpt} {your_splib.sptxt}`\n  - TODO add some benchmarking metrics to this readme ...\n- Crosslinked peptides?\n  - No\n- ETD ?\n  - No\n- CID ?\n  - No\n- Glycosilation ?\n  - No\n- Negative Mode ?\n  - No\n- No ?\n  - Not really ... I think all of those are interesting questions but\n    AS IT IS RIGHT NOW it is not within the scope of the project. If you want\n    to discuss it, write an issue in the repo and we can see if it is feasible.\n\n## Acknowledgements\n\n1. Purdue Univ for the computational resources for the preparation of the data (Brown Cluster).\n1. Pytorch Lightning Team ... without this being open sourced this would not be posible.\n1. Weights and Biases (same as above).\n',
    'author': 'J. Sebastian Paez',
    'author_email': 'jspaezp@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
