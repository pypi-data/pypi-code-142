# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitz', 'gitz.git', 'gitz.program']

package_data = \
{'': ['*']}

scripts = \
['git-adjust',
 'git-copy',
 'git-delete',
 'git-for-each',
 'git-gitz',
 'git-go',
 'git-infer',
 'git-multi-pick',
 'git-new',
 'git-permute',
 'git-rename',
 'git-rot',
 'git-save',
 'git-split',
 'git-st',
 'git-stripe',
 'git-update',
 'git-when']

setup_kwargs = {
    'name': 'gitz',
    'version': '1.4.1',
    'description': '🗜 gitz - tiny useful git commands, some dangerous 🗜',
    'long_description': "🗜 gitz - git commands for rapid development 🗜\n------------------------------------------------------\n\nThis is a collection of seventeen git utilities aimed at people doing rapid\ndevelopment using Git.\n\nGitz is for two types of users - quality-obsessed individuals who relentlessly\nmanicure their pull requests until every byte is in the right place; and\nultra-rapid developers who want to generate large features quickly while taking\nadvantage of continuous integration.\n\nMost of these utilities only exist here, one came from a chat on Reddit and\nI don't know where one of them came from.\n\nFour of them are written in Bash, the rest use Python 3.  They have been tested\non Mac OS/X (Darwin) and on Ubuntu, and will likely work on any Unix-like\noperating system.\n\nHow to install\n==============\n\nUse `pip <https://pypi.org/project/pip/>`_:\n\n.. code-block:: bash\n\n    pip3 install gitz\n\nOr simply download\n`this directory <https://github.com/rec/gitz/zipball/master/>`_\nand make sure it's in your shell's ``PATH`` - gitz has no\nexternal dependencies.\n\n\nGetting help\n============\n\nThis page contains a summary and a link to a manual page for each command.  From\nthe terminal, use ``-h`` flag like this: ``git new -h`` or use ``man`` like\nthis: ``man git-new``.\n\n\nWhen to use gitz\n=================\n\n1. At the start of a session\n\n   - ``git new`` safely creates fresh branches from upstream\n\n   - ``git update`` for each branch, rebases from upstream and force-pushes\n\n2. During development\n\n   - ``git st`` is a more compact and prettier ``git status``\n\n   - ``git when`` shows you when documents were last changed\n\n3. During rapid development\n\n   - ``git infer`` commits files with an automatically generated message -\n     great for committing tiny changes for later rebasing down\n\n4. While cleaning up a branch for review\n\n   - ``git permute`` permutes, squashes or removes commits in the current branch\n\n   - ``git split`` split one or more commits, perhaps with the staging area,\n     into many small individual commits, one per file\n\n5. During repository maintenance\n\n   - ``git rotate`` rotates through all branches\n\n   - ``git copy``, ``git delete``,  and ``git rename`` work on both local\n     and upstream branches\n\n6. Working with continuous integration\n\n   - ``git stripe`` pushes a sequence of commits to individual remote branches\n     where CI can find and test them\n\nThe movie\n==========\n\n.. figure:: https://asciinema.org/a/XwakAaMsMzKg4hIAJa18iiNac.png\n    :target: https://asciinema.org/a/XwakAaMsMzKg4hIAJa18iiNac?autoplay=1&theme=solarized-light&loop=1\n    :align: center\n    :alt: The whole gitz movie\n    :width: 430\n    :height: 402\n\nThe gitz commands\n-----------------\n\n\nSafe commands\n=============\n\nInformational commands that don't change your repository\n\n`git gitz <doc/git-gitz.rst>`_\n  Print information about the gitz git commands\n\n`git go <doc/git-go.rst>`_\n  Open a browser page for the current repo\n\n`git infer <doc/git-infer.rst>`_\n  Commit changes with an automatically generated message\n  \n  (from https://github.com/moondewio/git-infer)\n\n`git multi-pick <doc/git-multi-pick.rst>`_\n  Cherry-pick multiple commits, with an optional squash\n\n`git new <doc/git-new.rst>`_\n  Create and push new branches\n\n`git rot <doc/git-rot.rst>`_\n  Rotate through branches in a Git repository\n\n`git st <doc/git-st.rst>`_\n  Colorful, compact git status\n\n`git stripe <doc/git-stripe.rst>`_\n  Push a sequence of commit IDs to a remote repository\n\n`git when <doc/git-when.rst>`_\n  For each file, show the most recent commit that changed it.\n  \n  Dotfiles are ignored by default.\n\nDangerous commands that delete, rename or overwrite branches\n============================================================\n\n`git copy <doc/git-copy.rst>`_\n  Copy a git branch locally and remotely\n\n`git delete <doc/git-delete.rst>`_\n  Delete one or more branches locally and remotely\n\n`git rename <doc/git-rename.rst>`_\n  Rename a git branch locally and remotely\n\nBy default, the branches ``develop`` and ``master`` are protected -\nthey are not allowed to be copied to, renamed, or deleted.\n\nYou can configure this in three ways:\n\n- setting the ``--all/-a`` flag ignore protected branches entirely\n\n- setting the environment variable ``GITZ_PROTECTED_BRANCHES`` overrides these\n  defaults\n\n- setting a value for the keys ``PROTECTED_BRANCHES`` in the file\n  .gitz.json in the top directory of your Git project has the same effect\n\nDangerous commands that rewrite history\n=======================================\n\nSlice, dice, shuffle and split your commits.\n\nThese commands are not intended for use on a shared or production branch, but\ncan significantly speed up rapid development on private branches.\n\n`git adjust <doc/git-adjust.rst>`_\n  Amend any commit, not just the last\n\n`git permute <doc/git-permute.rst>`_\n  Reorder and delete commits in the current branch\n\n`git split <doc/git-split.rst>`_\n  Split a range of commits into many single-file commits\n\n`git update <doc/git-update.rst>`_\n  Update branches from a reference branch\n",
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'scripts': scripts,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
