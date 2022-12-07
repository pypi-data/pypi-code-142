# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tw_source_finder', 'tw_source_finder.scripts']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=5.1,<6.0',
 'reproject>=0.9.1,<0.10.0',
 'scikit-image>=0.19.3,<0.20.0',
 'shapely>=1.8.5.post1,<2.0.0']

entry_points = \
{'console_scripts': ['tw-source-list = '
                     'tw_source_finder.scripts.get_simple_source_list:main']}

setup_kwargs = {
    'name': 'tw-source-finder',
    'version': '1.0.0',
    'description': 'super-fast source finder routine using polygon based approach',
    'long_description': "tw-source-finder\n================\n\n[![Documentation Status](https://readthedocs.org/projects/tw-source-finder/badge/?version=latest)](https://tw-source-finder.readthedocs.io/en/latest/?badge=latest)\n\nThis package leverages a parallelization boiler-plate code to provide a super fast source finder routine which deletes background sources using a polygon based approach.\n\nWatch the video on [YouTube](https://www.youtube.com/watch?v=cO5TYy396xU) for detailed instructions on how to use the data analysis scripts. Hopefully, it will not put you to sleep! More detailed written instructions may follow.\n\nFeatures\n--------\nThere are two main scripts in the package, viz: `get_morphology_images` and `get_galaxy_parameters`.\n\n**get_morphology_images**\n\nUses morphological erosion and dilation to remove background sources from a radio astronomy image. It extends the technique described in [Rudnick, 2002](https://iopscience.iop.org/article/10.1086/342499/pdf).\n\nThe process can be described through the following equations:\n\n```\no = original image\n\nd = output from erosion/dilation\n\nt = white TopHat, which should show only 'compact' structures\n\nt = o - d\n\nm = mask derived from a comparison where t > some signal m * t = m * (o - d)\n\no_d = output diffuse image\n\n=o - m * t\n\n=o - (m * o - m * d)\n\n=o - m * o + (m * d)\n\nm*d would add the masked dilated image to the 'diffuse' image and we do not want to do that so we ignore it to get\n\no_d = o - m * o and\n\no_c = image of compact objects = m * o\n\nso the original image equates to o_d + o_c\n```\n\nWe may want to judiciously add selected components of `o_c` to `o_d` to get a final `o*`. We select the components of `o_c` we wish to add by masking their defining polygons to get a mask `m_c`\n\n$$o* = o_d + m_c * o_c$$\n\n**get_galaxy_parameters**\n\nIntegrates the signal contained within specified polygon areas of a radio astronomy image to derive integrated flux densities and other parameters of a radio source.\n\n\nRequirements\n------------\n\nThe code has been tested with python 3.8 on Ubuntu 20.04. See `pyproject.toml` or `requirements.txt` for package dependencies.\n\nInstallation\n------------\n\nInstall from source\n\n```bash\n$ pip install .\n```\n\nUse the routine\n\n```bash\n$ tw-source-list -f xyz.fits -t 6.5\n```\n",
    'author': 'Tony Willis',
    'author_email': 'tony.willis.research@gmail.com',
    'maintainer': 'Tony Willis',
    'maintainer_email': 'tony.willis.research@gmail.com',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
