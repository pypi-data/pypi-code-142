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
GETAWAY Descriptors - Geometry, topology, and atom-weights assembly (GETAWAY) descriptors
"""
H = np.array([[0.065,	0.031,	-0.036,	-0.07,	-0.036,	0.031,	0.057,	-0.063,	-0.123,	-0.063,	0.057,	0.148],
[0.031,	0.075,	0.042,	-0.034,	-0.077,	-0.044,	0.134,	0.076,	-0.059,	-0.136,	-0.079,	0.071],
[-0.036,	0.042,	0.079,	0.039,	-0.039,	-0.077,	0.075,	0.141,	0.068,	-0.071,	-0.138,	-0.082],
[-0.07,	-0.034,	0.039,	0.075,	0.039,	-0.034,	-0.061,	0.067,	0.132,	0.067,	-0.061,	-0.159],
[-0.036,	-0.077,	-0.039,	0.039,	0.079,	0.042,	-0.138,	-0.071,	0.068,	0.141,	0.075,	-0.082],
[0.031,	-0.044,	-0.077,	-0.034,	0.042,	0.075,	-0.079,	-0.136,	-0.059,	0.076,	0.134,	0.071],
[0.057,	0.134,	0.075,	-0.061,	-0.138,	-0.079,	0.242,	0.135,	-0.108,	-0.246,	-0.141,	0.13],
[-0.063,	0.076,	0.141,	0.067,	-0.071,	-0.136,	0.135,	0.25,	0.118,	-0.129,	-0.246,	-0.143],
[-0.123,	-0.059,	0.068,	0.132,	0.068,	-0.059,	-0.108,	0.118,	0.232,	0.118,	-0.108,	-0.28],
[-0.063,	-0.136,	-0.071,	0.067,	0.141,	0.076,	-0.246,	-0.129,	0.118,	0.25,	0.135,	-0.143],
[0.057,	-0.079,	-0.138,	-0.061,	0.075,	0.134,	-0.141,	-0.246,	-0.108,	0.135,	0.242,	0.13],
[0.148,	0.071,	-0.082,	-0.159,	-0.082,	0.071,	0.13,	-0.143,	-0.28,	-0.143,	0.13,	0.337]])

H1 = np.array([[0.056,	0.004,	-0.076,	0.13,	0.017,	0.037,	-0.114,	-0.11,	0.056],
[0.004,	0.054,	0.009,	0.04,	-0.096,	0.134,	0.049,	-0.071,	-0.122],
[-0.076,	0.009,	0.109,	-0.171,	-0.048,	-0.018,	0.17,	0.135,	-0.109],
[0.13,	0.04,	-0.171,	0.321,	-0.017,	0.163,	-0.233,	-0.293,	0.059],
[0.017,	-0.096,	-0.048,	-0.017,	0.179,	-0.225,	-0.136,	0.082,	0.243],
[0.037,	0.134,	-0.018,	0.163,	-0.225,	0.347,	0.061,	-0.23,	-0.27],
[-0.114,	0.049,	0.17,	-0.233,	-0.136,	0.061,	0.291,	0.157,	-0.247],
[-0.11,	-0.071,	0.135,	-0.293,	0.082,	-0.23,	0.157,	0.292,	0.038],
[0.056,	-0.122,	-0.109,	0.059,	0.243,	-0.27,	-0.247,	0.038,	0.351]
])

R1 = np.array([[0,	0.037,	0.031,	0.108,	0.073,	0.064,	0.037,	0.046,	0.073],
[0.037,	0,	0.058,	0.054,	0.041,	0.124,	0.059,	0.059,	0.043],
[0.031,	0.058,	0,	0.052,	0.05,	0.091,	0.162,	0.162,	0.052],
[0.108,	0.054,	0.052,	0,	0.109,	0.125,	0.067,	0.077,	0.15],
[0.073,	0.041,	0.05,	0.109,	0,	0.074,	0.059,	0.091,	0.258],
[0.064,	0.124,	0.091,	0.125,	0.074,	0,	0.126,	0.102,	0.086],
[0.037,	0.059,	0.162,	0.067,	0.059,	0.126,	0,	0.157,	0.066],
[0.046,	0.059,	0.162,	0.077,	0.091,	0.102,	0.157,	0,	0.092],
[0.073,	0.043,	0.052,	0.15,	0.258,	0.086,	0.066,	0.092,	0],
])

# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

leverage = calleverage(H1)

onesMat = np.ones([len(M),len(M)])
onesMatWithZerosDiag = np.ones([len(M),len(M)])
np.fill_diagonal(onesMatWithZerosDiag,0.0)
R = (np.sqrt((onesMat*leverage)*np.transpose(onesMat*leverage))*onesMatWithZerosDiag) / (G*onesMat)


R = calinfluencedistancematrix(M, G, leverage)
from scipy.stats.mstats import gmean

# Geometric mean of the leverage magnitude
HGM = gmean(leverage)*100

# Row sum of influence distnace matrix
VSi = np.sum(R1, axis=1)

# Total information content on the leverage equality
A0 = len(massheavy) # number of non-hydrogen atoms
Ng = # number of atoms with the same leverage value
ITH = 


# Standardized information content on the leverage equality
ISH = 


# Mean information content on the leverage magnitude
HIC =

# Average row sum of the influence/distance matrix
RARS =

# R-connectivity index
RCON =

# R-matrix leading eigenvalue
REIG = np.max(np.linalg.eig(R)[0])


############### GETAWAY descriptors based on autocorrelation functions ######################
# HATS indexes

# HATS total index

# Hindexes 

# H total index

# R indexes

# R total index

# Maximal R indexes


# Maximal R total index
