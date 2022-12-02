import os

from pathlib import Path
from setuptools import find_packages, setup

import vEMreg



def AllFiles():
	files = ['FiReTiTiLiB.jar', 'lib/*.jar']
	for file_path in Path('./vEMreg/').glob('**/*.py'):
		files.append(str(file_path))
	return files



setup(
	name=vEMreg.__name__,
	packages=find_packages(),
	version=vEMreg.__version__,
	author="Guillaume THIBAULT",
	author_email="thibaulg@ohsu.edu",
	maintainer="Guillaume THIBAULT",
	maintainer_email="thibaulg@ohsu.edu",
	url="https://www.thibault.biz/Research/VolumeEM/vEMreg/vEMreg.html",
	download_url="https://www.thibault.biz/Doc/vEMreg/vEMreg-" + vEMreg.__version__ + ".tar.gz",
	license="MIT",
	plateforms='ALL',
	package_data={'vEMreg': AllFiles()},
	keywords=["Registration", "Alignment", "Electron Microscopy", "Volume EM", "vEM", "FIB-SEM",
			"Focused Ion Beam Scanning Electron Microscop"],
	classifiers=["Development Status :: 4 - Beta",# "Development Status :: 5 - Production/Stable",
					"Environment :: Console",
					"Environment :: Other Environment",
					"Intended Audience :: Developers",
					"Intended Audience :: Healthcare Industry",
					"Intended Audience :: Science/Research",
					"License :: OSI Approved :: MIT License",
					"Operating System :: OS Independent",
					"Programming Language :: Python :: 3",
					"Programming Language :: Python :: 3.8",
					"Programming Language :: Python :: 3.9",
					"Topic :: Scientific/Engineering",
					"Topic :: Scientific/Engineering :: Bio-Informatics",
					"Topic :: Scientific/Engineering :: Image Processing"],
	#install_requires=["FiReTiTiPyLib>=1.5.2"],
	python_requires=">=3.8,<=3.11",
	entry_points={'console_scripts': ['vEMreg=vEMreg.vEMreg:Register']},
	description="Volume Electron Microscopy REGistration (vEMreg)",
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
	)
