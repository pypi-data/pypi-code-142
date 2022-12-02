# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['daft',
 'daft.dataframe',
 'daft.execution',
 'daft.experimental',
 'daft.experimental.serving',
 'daft.experimental.serving.backends',
 'daft.experimental.serving.static',
 'daft.internal',
 'daft.internal.kernels',
 'daft.logical',
 'daft.runners',
 'daft.viz']

package_data = \
{'': ['*']}

install_requires = \
['fsspec',
 'loguru>=0.6.0,<0.7.0',
 'numpy>=1.16.6,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'polars[timezone]>=0.14.12,<0.15.0',
 'protobuf>=3.19.0,<3.20.0',
 'pyarrow>=6,<7',
 'pydot>=1.4.2,<2.0.0',
 'ray>=1.10.0',
 'tabulate>=0.8.10,<0.9.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.0.0',
                             'pickle5>=0.0.12,<0.0.13'],
 'aws': ['boto3>=1.23.0,<2.0.0', 's3fs'],
 'experimental': ['fastapi>=0.79.0,<0.80.0',
                  'docker>=5.0.3,<6.0.0',
                  'uvicorn>=0.18.2,<0.19.0',
                  'cloudpickle>=2.1.0,<3.0.0',
                  'boto3>=1.23.0,<2.0.0',
                  'PyYAML>=6.0,<7.0',
                  'icebridge>=0.0.4,<0.0.5',
                  'Pillow>=9.2.0,<10.0.0'],
 'iceberg': ['icebridge>=0.0.4,<0.0.5'],
 'serving': ['fastapi>=0.79.0,<0.80.0',
             'docker>=5.0.3,<6.0.0',
             'uvicorn>=0.18.2,<0.19.0',
             'cloudpickle>=2.1.0,<3.0.0',
             'boto3>=1.23.0,<2.0.0',
             'PyYAML>=6.0,<7.0']}

entry_points = \
{'console_scripts': ['build_inplace = build:build_inplace']}

setup_kwargs = {
    'name': 'getdaft',
    'version': '0.0.19',
    'description': 'A Distributed DataFrame library for large scale complex data processing.',
    'long_description': '|Banner|\n\n|CI| |PyPI| |Latest Tag|\n\n`Website <https://www.getdaft.io>`_ • `Docs <https://www.getdaft.io/docs>`_ • `Installation`_ • `10-minute tour of Daft <https://getdaft.io/docs/learn/10-min.html>`_ • `Community and Support <https://github.com/Eventual-Inc/Daft/discussions>`_\n\nDaft: the distributed Python dataframe for complex data\n=======================================================\n\n\n`Daft <https://www.getdaft.io>`_ is a fast, Pythonic and scalable open-source dataframe library built for Python and Machine Learning workloads.\n\n  **Daft is currently in its Alpha release phase - please expect bugs and rapid improvements to the project.**\n  **We welcome user feedback/feature requests in our** `Discussions forums <https://github.com/Eventual-Inc/Daft/discussions>`_\n\n**Table of Contents**\n\n* `About Daft`_\n* `Getting Started`_\n* `License`_\n\nAbout Daft\n----------\n\nThe Daft dataframe is a table of data with rows and columns. Columns can contain any Python objects, which allows Daft to support rich complex data types such as images, audio, video and more.\n\n1. **Any Data**: Columns can contain any Python objects, which means that the Python libraries you already use for running machine learning or custom data processing will work natively with Daft!\n2. **Notebook Computing**: Daft is built for the interactive developer experience on a notebook - intelligent caching/query optimizations accelerates your experimentation and data exploration.\n3. **Distributed Computing**: Rich complex formats such as images can quickly outgrow your local laptop\'s computational resources - Daft integrates natively with `Ray <https://www.ray.io>`_ for running dataframes on large clusters of machines with thousands of CPUs/GPUs.\n\nGetting Started\n---------------\n\nInstallation\n^^^^^^^^^^^^\n\nInstall Daft with ``pip install getdaft``.\n\nQuickstart\n^^^^^^^^^^\n\n  Check out our `full quickstart tutorial <https://getdaft.io/docs/learn/quickstart.html>`_!\n\nIn this example, we load images from an AWS S3 bucket and run a simple function to generate thumbnails for each image:\n\n.. code:: python\n\n    from daft import DataFrame, lit\n\n    import io\n    from PIL import Image\n\n    def get_thumbnail(img: Image.Image) -> Image.Image:\n        """Simple function to make an image thumbnail"""\n        imgcopy = img.copy()\n        imgcopy.thumbnail((48, 48))\n        return imgcopy\n\n    # Load a dataframe from files in an S3 bucket\n    df = DataFrame.from_files("s3://daft-public-data/laion-sample-images/*")\n\n    # Get the AWS S3 url of each image\n    df = df.select(lit("s3://").str.concat(df["name"]).alias("s3_url"))\n\n    # Download images and load as a PIL Image object\n    df = df.with_column("image", df["s3_url"].url.download().apply(lambda data: Image.open(io.BytesIO(data))))\n\n    # Generate thumbnails from images\n    df = df.with_column("thumbnail", df["image"].apply(get_thumbnail))\n\n    df.show(3)\n\n|Quickstart Image|\n\n\nMore Resources\n^^^^^^^^^^^^^^\n\n* `10-minute tour of Daft <https://getdaft.io/docs/learn/10-min.html>`_ - learn more about Daft\'s full range of capabilities including dataloading from URLs, joins, user-defined functions (UDF), groupby, aggregations and more.\n* `User Guide <https://getdaft.io/docs/learn/user_guides.html>`_ - take a deep-dive into each topic within Daft\n* `API Reference <https://getdaft.io/docs/api_docs/index.html>`_ - API reference for public classes/functions of Daft\n\nLicense\n-------\n\nDaft has an Apache 2.0 license - please see the LICENSE file.\n\n.. |Quickstart Image| image:: https://user-images.githubusercontent.com/17691182/200086119-fb73037b-8b4e-414a-9060-a44122f0c290.png\n   :alt: Dataframe code to load a folder of images from AWS S3 and create thumbnails\n   :height: 256\n\n.. |Banner| image:: https://user-images.githubusercontent.com/17691182/190476440-28f29e87-8e3b-41c4-9c28-e112e595f558.png\n   :target: https://www.getdaft.io\n   :alt: Daft dataframes can load any data such as PDF documents, images, protobufs, csv, parquet and audio files into a table dataframe structure for easy querying\n\n.. |CI| image:: https://github.com/Eventual-Inc/Daft/actions/workflows/python-package.yml/badge.svg\n   :target: https://github.com/Eventual-Inc/Daft/actions/workflows/python-package.yml?query=branch:main\n   :alt: Github Actions tests\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/getdaft.svg?label=pip&logo=PyPI&logoColor=white\n   :target: https://pypi.org/project/getdaft\n   :alt: PyPI\n\n.. |Latest Tag| image:: https://img.shields.io/github/v/tag/Eventual-Inc/Daft?label=latest&logo=GitHub\n   :target: https://github.com/Eventual-Inc/Daft/tags\n   :alt: latest tag\n',
    'author': 'Eventual Inc',
    'author_email': 'daft@eventualcomputing.com',
    'maintainer': 'Sammy Sidhu',
    'maintainer_email': 'sammy@eventualcomputing.com',
    'url': 'https://getdaft.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
