# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trill', 'trill.utils']

package_data = \
{'': ['*'], 'trill': ['data/*']}

install_requires = \
['GitPython>=3.1.29,<4.0.0',
 'biotite>=0.35.0,<0.36.0',
 'datasets>=2.7.1,<3.0.0',
 'fair-esm>=2.0.0,<3.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'pytest>=7.2.0,<8.0.0',
 'transformers>=4.25.1,<5.0.0']

setup_kwargs = {
    'name': 'trill-proteins',
    'version': '0.1.0',
    'description': 'Sandbox (in progress) for Computational Protein Design',
    'long_description': '# TRILL\n**TR**aining and **I**nference using the **L**anguage of **L**ife\n\n## Arguments\n\n### Positional Arguments:\n1. name (Name of run)\n2. query (Input file. Needs to be either protein fasta (.fa, .faa, .fasta) or structural coordinates (.pdb, .cif))\n3. GPUs (Total # of GPUs requested for each node)\n\n### Optional Arguments:\n- -h, --help (Show help message)\n- --database (Input database to embed with --blast mode)\n- --nodes (Total number of computational nodes. Default is 1)\n- --lr (Learning rate for adam optimizer. Default is 0.0001)\n- --epochs (Number of epochs for fine-tuning transformer. Default is 20)\n- --noTrain (Skips the fine-tuning and embeds the query sequences with the base model)\n- --preTrained_model (Input path to your own pre-trained ESM model)\n- --batch_size (Change batch-size number for fine-tuning. Default is 5)\n- --blast (Enables "BLAST" mode. --database argument is required)\n- --model (Change ESM model. Default is esm2_t12_35M_UR50D. List of models can be found at https://github.com/facebookresearch/esm)\n- --strategy (Change training strategy. Default is None. List of strategies can be found at https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html)\n- --logger (Enable Tensorboard logger. Default is None)\n- --if1 (Utilize Inverse Folding model \'esm_if1_gvp4_t16_142M_UR50\' to facilitate fixed backbone sequence design. Basically converts protein structure to possible sequences)\n- --chain (Don\'t use right now)\n- --temp (Choose sampling temperature. Higher temps will have more sequence diversity, but less recovery of the original sequence)\n- --genIters (Adjust number of sequences generated for each chain of the input structure)\n\n## Examples\n\n### Default (Fine-tuning)\n  1. The default mode for the pipeline is to just fine-tune the base esm1_t12 model from FAIR with the query input.\n  ```\n  python3 main.py fine_tuning_ex ../data/query.fasta 4\n  ```\n### Embed with base esm1_t12 model\n  2. You can also embed proteins with just the base model from FAIR and completely skip fine-tuning.\n  ```\n  python3 main.py raw_embed ../data/query.fasta 4 --noTrain\n  ```\n### Embedding with a custom pre-trained model\n  3. If you have a pre-trained model, you can use it to embed sequences by passing the path to --preTrained_model. \n  ```\n  python3 main.py pre_trained ../data/query.fasta 4 --preTrained_model ../models/pre_trained_model.pt\n  ```\n### BLAST-like (Fine-tune on query and embed query+database)\n  4. To enable a BLAST-like functionality, you can use the --blast flag in conjuction with passing a database fasta file to --database. The base model from FAIR is first fine-tuned with the query sequences and then both the query and the database sequences are embedded.\n  ```\n  python3 main.py blast_search ../data/query.fasta 4 --blast --database ../data/database.fasta\n  ```\n### Distributed Training/Inference\n  5. In order to scale/speed up your analyses, you can distribute your training/inference across many GPUs with a few extra flags to your command. You can even fit models that do not normally fit on your GPUs with sharding and CPU-offloading. The list of strategies can be found here (https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html). The example below utilizes 16 GPUs in total (4(GPUs) * 4(--nodes)) with Fully Sharded Data Parallel and the 650M parameter ESM2 model.\n  ```\n  python3 main.py distributed_example ../data/query.fasta 4 --nodes 4 --strategy fsdp --model esm2_t33_650M_UR50D\n  ```\n### Generating protein sequences using inverse folding with ESM-IF1\n  6. When provided a protein backbone structure (.pdb, .cif), the IF1 model is able to predict a sequence that might be able to fold into the input structure. The example input are the backbone coordinates from DWARF14, a rice hydrolase. For every chain in the structure, 2 in 4ih9.pdb, the following command will generate 3 sequences. In total, 6 sequences will be generated.\n  ```\n  python3 main.py IF_Test ../data/4ih9.pdb 1 --if1 --gen_iters 3\n  ```\n## Quick Tutorial (NOT CURRENT, DON\'T USE):\n\n1. Type ```git clone https://github.com/martinez-zacharya/DistantHomologyDetection``` in your home directory on the HPC\n2. Download Miniconda by running ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh``` and then ```sh ./Miniconda3-latest-Linux-x86_64.sh```.\n3. Run ```conda env create -f environment.yml``` in the home directory of the repo to set up the proper conda environment and then type ```conda activate RemoteHomologyTransformer``` to activate it.\n4. Shift your current working directory to the scripts folder with ```cd scripts```.\n5. Type ```vi tutorial_slurm``` to open the slurm file and then hit ```i```.\n6. Change the email in the tutorial_slurm file to your email (You can use https://s3-us-west-2.amazonaws.com/imss-hpc/index.html to make your own slurm files in the future).\n7. Save the file by first hitting escape and then entering ```:x``` to exit and save the file. \n8. You can view the arguments for the command line tool by typing ```python3 main.py -h```.\n9. To run the tutorial analysis, make the tutorial slurm file exectuable with ```chmod +x tutorial_slurm.sh``` and then type ```sbatch tutorial_slurm.sh```.\n10. You can now safely exit the ssh instance to the HPC if you want\n\n## Misc. Tips\n\n- Make sure there are no "\\*" in the protein sequences\n- Don\'t run jobs on the login node, only submit jobs with sbatch or srun on the HPC\n- Caltech HPC Docs https://www.hpc.caltech.edu/documentation\n',
    'author': 'Zachary Martinez',
    'author_email': 'martinez.zacharya@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
