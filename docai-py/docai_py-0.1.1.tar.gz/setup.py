# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docai',
 'docai.annotations',
 'docai.common',
 'docai.generated',
 'docai.generated.api',
 'docai.generated.api.apps',
 'docai.generated.api.auth',
 'docai.generated.api.billing',
 'docai.generated.api.create_doc_type_jobs',
 'docai.generated.api.default',
 'docai.generated.api.document_types',
 'docai.generated.api.features',
 'docai.generated.api.ml_models',
 'docai.generated.api.model_library',
 'docai.generated.api.models',
 'docai.generated.api.queues',
 'docai.generated.api.users',
 'docai.generated.models',
 'docai.models',
 'docai.models.tests',
 'docai.predictions',
 'docai.test',
 'docai.training']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.3.0,<23.0.0',
 'evaluate>=0.3.0,<0.4.0',
 'httpx>=0.15.4,<0.24.0',
 'numpy>=1.17.0,<2.0.0',
 'pdf2image>=1.14.0,<2.0.0',
 'pillow>=8.0.0,<10.0.0',
 'python-dateutil>=2.8.1,<2.9.0',
 'seqeval>=1.2.2,<2.0.0',
 'transformers>=4.20.0,<5.0.0',
 'typing-extensions>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'docai-py',
    'version': '0.1.1',
    'description': 'Butler Doc AI',
    'long_description': '# Butler DocAI\n\nDocAI helps developers quickly build document, image and text processing pipelines using open source and cloud-based machine learning models for a wide range of applications.\n\n---\n\n🚧 DocAI is still a work-in-progress and undergoing early development.\n\nOur goal is to put modern machine-learning technology in the hands of the 20+ million developers in the world. If this excites you, we are looking for early adopters to come along for the ride!\n\n## Requirements\n\nPython >= 3.7\n\n## Installation & Usage\n\nTo install DocAI with pip:\n\n```sh\n\npip install docai-py\n\n```\n\n### System Dependencies\n\n#### Mac\n\n- Install [poppler](http://macappstore.org/poppler/)\n\n#### Linux\n\n- Install poppler-utils via your package manager\n\n## Getting Started\n\nPlease follow the [installation procedure](#installation--usage) and then run the following:\n\n```python\n\n\n\nfrom docai import PredictionClient\n\n\n\n# Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key\n\napi_key = \'<api-key>\'\n\n# Get Queue ID from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#go-to-the-model-details-page\n\nqueue_id = \'<queue_id>\'\n\n# Path to a local JPEG, PNG, or PDF file\n\nlocal_file_path = \'example.pdf\'\n\n\n\nextraction_results = PredictionClient(api_key).extract_document(queue_id, local_file_path)\n\nprint(extraction_results)\n\n```\n\n## Maintain\n\n### Install Packages for Development\n\nInstall [poetry](https://python-poetry.org/docs/#installation) on your host machine\n\n```sh\n\npoetry install\n\n```\n\n### Butler REST API Codegen\n\nTo regenerate code updates to REST API:\n\n```sh\n\nopenapi-python-client update --url https://app.butlerlabs.ai/api/docs-json --config codegen.yaml\n\n```\n\n### Running Unit Tests\n\nTo run all unit tests:\n\n```sh\npoetry run pytest -v -m unit_tests\n```\n\nAlternatively, you can also use VSCode\'s "Testing" tab to run/debug individual tests\n\n\n### Adding a New Dependency\n\nTo add a new pip package dependency, see [poetry add](https://python-poetry.org/docs/cli/#add).\n\nFor versioning, it is best to use the minimum version that works, combined with `^`, `~`, or `>=` and `<` checks.\n\nFor example:\n\n- `poetry add my-package@^1.2.3` is a shorthand for `>=1.2.3,<2.0.0`\n\n- `poetry add my-package@~1.2.3` is a shorthand for `>=1.2.3,<1.3.0`\n\n- `poetry add "my-package>=1.2.3,<4.5.6"`\n\nFor development only dependencies, make sure to include the `--dev` flag.\n\n### Build and Publish\n\n#### Build and Publish Setup\n\n```sh\n\n# setup for testpypi\n\npoetry config repositories.testpypi https://test.pypi.org/legacy/\n\npoetry config pypi-token.testpypi <testpypi token>\n\n\n\n# setup for pypi\n\npoetry config repositories.pypi https://upload.pypi.org/legacy/\n\npoetry config pypi-token.pypi <pypi token>\n\n```\n\n#### Build and Publish Procedure\n\nUpdate `pyproject.toml` and `docai/__init__.py` to have a new version number\n\n```sh\n\n# build packages\n\npoetry build\n\n\n\n# upload to test pypi\n\npoetry publish -r testpypi\n\n\n\n# test install from test pypi\n\npip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple docai-py\n\n\n\n# upload to real pypi\n\npoetry publish -r pypi\n\n```\n',
    'author': 'Butler Labs',
    'author_email': 'support@butlerlabs.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://butlerlabs.ai',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
