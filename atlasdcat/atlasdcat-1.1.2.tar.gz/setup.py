# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['atlasdcat']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'coverage>=6.5.0,<7.0.0',
 'datacatalogtordf>=3.0.0,<4.0.0',
 'pyapacheatlas>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'atlasdcat',
    'version': '1.1.2',
    'description': 'A library for managing DCAT metadata using Apache Atlas',
    'long_description': '# atlasdcat\n\n![Tests](https://github.com/Informasjonsforvaltning/atlasdcat/workflows/Tests/badge.svg)\n[![codecov](https://codecov.io/gh/Informasjonsforvaltning/atlasdcat/branch/main/graph/badge.svg?token=H4pXcHr8KK)](https://codecov.io/gh/Informasjonsforvaltning/atlasdcat)\n[![PyPI](https://img.shields.io/pypi/v/atlasdcat.svg)](https://pypi.org/project/atlasdcat/)\n[![Read the Docs](https://readthedocs.org/projects/atlasdcat/badge/)](https://atlasdcat.readthedocs.io/)\n\nA Python library for mapping [Apache Atlas](https://atlas.apache.org/) Glossary terms to DCAT metadata and vice versa.\n\nSpecification [the Norwegian Application Profile](https://data.norge.no/specification/dcat-ap-no) of [the DCAT standard](https://www.w3.org/TR/vocab-dcat-2/).\n\n> **Notice**\n> This library is part of the DCAT for Apache Atlas lifecycle and **not a complete solution**. The complete lifecycle contains the following actions:\n>\n> - Create glossary\n> - Add dataset descriptions by using atlasdcat mapper (this library)\n> - Assign dataset description glossary terms to entities (actual datasets)\n> - Fetch glossary terms as DCAT catalog in RDF format (this library)\n\n\n## Usage\n\n### Install\n\n```Shell\n% pip install atlasdcat\n```\n\n### Getting started\n\n#### Setup mapper\n\n```Python\n# Example...\nfrom atlasdcat import AtlasDcatMapper, AtlasGlossaryClient\nfrom pyapacheatlas.auth import BasicAuthentication\n\natlas_auth = BasicAuthentication(username="dummy", password="dummy")\natlas_client = AtlasGlossaryClient(\n    endpoint_url="http://atlas", authentication=atlas_auth\n)\n\nmapper = AtlasDcatMapper(\n    glossary_client=atlas_client,\n    glossary_id="myglossary",\n    catalog_uri="https://domain/catalog",\n    catalog_language="http://publications.europa.eu/resource/authority/language/NOB",\n    catalog_title="Catalog",\n    catalog_publisher="https://domain/publisher",\n    dataset_uri_template="http://domain/datasets/{guid}",\n    distribution_uri_template="http://domain/distributions/{guid}",\n    language="nb",\n)\n```\n\n#### Map glossary terms to DCAT Catalog RDF resource\n\n```Python\ntry:\n    mapper.fetch_glossary()\n    catalog = mapper.map_glossary_terms_to_dataset_catalog()\n    print(catalog.to_rdf())\nexcept Exception as e:\n    print(f"An exception occurred: {e}")\n```\n\n#### Map DCAT Catalog RDF resource to glossary terms\n\n```Python\ncatalog = Catalog()\ncatalog.identifier = "http://catalog-uri"\ncatalog.title = {"nb": "mytitle"}\ncatalog.publisher = "http://publisher"\ncatalog.language = ["nb"]\ncatalog.license = ""\n\ndataset = Dataset()\ndataset.title = {"nb": "Dataset"}\ndataset.description = {"nb": "Dataset description"}\ncatalog.datasets = [dataset]\n\ntry:\n    mapper.fetch_glossary()\n    mapper.map_dataset_catalog_to_glossary_terms(catalog)\n    mapper.save_glossary_terms()\nexcept Exception as e:\n    print(f"An exception occurred: {e}")\n```\n\nFor an example of usage of this library in a simple server, see [example](./example/README.md).\n\n## Development\n\n### Requirements\n\n- [pyenv](https://github.com/pyenv/pyenv) (recommended)\n- python3\n- [poetry](https://python-poetry.org/)\n- [nox](https://nox.thea.codes/en/stable/)\n\n```Shell\n% pip install poetry==1.1.13\n% pip install nox==2022.1.7\n% pip inject nox nox-poetry==1.0.0\n```\n\n### Install developer tools\n\n```Shell\n% git clone https://github.com/Informasjonsforvaltning/atlasdcat.git\n% cd atlasdcat\n% pyenv install 3.8.12\n% pyenv install 3.9.10\n% pyenv install 3.10.\n% pyenv local 3.8.12 3.9.10 3.10.\n% poetry install\n```\n\n### Run all sessions\n\n```Shell\n% nox\n```\n\n### Run all tests with coverage reporting\n\n```Shell\n% nox -rs tests\n```\n\n### Debugging\n\nYou can enter into [Pdb](https://docs.python.org/3/library/pdb.html) by passing `--pdb` to pytest:\n\n```Shell\nnox -rs tests -- --pdb\n```\n\nYou can set breakpoints directly in code by using the function `breakpoint()`.\n',
    'author': 'Jeff Reiffers',
    'author_email': 'jeff@ouvir.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Informasjonsforvaltning/atlasdcat',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
