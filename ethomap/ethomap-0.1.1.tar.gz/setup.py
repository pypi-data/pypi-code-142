# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ethomap']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.0.0,<2.0.0',
 'numba>=0.56.0,<0.57.0',
 'numpy>=1.23,<2.0',
 'scikit-learn>=1.1.0,<2.0.0',
 'scipy>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'ethomap',
    'version': '0.1.1',
    'description': 'Generate behavioral embeddings of postural time series.',
    'long_description': '# Ethomap\n\nLightweight library with basic modules for generating behavioral embeddings from dynamic time warping of postural time\nseries. Also includes modules to decompose behavioral sequences into transition modes.\n\nBased on [Mearns et al. (2020)](https://www.sciencedirect.com/science/article/pii/S0960982219314617).\n\n# Installation\n\n```commandline\npip install ethomap\n```\n\n# Examples\n\n## Dynamic time warping\n\n```python\nfrom ethomap import DynamicTimeWarping  # from dtw module\nimport numpy as np\n\n# Create some 3D time series\nx = np.random.rand(200, 3)\ny = np.random.rand(200, 3)\n\n# Align time series y to x\ndtw = DynamicTimeWarping(x)\ndist = dtw.align(y)\nprint("DTW distance between x and y:", dist)\n```\n\n## Behavioral embedding\n\n```python\nfrom ethomap import pdist_dtw, affinity_propagation, IsomapPrecomputed\nimport numpy as np\nimport time\nfrom scipy.spatial.distance import squareform\n\n# Create some 3D time series to align pairwise\nxs = np.random.rand(1000, 50, 3)\n\n# Compute pairwise distances between time series (pdist_dtw from ethomap.distance)\nt0 = time.time()\ndistances = pdist_dtw(xs, parallel_processing=True, n_processors=4, bw=0.1, fs=100)\ndistance_matrix = squareform(distances)  # make square\nt1 = time.time()\nprint("Time taken:", t1 - t0, "seconds")  # ~30 seconds for data of this size\nprint(distance_matrix.shape)  # (1000, 1000)\n\n# Create behavioral space from all data (IsomapPrecomputed from ethomap.embed)\nisomap = IsomapPrecomputed(n_neighbors=5, n_components=2)\nembedding = isomap.fit_transform(distance_matrix)\nprint(embedding.shape)  # (1000, 2)\n\n# Find exemplars by clustering distance matrix (affinity_propagation from ethomap.cluster)\nap = affinity_propagation(distance_matrix, preference="median")\ncluster_labels = ap.labels_\nexemplar_indices = ap.cluster_centers_indices_\n\n# Select exemplars from original data\nexemplars = xs[exemplar_indices]\nexemplar_distances = distance_matrix[exemplar_indices, :][:, exemplar_indices]\nprint(exemplars.shape)  # (n_exemplars, 50, 3)\nprint(exemplar_distances.shape)  # (n_exemplars, n_exemplars)\n\n# Create behavioral space from exemplars only\nembedding_exemplars = isomap.fit_transform(exemplar_distances)\nprint(embedding_exemplars.shape)  # (n_exemplars, 2)\n```\n',
    'author': 'Duncan Mearns',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
