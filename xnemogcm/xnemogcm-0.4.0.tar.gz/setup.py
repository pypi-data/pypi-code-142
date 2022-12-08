# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xnemogcm', 'xnemogcm.test']

package_data = \
{'': ['*'],
 'xnemogcm.test': ['data/4.0.0/domcfg_1_file/*',
                   'data/4.0.0/domcfg_mesh_mask/*',
                   'data/4.0.0/domcfg_multi_files/*',
                   'data/4.0.0/mesh_mask_multi_files/*',
                   'data/4.0.0/nemo/*',
                   'data/4.0.0/nemo_no_grid_in_filename/*',
                   'data/4.0.0/open_and_merge/*',
                   'data/4.0.0/runs/*',
                   'data/4.0.0/runs/EXP_1_proc/*',
                   'data/4.0.0/runs/EXP_4_procs/*',
                   'data/4.0.0/surface_fields/*',
                   'data/namelist/*']}

install_requires = \
['dask[array]', 'netcdf4>=1.5.8', 'xarray>=0.21.1']

extras_require = \
{'dev': ['f90nml>=1.3.1',
         'xgcm>=0.6.0',
         'pytest>=6.2.5',
         'black>=22.10.0,<23.0.0',
         'jupyterlab>=3.5.1'],
 'metrics': ['xgcm>=0.6.0'],
 'namelist': ['f90nml>=1.3.1'],
 'test': ['f90nml>=1.3.1', 'xgcm>=0.6.0', 'pytest>=6.2.5']}

setup_kwargs = {
    'name': 'xnemogcm',
    'version': '0.4.0',
    'description': 'Interface to open NEMO global circulation model output dataset and create a xgcm grid.',
    'long_description': "# xnemogcm\n\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5724577.svg)](https://doi.org/10.5281/zenodo.5724577)\n\nInterface to open NEMO ocean global circulation model output dataset and create a xgcm grid.\n\n\n## Usage\n\n```python\nfrom pathlib import Path\nfrom xnemogcm import open_nemo_and_domain_cfg\n\nds = open_nemo_and_domain_cfg(\n    nemo_files='/path/to/output/files',\n    domcfg_files='/path/to/domain_cfg/mesh_mask/files'\n)\n\n# Interface with xgcm\nfrom xnemogcm import get_metrics\nimport xgcm\ngrid = xgcm.Grid(ds, metrics=get_metrics(ds), periodic=False)\n```\n\nSee the [example](https://nbviewer.ipython.org/github/rcaneill/xnemogcm/blob/master/example/)\ndirectory for some jupyter notebook examples.\nxnemocgm is able to process xarray.Datasets (e.g. they could be retrieved from a remote server),\nand can get information of the variables grid points with multiple options\n(see [example/open_process_files.ipynb](https://nbviewer.ipython.org/github/rcaneill/xnemogcm/blob/master/example/open_process_files.ipynb).\n\n### Note\n\n`xnemogcm` is capable or recombining the domain_cfg and mesh_mask files outputted\nby multiple processors,\nthe recombining tool from the NEMO toolbox is thus not needed here, see\nthe [example/recombing_mesh_mask_domain_cfg.ipynb](https://nbviewer.ipython.org/github/rcaneill/xnemogcm/blob/master/example/recombing_mesh_mask_domain_cfg.ipynb)\n\n## Installation\n\nInstallation via pip:\n```bash\npip3 install xnemogcm\n```\n\nInstallation via conda:\n```bash\nconda install -c conda-forge xnemogcm\n```\n\n## Requirements for dev\n\nWe use *poetry* to set up a virtual environment containing all\nneeded packages to run xnemogcm and the tests.\nTo install all the dependencies, type `poetry install -E dev`\nafter cloning the directory. This will create a new virtual environment.\nTyping `poetry shell` in the package directory will activate the virtual environment.\n\n## What's new\n\n### v0.4.0 (2022-12-08)\n* Optimize speed\n* Add option to decode grid type from attributes\n* Shift from pipenv and setupy.py to poetry\n* Refactor data test to allow testing of multiple version of NEMO\n\n### v0.3.4 (2021-06-15)\n* Adding some example\n* Bug fixes\n* Add option to compute extra scale factors\n\n### v0.3.2 - v0.3.3 (2021-05-05)\n* By default adds the lat/lon/depth variables of domcfg as coordinates\n\n### v0.3.1 (2021-05-04)\n* Minor bug fix when merging\n* better squeezing of time in domcfg + nemo v3.6 compatibility\n\n### v0.3.0 (2021-04-13)\n* Cleaning the backend\n* Removing the saving options (that were useless and confusing)\n* Minor bug fixes\n* Tested with realistic regional configuration\n\n### v0.2.3 (2021-03-15)\n* Support for surface only files\n* Reshaping the data files for the tests (dev)\n",
    'author': 'Romain Caneill',
    'author_email': 'romain.caneill@gu.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rcaneill/xnemogcm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
