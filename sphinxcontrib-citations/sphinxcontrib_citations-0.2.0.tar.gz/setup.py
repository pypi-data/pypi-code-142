# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['sphinxcontrib', 'sphinxcontrib.citations']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=4.0', 'requests>=2.0,<3.0', 'sphinxcontrib-bibtex>=2.0,<3.0']

setup_kwargs = {
    'name': 'sphinxcontrib-citations',
    'version': '0.2.0',
    'description': 'Create a list with all the papers that cite yours',
    'long_description': '# sphinxcontrib-citations\n[![PyPI version](https://badge.fury.io/py/sphinxcontrib-citations.svg)](https://badge.fury.io/py/sphinxcontrib-citations)\n[![Test](https://github.com/Sbozzolo/sphinxcontrib-citations/actions/workflows/test.yml/badge.svg)](https://github.com/Sbozzolo/sphinxcontrib-citations/actions/workflows/test.yml)\n\nIt is often the case that open-source software enables new scientific\ndevelopments. When this happens, it is desirable to highlight which new results\nwere obtained with a given piece of software. If your project has one or more\nassociated published resources (for example, in the Journal of Open-Source\nSoftware, or in Zenodo), you can use `sphinxcontrib-citations` to generate a\npage in your documentations that lists the papers that cite your code.\n\n`sphinxcontrib-citations` is an Sphinx extension that uses NASA\'s ADS to look up\nwhich papers cite a given list of references. `sphinxcontrib-citations` is\ncurrently in a state of minimum-viable-product: the basic features are\navailable, but not much else. Pull request are welcome.\n\nTo use `sphinxcontrib-citations`, first install it and add it to the\n`extensions` variable in your `conf.py` as `sphinxcontrib.citations`.\n`sphinxcontrib-citations` has only three options:\n\n- `citations_ads_token`: this is the ADS API token, and it required for the\n  correct functioning of the extension. You need a freely obtainable API token\n  to use this package. [Read more about NASA ADS\n  API](https://ui.adsabs.harvard.edu/help/api/).\n- `citations_bibcode_list`: this is the list of bibcodes for which citations\n  have to be found. You can find the bibcode for a given paper on ADS.\n- `citations_bibtex_file`: this is the name of the `.bib` file that will be\n  generated. If not specified, it will be `sphinxcontrib_citations.bib`. If a\n  file with the given path already exists, it will be silently overwritten.\n\nWhen you compile your documentation, `sphinxcontrib-citations` will find all the\nreferences and create a `bib` file. Then, `sphinxcontrib-citations` interfaces\nwith `sphinxcontrib-bibtex` to produce the page. You can use all the options\nprovided by that package. A simple page might look like:\n\n``` restructuredtext\nPapers citing this software\n=============================================\n\n.. bibliography:: sphinxcontrib_citations.bib\n   :list: enumerated\n   :all:\n```\n\nMake sure that the name of the file matches your choice for\n`citations_bibtex_file`.\n\n### ADS API Token in GitHub actions\n\nClearly, committing the API token directly to GitHub is not a good idea. GitHub\nactions support [encrypted\nsecrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)\nthat can be used to safely store the token.\n\nAssuming you create a repository secret named `ADS_API` (that contains the\ntoken), you can pass it to `Sphinx` through an environment variable. For\ninstance, the action step might look like:\n``` yaml\n- name: Produce documentation\n  env:\n      ADS_API: ${{ secrets.ADS_API }}\n  run: |\n    make html\n```\nwith `citations_ads_token = os.environ["ADS_API"]` in the `conf.py`.\n\n### Example\n\nFor an example, see\n[kuibit](https://sbozzolo.github.io/kuibit/dev/citations.html).\n\nThe relevant Sphinx configuration settings that generated this example are:\n``` python\ncitations_ads_token = os.environ["ADS_API"]\ncitations_bibcode_list = ["2021JOSS....6.3099B"]\n```\n\n',
    'author': 'Gabriele Bozzola',
    'author_email': 'sbozzolator@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sbozzolo/sphinx-citations',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
