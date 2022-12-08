# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qualle',
 'qualle.features',
 'qualle.features.label_calibration',
 'qualle.interface',
 'qualle.label_calibration']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.66,<0.67',
 'pydantic>=1.8.2,<1.9',
 'rdflib>=4.2,<4.3',
 'scikit-learn>=0.24,<0.25',
 'scipy>=1.6,<1.7',
 'stwfsapy==0.1.5',
 'uvicorn>=0.14,<0.15']
 
entry_points = \
{'console_scripts': ['qualle = qualle.interface.cli:cli_entrypoint']}


setup_kwargs = {
    'name': 'qualle',
    'version': '0.1.1',
    'description': 'A framework to predict the quality of a multi-label classification result',
    'long_description': '# Qualle\n![CI](https://github.com/zbw/qualle/actions/workflows/main.yml/badge.svg)\n[![codecov](https://codecov.io/gh/zbw/qualle/branch/master/graph/badge.svg?token=ZE7OWKA83Q)](https://codecov.io/gh/zbw/qualle)\n\nThis is an implementation of the Qualle framework as proposed in the paper\n[1] and accompanying source code.\n\nThe framework allows to train a model which can be used to predict\nthe quality of the result of applying a multi-label classification (MLC) \nmethod on a document. In this implementation, only the\n[recall](https://en.wikipedia.org/wiki/Precision_and_recall) \nis predicted for a document, but in principle\nany document-level quality estimation (such as the prediction of precision) \ncan be implemented analogously.\n\nQualle provides a command-line interface to train\nand evaluate models. In addition, a REST webservice for predicting\nthe recall of a MLC result is provided.\n\n### Command line interface (CLI)\nIn order to run the CLI, you must install the packages from the Pipfile.\nThe interface is then accessible from the module ``qualle.main``. To\nsee the help message, run (inside the Qualle directory)\n\n``python -m qualle.main -h``\n\n\n### Train\nIn order to train a model you have to provide a training data file.\nThis file has to be a tabular-separated file (tsv) in the format (tabular is marked with ``\\t``)\n\n```document-content\\tpredicted_labels_with_scores\\ttrue_labels```\n\nwhere\n- ``document-content`` is a string describing the content of the document\n(more precisely: the string on which the MLC method is trained), e.g. the title\n- ``predicted_labels_with_scores`` is a comma-separated list of pairs ``predicted_label:confidence-score``\n(this is basically the output of the MLC method)\n- ``true_labels`` is a comma-separated list of true labels (ground truth)\n\nFor example, a row in the data file could look like this:\n\n``Optimal investment policy of the regulated firm\\tConcept0:0.5,Concept1:1\\tConcept0,Concept3``\n\nTo train a model, use the ``main`` module inside ``qualle``, e.g.:\n\n``python -m qualle.main train /path/to/train_data_file /path/to/output/model``\n\nIt is also possible to use label calibration using the subthesauri of a thesaurus (such as the [STW](http://zbw.eu/stw/version/latest/about))\nas categories (please read the paper for more explanations). Consult the help (see above) for the required options.\n\n### Evaluate\nYou must provide a test data file and the path to a trained model in order to evaluate that model.\nThe test data file has the same format as the training data file. Metrics\nsuch as the [explained variation](https://en.wikipedia.org/wiki/Explained_variation) are printed out, describing the quality\nof the recall prediction (please consult the paper for more information).\n\n### REST interface\nTo perform the prediction on a MLC result, a REST interface can be started. \n[uvicorn](https://www.uvicorn.org/) is used as HTTP server. You can also use any\nASGI server implementation and create the ASGI app directly with the method\n``qualle.interface.rest.create_app``. You need to provide the environment variable\nMODEL_FILE with the path to the model (see ``qualle.interface.config.RESTSettings``).\n\nThe REST endpoint expects a HTTP POST with the result of a MLC for a list of documents\nas body. The format is JSON as specified in ``qualle/openapi.json``. You can also use\nthe Swagger UI accessible at ``http://address_of_server/docs`` to play around a bit.\n\n### Deployment with Docker\nYou can use the Dockerfile included in this project to build a Docker image. E.g.:\n\n ``docker build -t qualle .``\n\nPer default, gunicorn is used to run the REST interface on ``0.0.0.0:8000``\nYou need to pass the required settings per environment variable. E.g.:\n\n``docker run --rm -it --env model_file=/model -v /path/to/model:/model -p 8000:8000 qualle``\n\nOf course you can also use the Docker image to train or evaluate by using a \ndifferent command as input to [docker run](https://docs.docker.com/engine/reference/run/#general-form).\n\n## References\n[1] [Toepfer, Martin, and Christin Seifert. "Content-based quality estimation for automatic subject indexing of short texts under precision and recall constraints." International Conference on Theory and Practice of Digital Libraries. Springer, Cham, 2018., DOI 10.1007/978-3-030-00066-0_1](https://arxiv.org/abs/1806.02743)\n\n## Context information\nThis code was created as part of the subject indexing automatization effort at [ZBW - Leibniz Information Centre for Economics](https://www.zbw.eu/en/). See [our homepage](https://www.zbw.eu/en/about-us/key-activities/automated-subject-indexing) for more information, publications, and contact details.\n',
    'author': 'AutoSE',
    'author_email': 'autose@zbw.eu',
    'url': 'https://github.com/zbw/qualle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
     'classifiers': [
         "Intended Audience :: Science/Research",
         "License :: OSI Approved :: Apache Software License",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    'entry_points': entry_points
}


setup(**setup_kwargs)
