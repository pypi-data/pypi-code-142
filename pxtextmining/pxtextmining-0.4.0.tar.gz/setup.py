# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pxtextmining',
 'pxtextmining.factories',
 'pxtextmining.helpers',
 'pxtextmining.pipelines']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'SQLAlchemy==1.3.23',
 'blis==0.7.4',
 'catalogue==1.0.0',
 'certifi==2021.5.30',
 'chardet==4.0.0',
 'click==8.0.1',
 'cycler==0.10.0',
 'cymem==2.0.5',
 'emojis>=0.6.0,<0.7.0',
 'idna==2.10',
 'imbalanced-learn==0.7.0',
 'joblib>=1.2.0,<2.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'kiwisolver==1.3.1',
 'matplotlib==3.3.2',
 'mkdocs>=1.4.2,<2.0.0',
 'mkdocstrings-python>=0.8.2,<0.9.0',
 'mkdocstrings>=0.19.0,<0.20.0',
 'murmurhash==1.0.5',
 'mysql-connector-python==8.0.23',
 'nltk==3.6.6',
 'numpy>=1.22',
 'pandas==1.2.3',
 'pickleshare==0.7.5',
 'plac==1.1.3',
 'preshed==3.0.5',
 'protobuf>=3.18.3',
 'pyparsing==2.4.7',
 'python-dateutil>=2.8.2',
 'pytz==2021.1',
 'regex==2021.8.3',
 'requests==2.25.1',
 'scikit-learn==0.23.2',
 'scipy==1.6.3',
 'seaborn==0.11.0',
 'six==1.16.0',
 'spacy==2.3.5',
 'srsly==1.0.5',
 'tensorflow>=2.11.0,<3.0.0',
 'textblob==0.15.3',
 'thinc==7.4.5',
 'threadpoolctl==2.1.0',
 'tqdm==4.61.0',
 'transformers>=4.24.0,<5.0.0',
 'urllib3==1.26.5',
 'vaderSentiment==3.3.2',
 'wasabi==0.8.2']

setup_kwargs = {
    'name': 'pxtextmining',
    'version': '0.4.0',
    'description': 'Text classification of patient experience feedback.',
    'long_description': '# pxtextmining: Text Classification of Patient Experience feedback\n\n## Project description\n**pxtextmining** is a Python package for classifying and conducting sentiment analysis of patient feedback comments, collected via the [NHS England Friends and Family Test](https://www.england.nhs.uk/fft/) (FFT).\n\nThere are two parts to the package. The first, comprising the majority of the codebase, is a machine learning pipeline that trains a model using labelled data. This pipeline outputs a fully trained model which can predict either \'criticality\' scores or a thematic \'label\' category for some feedback text. Examples of this can be found in the \'execution\' folder.\n\nThe second part utilises the trained model to make predictions on unlabelled feedback text, outputting predicted labels or criticality scores. An example of how this works using a model trained to predict \'label\' is given below:\n\n```\ndataset = pd.read_csv(\'datasets/text_data.csv\')\npredictions = factory_predict_unlabelled_text(dataset=dataset, predictor="feedback", pipe_path_or_object="results_label/pipeline_label.sav")\n```\n\n__We are working openly by open-sourcing the analysis code and data where possible to promote replication, reproducibility and further developments (pull requests are more than welcome!). We are also automating common steps in our workflow by shipping the pipeline as a [Python](https://www.python.org/) package broken down into sub-modules and helper functions to increase usability and documentation.__\n\n## Documentation\n\nFull documentation, including installation instructions, is available on our [documentation page](https://cdu-data-science-team.github.io/pxtextmining/).\n\n## Pipeline to train a new model\n\nThe pipeline is built with Python\'s [`Scikit-learn`](https://scikit-learn.org/stable/index.html) (Pedregosa et al., 2011). The pipeline performs a randomized search ([`RandomizedSearchCV()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV)) to identify the best-performing learner and (hyper)parameter values.\n\nBreakdown of the pipeline process, built by the functions in [pxtextmining.factories](https://github.com/CDU-data-science-team/pxtextmining/tree/main/pxtextmining/factories):\n\n1. The data is loaded and split into training and test sets `factory_data_load_and_split`. This module also conducts some basic text preprocessing, such as removing special characters, whitespaces and linebreaks. It produces additional features through the creation of \'text_length\' and sentiment scores using [vaderSentiment](https://pypi.org/project/vaderSentiment/) and [textblob](https://pypi.org/project/textblob/).\n\n2. The function in `factory_pipeline` creates an sklearn pipeline. This pipeline is comprised of the following steps: first, the preprocessed text input is upsampled to help compensate for the unbalanced dataset. The text is then tokenized and vectorised using either [spacy](https://spacy.io/) or [wordnet](https://wordnet.princeton.edu/). Feature selection is then conducted. A hyperparameter grid is constructed with potential hyperparameter values, depending on the learners/classification models to be tested in the Randomized Search. The pipeline is then fitted on the dataset to identify the best model.\n\n3. The fitted pipeline is then evaluated on the test set in `factory_model_performance`. The evaluation metrics used are: ([Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html), [Class Balance Accuracy](https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=4544&context=etd) (Mosley, 2013), [Balanced Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html) (Guyon et al., 2015, Kelleher et al., 2015) and [Matthews Correlation Coefficient](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html) (Baldi et al., 2000, Matthews, 1975)). A visual representation of the performance evaluation is output in the form of a barchart.\n\n4. Writing the results: The fitted pipeline, tuning results, predictions, accuracy\nper class, model comparison barchart, training data index, and test data index are output by `factory_write_results`.\n\nThe four steps above are all pulled together in [`pxtextmining.pipelines.text_classification_pipeline`](https://github.com/CDU-data-science-team/pxtextmining/tree/main/pxtextmining/pipelines).\n\n\n## References\nBaldi P., Brunak S., Chauvin Y., Andersen C.A.F. & Nielsen H. (2000). Assessing\nthe accuracy of prediction algorithms for classification: an overview.\n_Bioinformatics_  16(5):412--424.\n\nGuyon I., Bennett K. Cawley G., Escalante H.J., Escalera S., Ho T.K., Macià N.,\nRay B., Saeed M., Statnikov A.R, & Viegas E. (2015). [Design of the 2015 ChaLearn AutoML Challenge](https://ieeexplore.ieee.org/document/7280767),\nInternational Joint Conference on Neural Networks (IJCNN).\n\nKelleher J.D., Mac Namee B. & D’Arcy A.(2015).\n[Fundamentals of Machine Learning for Predictive Data Analytics: Algorithms, Worked Examples, and Case Studies](https://mitpress.mit.edu/books/fundamentals-machine-learning-predictive-data-analytics).\nMIT Press.\n\nMatthews B.W. (1975). Comparison of the predicted and observed secondary\nstructure of T4 phage lysozyme. _Biochimica et Biophysica Acta (BBA) - Protein Structure_ 405(2):442--451.\n\nPedregosa F., Varoquaux G., Gramfort A., Michel V., Thirion B., Grisel O.,\nBlondel M., Prettenhofer P., Weiss R., Dubourg V., Vanderplas J., Passos A.,\nCournapeau D., Brucher M., Perrot M. & Duchesnay E. (2011),\n[Scikit-learn: Machine Learning in Python](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html).\n_Journal of Machine Learning Research_ 12:2825--2830\n\n[^1]: A vritual environment can also be created using Conda, where the commands\nfor creating and activating it are a little different. See [this](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).\n',
    'author': 'CDU Data Science',
    'author_email': 'cdudatascience@nottshc.nhs.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CDU-data-science-team/pxtextmining',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
