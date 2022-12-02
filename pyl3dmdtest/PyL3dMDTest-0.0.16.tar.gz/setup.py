# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:39:02 2022

@author: Pawan Panwar, Quanpeng Yang, Ashlie Martini


PyL3dMD: Python LAMMPS 3D Molecular Dynamics/Descriptors
Copyright (C) 2022  Pawan Panwar, Quanpeng Yang, Ashlie Martini

This file is part of PyL3dMD.

PyL3dMD is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published 
by the Free Software Foundation, either version 3 of the License, 
or (at your option) any later version.

PyL3dMD is distributed in the hope that it will be useful, but 
WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
 along with PyL3dMD. If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

VERSION = '0.0.16' 
DESCRIPTION = 'Python LAMMPS 3-Dimensional Molecular Dynamics/Descriptors'
LONG_DESCRIPTION = 'PyL3dMD stands for Python LAMMPS 3-Dimensional Molecular Dynamics/Descriptors, a python package for 3D descriptors calculation'

# setup
setup(
       # name
        name="PyL3dMDTest", 
        version=VERSION,
        author="Pawan Panwar, Quanpeng Yang, Ashlie Martini",
        author_email="samtari@163.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        # install_requires=["numpy","pandas","rdkit","os", "time"], # add any additional packages that 
        install_requires=[], # add any additional packages that 
        # Packages needed，e.g.,：'caer'
        
        keywords=['Python', 'LAMMPS', 'Molecular Dynamics Simulations', 'Descriptors', 'Machine Learning', 'MD Simulations', '3-Dimensional'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)