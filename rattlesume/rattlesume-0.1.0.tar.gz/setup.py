# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rattlesume']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0', 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'rattlesume',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Rattlesume\n\nA tool for building resumes by combining markdown snippets into a single\ndocument using `yaml` definitions, then transformed into a PDF `pandoc`. Allows\ndevelopers to store their resumes in git, and present them in a common format.\nDifferent yaml definitions can be used to craft bespoke resumes from a collection\nof markdown snippets.\n\n# Usage\n\n## Snippets\n\nTo start, create a `content` directory with a subdirectory\nto organize a class of snippets. **The name of the\nsubdirectory will be the same as the header in the final resume.**\n\n```\n\uf115 example/content/\n├── \uf115 experience/\n│  └── \uf48a FooBar.md\n└── \uf115 projects/\n   └── \uf48a Rattlusume.md\n```\n\nEach of these markdown files are called \'snippets\'. They are\ntypically a short summary & include relevant information such as\ndates, job titles, etc.\n\n```markdown\n---\nfilename: FooBar.md\n---\n# FooBar Inc.\n## Sr. Foobar Enigneer, March 5th, 2015 - Present\n\nResponsible for announcing the zero-modulate of the counting numbers greater than\nzero with respect to three and five. Saved FooBar Inc. $15 annually by implementing\nan `O(n)` solution.\n```\n\n> Snippets can contain an optional slug at the very top, denoted by `---`.\n> This slug must be valid yaml. Currently, it is parsed, but not used.\n\n\n## Definitions\n\nEach unique resume has a corresponding definition file.\nThere are currently two required top-level values. `header`,\nand `resume`.\n\n### `header`\n\nThe format of this value is still in flux.\n\n### `resume`\n\nThe `resume` section has arbitrary sub-key corresponding to the\nnames of the subdirectories the snippets are located in.\n\nEach of these sub-keys take a list of values, which are ether file names\nor special values.\n\nFor example, the aforementioned \'FooBar.md\' could be defined as follows:\n\n```yaml\nheader:\n  ...\n\nresume:\n  experience:\n    - "---"\n    - "FooBar.md"\n```\n\nThere is currently only one special value,\n`"---"`, which denotes a horizontal rule.\n',
    'author': 'Kelton Bassingthwaite',
    'author_email': 'keltonbassingthwaite@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
