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
Unweighted WHIM descriptors
"""
def calwhimdescriptorsunweighted(xyz):
    nA, _ = xyz.shape   
    weight = np.matrix(np.eye(nA))
    
    xyzNew = xyz-np.mean(xyz,axis=0)
    temp = xyzNew.T*weight*xyzNew/sum(np.diag(weight))
    u,s,v = np.linalg.svd(temp)
    
    L1 = s[0] 
    L2 = s[1]
    L3 = s[2]
    T = sum(s)
    A = s[0]*s[1] + s[0]*s[2] + s[1]*s[2]    
    V = A + T + s[0]*s[1]*s[2]
    P1 = s[0] / (s[0] + s[1] + s[2])
    P2 = s[1] / (s[0] + s[1] + s[2])
    P3 = s[2] / (s[0] + s[1] + s[2])
    
    temp = 0.0
    for i in s:
        temp = temp + abs(i/sum(s) - 1/3.0)    
    K = 3.0/4*temp
    
    E1 = np.power(s[0],2)*nA/sum(np.power(xyzNew*u[:,0],4)).item()
    E2 = np.power(s[1],2)*nA/sum(np.power(xyzNew*u[:,1],4)).item()
    E3 = np.power(s[2],2)*nA/sum(np.power(xyzNew*u[:,2],4)).item()
    D = E1 + E2 + E3
    return (L1,L2,L3,T,A,V,P1,P2,P3,K,E1,E2,E3,D)

"""
Weighted WHIM descriptors
"""
def calwhimdescriptorsweighted(xyz,atomproperty):
    nA, _ = xyz.shape   
    weight = np.matrix(np.diag(atomproperty))
    
    xyzNew = xyz-np.mean(xyz,axis=0)
    temp = xyzNew.T*weight*xyzNew/sum(np.diag(weight))
    u,s,v = np.linalg.svd(temp)
    
    L1 = s[0] 
    L2 = s[1]
    L3 = s[2]
    T = sum(s)
    A = s[0]*s[1] + s[0]*s[2] + s[1]*s[2]    
    V = A + T + s[0]*s[1]*s[2]
    P1 = s[0] / (s[0] + s[1] + s[2])
    P2 = s[1] / (s[0] + s[1] + s[2])
    P3 = s[2] / (s[0] + s[1] + s[2])
    
    temp = 0.0
    for i in s:
        temp = temp + abs(i/sum(s) - 1/3.0)    
    K = 3.0/4*temp
    
    E1 = np.power(s[0],2)*nA/sum(np.power(xyzNew*u[:,0],4)).item()
    E2 = np.power(s[1],2)*nA/sum(np.power(xyzNew*u[:,1],4)).item()
    E3 = np.power(s[2],2)*nA/sum(np.power(xyzNew*u[:,2],4)).item()
    D = E1 + E2 + E3
    return (L1,L2,L3,T,A,V,P1,P2,P3,K,E1,E2,E3,D)

def calwhimdescriptors(xyz,mass,charge):
    WHIM = {}
    L1,L2,L3,T,A,V,P1,P2,P3,K,E1,E2,E3,D = calwhimdescriptorsunweighted(xyz)
    WHIM['L1u'] = L1
    WHIM['L2u'] = L2
    WHIM['L3u'] = L3
    WHIM['Tu'] = T
    WHIM['Au'] = A
    WHIM['Vu'] = V
    WHIM['P1u'] = P1
    WHIM['P2u'] = P2
    WHIM['P3u'] = P3
    WHIM['Ku'] = K
    WHIM['E1u'] = E1
    WHIM['E2u'] = E2
    WHIM['E3u'] = E3
    WHIM['Du'] = D
     
    L1,L2,L3,T,A,V,P1,P2,P3,K,E1,E2,E3,D = calwhimdescriptorsweighted(xyz,mass)
    WHIM['L1m'] = L1
    WHIM['L2m'] = L2
    WHIM['L3m'] = L3
    WHIM['Tm'] = T
    WHIM['Am'] = A
    WHIM['Vm'] = V
    WHIM['P1m'] = P1
    WHIM['P2m'] = P2
    WHIM['P3m'] = P3
    WHIM['Km'] = K
    WHIM['E1m'] = E1
    WHIM['E2m'] = E2
    WHIM['E3m'] = E3
    WHIM['Dm'] = D

    L1,L2,L3,T,A,V,P1,P2,P3,K,E1,E2,E3,D = calwhimdescriptorsweighted(xyz,charge)
    WHIM['L1c'] = L1
    WHIM['L2c'] = L2
    WHIM['L3c'] = L3
    WHIM['Tc'] = T
    WHIM['Ac'] = A
    WHIM['Vc'] = V
    WHIM['P1c'] = P1
    WHIM['P2c'] = P2
    WHIM['P3c'] = P3
    WHIM['Kc'] = K
    WHIM['E1c'] = E1
    WHIM['E2c'] = E2
    WHIM['E3c'] = E3
    WHIM['Dc'] = D

    return WHIM