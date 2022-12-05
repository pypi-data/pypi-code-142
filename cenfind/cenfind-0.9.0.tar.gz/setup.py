# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cenfind',
 'cenfind.cli',
 'cenfind.core',
 'cenfind.evaluation',
 'cenfind.experiments',
 'cenfind.labelbox',
 'cenfind.sankaran']

package_data = \
{'': ['*'], 'cenfind': ['models/dev/multiscale/20221115_125221/*']}

install_requires = \
['csbdeep>=0.6.3,<0.7.0',
 'imageio>=2.16.0,<3.0.0',
 'numpy>=1.21.2,<1.22',
 'opencv-python>=4.5.5.62,<5.0.0.0',
 'pandas>=1.4.1,<2.0.0',
 'pytomlpp>=1.0.10,<2.0.0',
 'scikit-image>=0.19.2,<0.20.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'scipy>=1.7.1,<2.0.0',
 'spotipy-detector>=0.1.0,<0.2.0',
 'stardist>=0.8.3,<0.9.0',
 'tensorflow>=2.8.0,<3.0.0',
 'tifffile>=2022.5.4,<2023.0.0',
 'tqdm>=4.62.3,<5.0.0',
 'xarray>=0.21.1,<0.22.0']

entry_points = \
{'console_scripts': ['evaluate = cenfind.cli.evaluate:main',
                     'prepare = cenfind.cli.prepare:main',
                     'score = cenfind.cli.score:main',
                     'squash = cenfind.cli.squash:main',
                     'upload = cenfind.labelbox.upload_labels:main',
                     'vignettes = cenfind.labelbox.vignettes:main']}

setup_kwargs = {
    'name': 'cenfind',
    'version': '0.9.0',
    'description': 'Score centrioles in fluorescence images',
    'long_description': "# cenfind\n\nA command line interface to score cells for centrioles.\n\n## Introduction\n\n`cenfind` is a command line interface to detect and assign centrioles in immunofluorescence images of human cells. Specifically, it orchestrates:\n\n- the z-max projection of the raw files;\n- the detection of centrioles;\n- the detection of the nuclei;\n- the assignment of the centrioles to the nearest nucleus.\n\n## Installation\n\n1. Download `cenfind` with:\n\n```shell\npython -m venv test_cenfind\nsource test_cenfind/bin/activate\npip install cenfind\npip install tensorflow\npip install -e projects/spotipy\n```\n\n5. As of now, you need to install the spotipy package from the git repository https://github.com/maweigert/spotipy:\n\n```shell\ngit clone git@github.com:maweigert/spotipy.git\n```\n\n6. Add manually the package spotipy\n```shell\npip install -e ../spotipy/\n```\n\n7. Check that `cenfind`'s programs are correctly installed by running:\n\n```shell\nsquash --help\n```\n\n## Basic usage\nBefore scoring the cells, you need to prepare the dataset folder. `cenfind` assumes a fixed folder structure. In the following we will assume that the .ome.tif files are all immediately in raw/. Each field of view is a z-stack containing 4 channels (0, 1, 2, 3). The channel 0 contains the nuclei and the channels 1-3 contains centriolar markers.\n```text\n<project_name>/\n└── raw/\n```\n2. Run `prepare` to initialise the folder with a list of fields and output folders:\n```shell\nprepare /path/to/dataset 1 2 3 [--pixel_size, [--projection_suffix]]\n```\n\n2. Run `squash` with the argument of the path to the project folder and the suffix of the raw files. `projections/` is populated with the max-projections `*_max.tif` files.\n```shell\nsquash path/to/dataset\n```\n\n3. Run `score` with the arguments source and the index of the nuclei channel (usually 0 or 3).\n```shell\nscore path model channel_nuclei channels factor\n```\n\n4. Check that the predictions are satisfactory by looking at the folder `outlines` and at the results/scores.csv.\n\n## API\n\n`cenfind` consists of two core classes: `Dataset` and `Field`. The class `Dataset` represents a collection of fields with identical pixel size, channels, and cell type. The class `Field` represents a field of view and is responsible for calling the detection procedure and for managing (storing and writing) the predictions.\n\nUsing those two objects, `cenfind` should\n\n- detect centrioles (data, model) => points,\n- extract nuclei (data, model) => contours,\n- assign centrioles to nuclei (contours, points) => pairs\n- outline centrioles and nuclei (data, points) => image\n- create composite vignettes (data) => composite_image\n- flag partial nuclei (contours, tolerance) => contours\n- compare predictions with annotation (points, points) => metrics_namespace\n",
    'author': 'Leo Burgy',
    'author_email': 'leo.burgy@epfl.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/UPGON/cenfind',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
