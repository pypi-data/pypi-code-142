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

import os
from rdkit import Chem

"""
This script take coordinates of atoms, masses of atoms, bonds between atoms
in a molecule and write a temperory *.mol file for detemining adjacency and
distance matrices

coordinates = x, y, z coordinates of atoms in a molecule
masses = mass of atoms in a molecule
bonds = ids of atoms forming bonds in a molecules
""" 
def lammpsdata2mol(whichmolcule, coordinates, masses, bonds):
    natoms = len(coordinates)
    nbonds = len(bonds)
    molfilename = 'molID' + str(whichmolcule) + '_numAtoms' + str(natoms) + '_numBonds' + str(len(bonds)) + '.mol'

    first_line = 'This is a mol file of the molcules whose molID = ' + str(whichmolcule)
    second_line = 'This is created temporarily to only obtain adjacency and distance matrices of the molecule'
    third_line = ' '
    
    
    # Check whether the specified path exists or not
    path = os.getcwd() + '/temp/'
    isExist = os.path.exists(path) 
    
    # Create a new temp directory because it does not exist 
    if not isExist: 
        os.makedirs(path)
              

    #####################################     V2000     #####################################
    if natoms <= 999: 
        
        countsblock_line  = [natoms, nbonds, 0, 0, 0, 0, 0, 0, 0, '0999', 'V2000']
        k = countsblock_line
        
        atomtable = []
        for i in range(natoms):
            amass = masses[i]
            x = coordinates[i,0]
            y = coordinates[i,1]
            z = coordinates[i,2]
            
            if amass > 1.5:
                symbol_elemnt = "C"
            else:
                symbol_elemnt = "H"
        
            toapp = [x, y, z, symbol_elemnt , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            atomtable.append(toapp)
        
        bondtable = []
        btype = 1
        for i in range(nbonds):     
            abond = [bonds[i,0], bonds[i,1], btype, 0, 0, 0, 0]
            bondtable.append(abond)
            
        
        with open(path+molfilename, 'w') as f:
            f.write(first_line + '\n')
            f.write(second_line + '\n')
            f.write(third_line + '\n')
            
            #counts line:
            if natoms <= 99:
                newline = '{:>3} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>5} {:>5}'.format(\
                    k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10])
            else:
                newline = '{:>3}{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>5} {:>5}'.format(\
                    k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8], k[9], k[10])
            f.write(newline + '\n')
            
            #print atom block
            for i in atomtable:
                newline = '{:>10.4f} {:>9.4f} {:>9.4f} {:>1} {:>3} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(\
                      i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15])
                f.write(newline + '\n')
            
            #print bond block
            for i in bondtable:
                if natoms <= 99:
                    newline = '{:>3} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(\
                            i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                else:
                    newline = '{:>3}{:>3} {:>2} {:>2} {:>2} {:>2} {:>2}'.format(\
                            i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                f.write(newline + '\n')

            f.write('M  END')          


    #####################################     V2000     #####################################
    elif natoms > 999: # V3000
        
        atomtable = []
        for i in range(natoms):
            amass = masses[i]
            x = coordinates[i,0]
            y = coordinates[i,1]
            z = coordinates[i,2]
            
            if amass > 1.5:
                symbol_elemnt = "C"
            else:
                symbol_elemnt = "H"

            toapp = ['M', 'V30', i+1, symbol_elemnt, x, y, z, 0, 'CHG=0']
            atomtable.append(toapp)
        
        with open(path+molfilename, 'w') as f:
            f.write(first_line + '\n')
            f.write(second_line + '\n')
            f.write(third_line + '\n')
            f.write('  0  0  0  0  0  0  0  0  0  0999 V3000\n')
            f.write('M  V30 BEGIN CTAB\n')
            f.write('M  V30 COUNTS ' + str(natoms) + ' ' + str(nbonds) + ' 0 0 0\n')
            f.write('M  V30 BEGIN ATOM\n')        
            
            #print atom block
            for i in atomtable:
                newline = '{:>1}  {:>2} {:>1} {:>1} {:>13.4f} {:>11.4f} {:>11.4f}'.format(\
                      i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                f.write(newline + ' 0 CHG=0\n')
            f.write('M  V30 END ATOM\n')
            f.write('M  V30 BEGIN BOND\n')
            
            # print bond block
            btype = 1
            for i in range(nbonds):
                f.write('M  V30 ' + str(i+1) + ' ' + str(btype) + ' ' + str(bonds[i,0]) + ' ' + str(bonds[i,1]) + ' CFG=0\n')
            f.write('M  V30 END BOND\n')
            f.write('M  V30 END CTAB\n')    
            f.write('M  END\n')
    return (path, molfilename)

"""
Get adjacency and distnace matrices from rdkit
"""
def getadjANDdismatrices(atomSection, eachMolsIdx, eachMolsBonds, eachMolsMass):
    eachMolsAdjMat = {}
    eachMolsDisMat = {}
    numMols = len(eachMolsIdx)
    for i in range(numMols):
        idxAtoms = eachMolsIdx[i]
        coordinates = atomSection[idxAtoms,4:]
        bonds = eachMolsBonds[i]
        masses = eachMolsMass[i]
        path, molfilename = lammpsdata2mol(i, coordinates, masses, bonds)
        
        mol = Chem.MolFromMolFile((path + '/'+ molfilename))
        eachMolsAdjMat[i] = Chem.GetAdjacencyMatrix(mol)   # Get 2D adjaceny matrix using rdkit
        eachMolsDisMat[i] = Chem.GetDistanceMatrix(mol)    # Get 2D distance matrix using rdkit
    return (eachMolsAdjMat, eachMolsDisMat)