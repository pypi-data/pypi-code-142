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
3D Geary autocorrelation indices
"""
def calgearyindices(G, mass, charge):
    n = 20
    intervalsize = 1.0
    lagL = np.array([i for i in range(0,n)]).astype(float)*intervalsize
    lagU = lagL+intervalsize
    nA = len(G)
    
    avgmass = sum(mass)/nA
    temppm = sum(np.square(mass-avgmass))
    
    avgcharge = sum(charge)/nA
    temppc = sum(np.square(charge-avgcharge))
    
    GATS = {}
    for kkk in range(len(lagL)):
        tempm = 0.0
        tempc = 0.0
        index = 0
        for i in range(nA):
            for j in range(nA):  
                if G[i,j] >= lagL[kkk] and G[i,j] < lagU[kkk]:
                    tempm = tempm + np.square(mass[i]-mass[j])
                    tempc = tempc + np.square(charge[i]*charge[j])
                    index = index + 1
                else:
                    tempm = tempm + 0.0
                    tempc = tempc + 0.0
                    
                
        if temppm == 0 or index == 0:
            GATS['GATSm'+str(kkk+1)] = 0
        else:
            GATS['GATSm'+str(kkk+1)] = (tempm/index/2)/(temppm/(nA-1))
            
        if temppc == 0 or index == 0:
            GATS['GATSc'+str(kkk+1)] = 0
        else:
            GATS['GATSc'+str(kkk+1)] = (tempc/index/2)/(temppc/(nA-1))
        
    return GATS