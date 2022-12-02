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
3D RDF descriptors
"""
def calrdfdescriptors(G, mass, charge):
    nA = len(G)
    beta = 100
    n = 30
    R = np.array([i for i in range(2,n+2)]).astype(float)*0.5 # R in RDF equation
    mC = 12.011
    RDF = {}
    for kkk, Ri in enumerate(R):        
        tempu = 0.0
        tempm = 0.0
        tempc = 0.0
        for j in range(nA-1):
            for k in range(j+1,nA):
                tempu = tempu + np.exp(-beta*np.power(Ri-G[j,k],2))
                tempm = tempm + mass[j]*mass[k]*np.exp(-beta*np.power(Ri-G[j,k],2))
                tempc = tempc + charge[j]*charge[k]*np.exp(-beta*np.power(Ri-G[j,k],2))
        RDF['RDF'+'u'+str(kkk+1)] = tempu
        RDF['RDF'+'c'+str(kkk+1)] = tempc
        RDF['RDF'+'m'+str(kkk+1)] = tempm/(mC**2)
    return RDF