# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hwave', 'hwave.qlmsio', 'hwave.solver']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.14,<2.0',
 'requests>=2.28.1,<3.0.0',
 'scipy>=1.7,<2.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['hwave = hwave.qlms:main']}

setup_kwargs = {
    'name': 'hwave',
    'version': '0.1',
    'description': 'UHF',
    'long_description': '# H-wave\n\nH-wave is a program for performing unrestricted Hartree-Fock (UHF) approximation\nfor itinerant electron systems.\nThe UHF method approximates two-body interaction terms into one-body ones by\ntaking account of the fluctuations up to the first order. The wave functions\nand energies are determined self-consistently by an iterative method.\nH-wave treats two types of UHF approximation: one is real-space and the other is\nwavenumber-space UHF methods using translational symmetry. In the wavenumber space\nUHF method, the input file defining the one-body and two-body interactions is\nbased on the Wannier90 format, and the program can be smoothly connected to\nthe softwares for deriving effective models from first-principles calculations.\n\n## Methods\n\nHartree-Fock approximation\n\n## Target models\n\nHubbard model, multi-orbital Hubbard model\n\n## Available physical quantities\n\nground-state energy, free energy, etc.\n\n## Requirement\n\nPython3 with numpy, scipy, and other library packages\n\n## Install\n\n- From PyPI\n\n``` bash\npython3 -m pip install hwave\n```\n\n- From source (if you modify the program)\n\n``` bash\npython3 -m pip install DIRECTORY_OF_THE_REPOSITORY\n```\n\n## License\n\nThe distribution of the program package and the source codes for H-wave follow\nGNU General Public License version 3\n([GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html)).\n\nCopyright (c) <2022-> The University of Tokyo. All rights reserved.\n\nThis software was developed with the support of\n"Project for Advancement of Software Usability in Materials Science"\nof The Institute for Solid State Physics, The University of Tokyo.\n\n## Official page\n\n- [H-wave project site](https://www.pasums.issp.u-tokyo.ac.jp/h-wave/en)\n- [Software repository](https://github.com/issp-center-dev/H-wave)\n- [User Manual](https://www.pasums.issp.u-tokyo.ac.jp/h-wave/en/doc/manual)\n\n## Authors\n\nKazuyoshi Yoshimi,\nYuichi Motoyama,\nTatsumi Aoyama,\nKota Ido,\nTakahiro Misawa,\nTaiki Kawamura\nAkito Kobayashi,\nTakeo Kato\n',
    'author': 'H-Wave developers',
    'author_email': 'hwave-dev@issp.u-tokyo.ac.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/issp-center-dev/H-Wave',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
