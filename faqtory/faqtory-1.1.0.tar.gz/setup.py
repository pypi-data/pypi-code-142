# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['faqtory']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-frontmatter>=1.0.0,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'thefuzz[speedup]>=0.19.0,<0.20.0']

entry_points = \
{'console_scripts': ['faqtory = faqtory.cli:run']}

setup_kwargs = {
    'name': 'faqtory',
    'version': '1.1.0',
    'description': 'Auto FAQ builder',
    'long_description': '# FAQtory\n\nFAQtory is a tool to auto-generate a [FAQ.md](./FAQ.md) (Frequently Asked Questions) document for your project.\n\nAdditionally, a "suggest" feature uses fuzzy matching to reply to GitHub issues with suggestions from your FAQ.\n\n## Getting started\n\nInstall `faqtory` from PyPI. I\'m going to assume you know how to do this bit.\n\nRun the following from the directory you wish to store the FAQ document. \n\n```bash\nfaqtory init\n```\n\nThis will create the following files and directories:\n\n- `faq.yml` A configuration file which you can edit.\n- `./.faq/` A directory which will contain templates.\n- `./questions/` A directory containing question documents.\n\n## Adding questions\n\nTo add questions create a file with the extension `.question.md` in the questions directory (`./questions/` if you are using the defaults).\n\nQuestion documents are Markdown with front-matter. Here\'s an example:\n\n```yml\n---\ntitle: "What does FAQ stand for?"\nalt_titles:\n  - "What is the meaning of FAQ?"\n  - "What does FAQ mean?"\n---\n\nFAQ stands for *Frequently Asked Questions*\n```\n\nThe filename is unimportant, but a `title` is mandatory. You can also optionally add alternative titles under `alt_titles` which will be used with the `faqtory suggest` feature (but not displayed).\n\n## Building\n\nRun the following command to build the FAQ:\n\n```bash\nfaqtory build\n```\n\nWith the default settings this will generate an [FAQ.md](./FAQ.md) file.\n\n\n## Suggest\n\nThe "suggest" subcommand can compile a list of FAQ entries that match a supplied issue title. Here\'s an example:\n\n```bash\nfaqtory suggest "who is the author of FAQtory?"\n```\n\nThis will generate a list of matching entries from the FAQ, and write Markdown to stdout. You can modify the output with the "suggest.md" template, which you will find in your ".faq/" directory (if you haven\'t configured it elsewhere),\n\nThis feature is designed to be used with a GitHub action to post an automated response. To enable this feature, copy [new_issue.yml](https://github.com/willmcgugan/faqtory/blob/main/.github/workflows/new_issue.yml) to a similarly named directory in your repository.\n\n\n## Disclaimer\n\nThis was a hastily put together tool by a maintainer that was tired of responding to the same old issues. I can\'t devote much time to this project, but I will happily accept PRs!\n',
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
