# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fractalpy', 'fractalpy.cli', 'fractalpy.cli.commands', 'fractalpy.fractals']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'imageio>=2.22.4,<3.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'mpire>=2.6.0,<3.0.0',
 'numba>=0.56.4,<0.57.0',
 'numpy>=1.23.5,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0']

entry_points = \
{'console_scripts': ['fractalpy = fractalpy.cli.cli_main:main']}

setup_kwargs = {
    'name': 'fractalpy',
    'version': '0.1.0',
    'description': 'A high performance framework for fractal image and video generation',
    'long_description': '# FractalPy\n![pypi](https://img.shields.io/pypi/v/FractalPy)\n![tag](https://img.shields.io/github/v/tag/Fergus-OH/FractalPy)\n![python_version](https://img.shields.io/pypi/pyversions/FractalPy)\n![licence](https://img.shields.io/github/license/Fergus-OH/FractalPy)\n![checks](https://img.shields.io/github/checks-status/Fergus-OH/FractalPy/main)\n[![codecov](https://codecov.io/gh/Fergus-OH/FractalPy/branch/main/graph/badge.svg?token=XWYUNL7XIE)](https://codecov.io/gh/Fergus-OH/FractalPy)\n\n<p align="center">\n  <img src= "https://raw.githubusercontent.com/Fergus-OH/mandelbrot-julia-sets/numba/assets/Mandelbrot_4320pts_1000threshold.png" width="800">\n</p>\n\nConsider the recurrence relation $z_{n+1} = z_n^2 + c$ where $c$ is a complex number.\nThe Mandelbrot set is a fractal, defined by the set of complex numbers $c$ for which this recurrence relation, with initial value $z_0 = 0$, does not diverge.\nAnother interesting type of set, which are related to the Mandelbrot set, are Julia sets and are defined for a specific complex number $c$.\nTo keep things brief, we will just establish the definition of a filled-in Julia set and do so in the following way:\nThe filled-in Julia set of a complex number $c$ is the set of initial values $z_0$ for which the previously mentioned recurrence relation does not diverge.\nNot every filled-in Julia set is a fractal, but for almost all complex numbers $c$, they are.\nThis project contains an implementation to generate images and videos relating to the Mandelbrot set and Julia sets.\n\n[//]: # (<img src="https://raw.githubusercontent.com/Fergus-OH/FractalPy/numba/assets/zoom_&#40;-1,186592,-0,1901211&#41;)\n\n[//]: # (_1000thresh_360pts_60frames_15fps.gif" width="400">)\n\n<p align="center">\n  <img src="https://raw.githubusercontent.com/Fergus-OH/FractalPy/numba/assets/zoom_(-1,186592,-0,1901211)_1000thresh_360pts_60frames_15fps-min.gif" width="400">\n  <img src="https://raw.githubusercontent.com/Fergus-OH/FractalPy/numba/assets/spin_(-0,79+0,15j)_1000thresh_360pts_110frames_30fps.gif" width="400">\n</p>\n\n\n\n\n[//]: # (<img src="https://raw.githubusercontent.com/Fergus-OH/mandelbrot-julia-sets/numba/assets/zoom_&#40;10004407000,-0,7436439059192348,-0,131825896951&#41;_5000thresh_480pts_300frames_30fps.gif" width="500">)\n[//]: # (<img src="https://raw.githubusercontent.com/Fergus-OH/mandelbrot-julia-sets/numba/assets/julia_spin2.gif" width="500">)\n  \n\n\n## Installation\nBefore installing the `FractalPy` package, it is recommended to create and activate a virtual environment with `python 3.10`.\nThis can be done with conda by running the following commands in a terminal\n```\n$ conda create --name fractal python==3.10\n```\n\n```\n$ conda activate fractal\n```\nNow the package and it\'s dependencies can be installed in the virtual environment, `fractal`, using pip\n```\n$ pip install fractalpy\n```\n\nFor an editable installation from the source, first clone the repository and install with the following\n```\n$ conda activate fractal\n$ pip install -e .\n```\n\n## Usage\nThere are two ways of using `FractalPy`.\nThe package can be imported to a python script with\n\n```python\nimport fractalpy as frac\n\n# Plot the Mandelbrot set\nfrac.Mandelbrot().plot()\n\n# Plot the Julia set\nfrac.Julia().plot()\n```\n\nThe package also offers a command line interface that can be immediately accessed in the terminal with\n```\nfractalpy --help\n```\n\nFor example, we can create a gif of zooming into the mandelbrot set with the following command:\n```\nfractalpy mandelbrot zoom\n```\n\nIf FFmpeg is installed and accessible via the $PATH environment variable, then `FractalPy` can also generate videos, for example\n```\nfractalpy mandelbrot zoom --extension mp4\n```\n\n`FractalPy` makes use of multiprocessing to generate multiple frames simultaneously and also performs the computationally expensive calculations in parallel with `jit`, making it an extremely fast.\n<!-- ```\nFractal().\n```\n\n\nA notebook with demos can be found [here](https://nbviewer.org/github/Fergus-OH/mandelbrot-julia-sets/blob/numba/demos.ipynb)\n\n<a href="https://nbviewer.org/github/Fergus-OH/mandelbrot-julia-sets/blob/numba/demos.ipynb"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="Render nbviewer" /></a> -->',
    'author': "Fergus O'Hanlon",
    'author_email': 'fergusohanlon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Fergus-OH/FractalPy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
