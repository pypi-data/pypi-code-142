# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['italianswirls']

package_data = \
{'': ['*']}

install_requires = \
['jedi>=0.18,<0.19', 'pygls>=0.13,<0.14']

entry_points = \
{'console_scripts': ['italianswirls = italianswirls.cli:main']}

setup_kwargs = {
    'name': 'italianswirls',
    'version': '0.0.1',
    'description': 'Minimal Python language server based on Jedi',
    'long_description': "Italian Swirls 🍝\n=================\n\nMinimal Python language server, based on [Jedi][jedi] and [pygls][pygls].\n\n[jedi]: https://jedi.readthedocs.io/en/latest/index.html\n[pygls]: https://pygls.readthedocs.io/en/latest/index.html\n\nStill in development but works on my machine. ✨\n\nSupported features:\n\n| LSP method                    | Description                |\n|-------------------------------|----------------------------|\n| `textDocument/completion`     | Complete                   |\n| `textDocument/definition`     | Go to definition           |\n| `textDocument/typeDefinition` | Go to type definition      |\n| `textDocument/hover`          | Show documentation         |\n| `textDocument/references`     | Show references            |\n| `textDocument/rename`         | Renaming symbols and files |\n\n\n\nInstall\n-------\n\nTODO\n\n\n\nAbout\n-----\n\n### Why?\n\nGeneral-purpose servers (e.g. pyls, py-lsp) try to do too much and break stuff\ntoo often for me. Locking Neovim when I press tab, crashes of all kind,\nLspRestart failing. Also I like my linting and formatting done by dedicated\ntools such as [nvim-lint][nvim-lint] and [formatter][formatter].\n\n[nvim-lint]: https://github.com/mfussenegger/nvim-lint\n[formatter]: https://github.com/mhartington/formatter.nvim\n\nOther Jedi-based servers (e.g. jedi-language-server) seem to focus on coc-nvim\nand frequently fail on Neovim's native LSP client for me. I tried to fix\njedi-language-server several times when it failed me but I thought it could be\nfun to try pygls to redo it as small and simple as I can. And running a Node\nserver to get Python completions? No way. That said, jedi-language-server is a\ngood project and if you're fine with coc-nvim you should definitely check it\nout. Lots of the code here is ~~stolen~~ inspired from this project.\n\n### Why the name?\n\nTake the string “Is this a Star Wars reference?” Language Server, compress it to\n`ITASWRLS` and expand it back to Italian Swirls. Italian dishes are made of few\nelements that work well together. Enough questions!\n\n### License\n\nGPLv3.\n",
    'author': 'dece',
    'author_email': 'shgck@pistache.land',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.dece.space/Dece/ItalianSwirls',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
