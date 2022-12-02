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

import numpy as np
"""
Moreau-Broto autocorrelation descriptors
"""
def calmoreaubrotodescriptors(G, mass, charge):
    n = 20
    intervalsize = 1.0
    lagL = np.array([i for i in range(0,n)]).astype(float)*intervalsize
    lagU = lagL+intervalsize
    nA = len(G)

    ATS = {}
    for kkk in range(len(lagL)):
        tempm = 0.0
        tempc = 0.0
        for i in range(nA):
            for j in range(nA):  
                if G[i,j] >= lagL[kkk] and G[i,j] < lagU[kkk]:
                    tempm = tempm + mass[i]*mass[j]
                    tempc = tempc + charge[i]*charge[j]
                else:
                    tempm = tempm + 0.0
                    tempc = tempc + 0.0
                    
        ATS['ATSm'+str(kkk+1)] = np.log(tempm/2+1)
        ATS['ATSc'+str(kkk+1)] = np.log(tempc/2+1)
    return ATS