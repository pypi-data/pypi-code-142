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

def getalldatafileinfo(datafilename):
    """
    idAtoms - ids of the atoms in the simulation box
    idMols - ids of the molecules in the simulation box
    atomTypes - atom types of all the atoms in the simulation box
    atomCharges - atom charges of all the atoms in the simulation box
    atomMasses - masses of all the atoms in the simulation box
    AtomList = atoms section from the LAMMPS data file [atomID moldID atomtype charge x y z]
    BondList = bonds section from the LAMMPS data file [bondID bondtype atom1ID atom2ID]
    AngleList = angles section from the LAMMPS data file [angleID angletype atom1ID atom2ID atom3ID]
    DihedralList = dihedrals section from the LAMMPS data file [dihedralID dihedralype atom1ID atom2ID atom3ID atom4ID]
    """
    
    atomSection, bondSection, angleSection, dihedralSection = readlammpsdataFile(datafilename)

    idAtoms = np.array(atomSection[:,0]).astype(int)        # ids of the atoms in the simulation box
    idMols = np.array(atomSection[:,1]).astype(int)         # ids of the molecules in the simulation box
    atomTypes = np.array(atomSection[:,2]).astype(int)      # atom type of all the atoms in the simulation box
    atomCharges = np.array(atomSection[:,3]).astype(float)  # atom charge of all the atoms in the simulation box
    atomMasses = getmass(datafilename,atomTypes)
    
    return (idAtoms, idMols, atomTypes, atomCharges, atomMasses, atomSection, bondSection, angleSection, dihedralSection)
    

def getmass(datafilename,atomTypes):
    """
    It returns a dictionary of the mass of each atom type
    """  
    atomTyesAndMasses = {}
    foundatomTyesAndMasses = False
    readingatomTyesAndMasses = True
    atomnum = 1
    datfile = open(datafilename)
    for i in range(0,4):
        datfile.readline()
    
    while foundatomTyesAndMasses == False:
        line = datfile.readline()
        line = line.split()
        
        if len(line) > 0:
            if line[0] == 'Masses':
                foundatomTyesAndMasses = True
                datfile.readline()  
    while readingatomTyesAndMasses == True:
        line = datfile.readline()
        line = line.split()
        if len(line) > 0:
            if int(line[0]) == atomnum:
                atomTyesAndMasses[int(line[0])] = float(line[1])
                atomnum += 1
            else:
                readingatomTyesAndMasses = False
        else:
            readingatomTyesAndMasses = False
    datfile.close()
    
    # loop over each atom type of atom or mass
    numAtoms = len(atomTypes)
    atomMasses = np.zeros(numAtoms)
    for i in atomTyesAndMasses:
        idx = findidxofmatchingelements(atomTypes, i)   # find the indices of a atom type
        atomMasses[idx] = atomTyesAndMasses[i]          # Assign mass to the atoms
        
    return atomMasses

def arragebymolecule(idAtoms, idMols, atomMasses, atomCharges, bondSection, angleSection, dihedralSection):
    """
    It stores number of atoms in each molecules in a list where index id molecule ID
    It stores ID of atoms, mass of atoms, charge of atoms in each molecules in dictonaries where key is molecule ID
    It stores bonds, angles, and dihedrals between atoms of each molecules in dictonaries where key is molecule ID
    """
    # num of molecules in the simulation box      
    numMols = max(idMols)   

    # Make dictonaries to store properties for each molecules separately
    eachMolsNumIdx = [] # stores number of atoms in each molecules
    eachMolsIdx = {}
    eachMolsMass = {}
    eachMolsCharge = {}
    for i in range(numMols):                            # Loop over each molecule
        idx = findidxofmatchingelements(idMols, i+1)    # find the indices of a molecules
        eachMolsNumIdx.append(len(idx))                 # Number of atoms in each molecules in the simulation box
        eachMolsIdx[i] = idx                            # Indices of each molecules
        eachMolsMass[i] = atomMasses[idx]               # Indices of each molecules
        eachMolsCharge[i] = atomCharges[idx]            # Indices of each molecules

    # Now organize bonds, angles, and dihedrals            
    connectivity2 = [] # connectivity between two atoms (i.e., bond)
    connectivity3 = [] # connectivity between three atoms (i.e., angle)
    connectivity4 = [] # connectivity between four atoms (i.e., dihedral)
    
    eachMolsBonds = {}
    eachMolsAngles = {}
    eachMolsDihedrals = {}
    j = 0
    for i in range(numMols):
        j = i+1
        # Get index of all bonds in a molecules
        idxBnd = np.where(np.isin(bondSection[:,2],idAtoms[idMols==j]))
        idxAng = np.where(np.isin(angleSection[:,2],idAtoms[idMols==j]))
        idxDih = np.where(np.isin(dihedralSection[:,2],idAtoms[idMols==j]))
        
        if j == 1:
            #Extract bonds
            connectivity2.append(bondSection[idxBnd,:]);
            connectivity3.append(angleSection[idxAng,:]);
            connectivity4.append(dihedralSection[idxDih,:]);
            
        elif j > 1:
            #Extract bonds
            connectivity2.append(bondSection[idxBnd,:]);
            connectivity3.append(angleSection[idxAng,:]);
            connectivity4.append(dihedralSection[idxDih,:]);
            
            # Correct bondID and atomIDs
            connectivity2[i][0,:,0] = connectivity2[i][0,:,0] - min(connectivity2[i][0,:,0]) + 1;
            connectivity2[i][0,:,2:] = connectivity2[i][0,:,2:] - connectivity2[i][0,:,2:].min() + 1;
            
            connectivity3[i][0,:,0] = connectivity3[i][0,:,0] - min(connectivity3[i][0,:,0]) + 1;
            connectivity3[i][0,:,2:] = connectivity3[i][0,:,2:] - connectivity3[i][0,:,2:].min() + 1;
            
            connectivity4[i][0,:,0] = connectivity4[i][0,:,0] - min(connectivity4[i][0,:,0]) + 1;
            connectivity4[i][0,:,2:] = connectivity4[i][0,:,2:] - connectivity4[i][0,:,2:].min() + 1;
            
        eachMolsBonds[i] = connectivity2[i][0,:,2:]
        eachMolsAngles[i] = connectivity3[i][0,:,2:]
        eachMolsDihedrals[i] = connectivity4[i][0,:,2:]
        
    return (eachMolsNumIdx,eachMolsIdx,eachMolsMass,eachMolsCharge,eachMolsBonds,eachMolsAngles,eachMolsDihedrals)

         
def readlammpsdataFile(datafilename):
    """
    Import data from a LAMMPS data file - AtomList, BondList, AngleList, DihedralList = readLAMMPSdataFile(datafilename)

    AtomList = atoms section from the LAMMPS data file [atomID moldID atomtype charge x y z]
    BondList = bonds section from the LAMMPS data file [bondID bondtype atom1ID atom2ID]
    AngleList = angles section from the LAMMPS data file [angleID angletype atom1ID atom2ID atom3ID]
    DihedralList = dihedrals section from the LAMMPS data file [dihedralID dihedralype atom1ID atom2ID atom3ID atom4ID]
    """ 
    f = open(datafilename, "r")
    
   # Initialization
    AtomList = []
    BondList = []
    AngleList = []
    DihedralList = []
    readStartAtoms = False
    readStartAtoms = False
    readStartBonds = False
    readStartAngles = False
    readStartDihedrals = False
    count = 0
    
    # Lopp over each line of LAMMPS data file
    for line in f:
        count += 1
        lineSplit = line.split()
        
        if len(lineSplit) > 0:
            if lineSplit[0] == "Atoms":
                readStartAtoms = True
            elif lineSplit[0] == "Bonds":
                readStartBonds = True
                readStartAtoms = False
            elif lineSplit[0] == "Angles":
                readStartAngles = True
                readStartBonds = False
            elif lineSplit[0] == "Dihedrals":
                readStartDihedrals = True
                readStartAngles = False
            elif lineSplit[0] == "":
                readStartDihedrals = False
                
               
        if len(lineSplit)>1 and readStartAtoms is True: # this means it is an atom line
            # storing the paramers of the atoms  to a 2D list 
            # atomID moldID atomtype charge x y z
            AtomList.append([lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4],lineSplit[5],lineSplit[6]]) 
            
        if len(lineSplit)>1 and readStartBonds is True: # this means it is an atom line
            # storing the paramers of the bonds to a 2D list 
            # bondID bondtype atomID atomID
            BondList.append([lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3]]) 
            
        if len(lineSplit)>1 and readStartAngles is True: # this means it is an atom line
            # storing the paramers of the angles to a 2D list 
            # angleID angletype atomID atomID atomID
            AngleList.append([lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4]]) 
        
        if len(lineSplit)>1 and readStartDihedrals is True: # this means it is an atom line
            # storing the paramers of the dihedrals to a 2D list 
            # dihedralID dihedraltype atomID atomID atomID atomID
            DihedralList.append([lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4],lineSplit[5]])
            
    atomSection = np.array(AtomList).astype(float)
    bondSection = np.array(BondList).astype(int)
    angleSection = np.array(AngleList).astype(int)
    dihedralSection = np.array(DihedralList).astype(int)
    
    # Sort in ascending values of ids in case they are not sorted
    atomSection = atomSection[atomSection[:, 0].argsort()]      # with respect to atom id in 1st column
    bondSection = bondSection[bondSection[:, 0].argsort()]      # with respect to bond id in 1st column
    angleSection = angleSection[angleSection[:, 0].argsort()]   # with respect to angle id in 1st column
    dihedralSection = dihedralSection[dihedralSection[:, 0].argsort()] # with respect to dihedral id in 1st column
    
    if atomSection[0,1] == float(0):           # check if molecules ID start with 0 then it should start with 1
        atomSection[:,1] += float(1)
        
    return (atomSection, bondSection, angleSection, dihedralSection)    


def findidxofmatchingelements(listName, a):
    """
    Retun indexes of the elements in the list "listName" matches with "a"
    """ 
    return [i for i, x in enumerate(listName) if x == a]


def arragebynumatomsinmolecule(eachMolsNumIdx,eachMolsIdx,eachMolsMass,eachMolsCharge,eachMolsBonds,eachMolsAngles,eachMolsDihedrals):
    """
    It stores number of atoms in each molecules in a list where index id molecule ID
    It stores ID of atoms, mass of atoms, charge of atoms in each molecules in dictonaries where key is molecule ID
    It stores bonds, angles, and dihedrals between atoms of each molecules in dictonaries where key is molecule ID
    """
    
    # Identify types of molecule using number of atoms in the molecules
    # list of number of atoms in each type of molecule
    numAtomsOfUniqueMolecule = list(set(eachMolsNumIdx))    # remove duplicates from list
    numMolsOfUniqueMolecule = [] # Number of molecules of each unique molecule in the simulation box
    
    # Find the number of each different type of molecule in the fluid or simulation box
    eachTypeMolsIdx = {}
    eachTypeMolsMass = {}
    eachTypeMolsCharge = {}
    eachTypeMolsBonds = {}
    eachTypeMolsAngles = {}
    eachTypeMolsDihedrals = {}
    for i in numAtomsOfUniqueMolecule:
        idx = findidxofmatchingelements(eachMolsNumIdx, i)  # find the indices of a molecules
        eachTypeMolsIdx[i] = idx                            # Indices of each molecules
        numMolsOfUniqueMolecule.append(len(idx))
        
        a = [x - min(idx) for x in idx]
        eachTypeMolsMass[i] = {}
        eachTypeMolsCharge[i] = {}
        eachTypeMolsBonds[i] = {}
        eachTypeMolsAngles[i] = {}
        eachTypeMolsDihedrals[i] = {}
        for j in a:
            eachTypeMolsMass[i][j] = eachMolsMass[idx[j]]
            eachTypeMolsCharge[i][j] = eachMolsCharge[idx[j]]
            eachTypeMolsBonds[i][j] = eachMolsBonds[idx[j]]
            eachTypeMolsAngles[i][j] = eachMolsAngles[idx[j]]
            eachTypeMolsDihedrals[i][j] = eachMolsDihedrals[idx[j]]
            
    return (numAtomsOfUniqueMolecule,numMolsOfUniqueMolecule,eachTypeMolsIdx,eachTypeMolsMass,eachTypeMolsCharge,eachTypeMolsBonds,eachTypeMolsAngles,eachTypeMolsDihedrals)


def identifymoltype(numAtomsOfUniqueMolecule,numMolsOfUniqueMolecule,eachTypeMolsIdx,eachTypeMolsMass,eachTypeMolsCharge,eachTypeMolsBonds,eachTypeMolsAngles,eachTypeMolsDihedrals):
    """
    Idensity number of unique molecules in the simulation box by comparing masses,
    charges, bonds, angles, and dihedrals of molecules of same number of atoms
    """
    tempMolsMass = {}
    tempMolsCharge = {}
    tempMolsBondNum = {}
    tempMolsAngleNum = {}
    tempMolsDihedralNum = {}
    for i in range(len(numAtomsOfUniqueMolecule)):
        idxi = numAtomsOfUniqueMolecule[i]
        tempMolsMass[idxi] = np.zeros([idxi,numMolsOfUniqueMolecule[i]])
        tempMolsCharge[idxi] = np.zeros([idxi,numMolsOfUniqueMolecule[i]])
        tempMolsBondNum[idxi] = np.zeros([1,numMolsOfUniqueMolecule[i]])
        tempMolsAngleNum[idxi] = np.zeros([1,numMolsOfUniqueMolecule[i]])
        tempMolsDihedralNum[idxi] = np.zeros([1,numMolsOfUniqueMolecule[i]])
        for j in range(numMolsOfUniqueMolecule[i]):
            tempMolsMass[idxi][:,j] = eachTypeMolsMass[idxi][j]
            tempMolsCharge[idxi][:,j] = eachTypeMolsCharge[idxi][j]
            tempMolsBondNum[idxi][:,j] = len(eachTypeMolsBonds[idxi][j])
            tempMolsAngleNum[idxi][:,j] = len(eachTypeMolsAngles[idxi][j])
            tempMolsDihedralNum[idxi][:,j] = len(eachTypeMolsDihedrals[idxi][j])
            
        tempMolsMass[idxi] = np.unique(tempMolsMass[idxi], axis=1)
        tempMolsCharge[idxi] = np.unique(tempMolsCharge[idxi], axis=1)
        tempMolsBondNum[idxi] = np.unique(tempMolsBondNum[idxi], axis=1)
        tempMolsAngleNum[idxi] = np.unique(tempMolsAngleNum[idxi], axis=1)
        tempMolsDihedralNum[idxi] = np.unique(tempMolsDihedralNum[idxi], axis=1)

        np.shape(tempMolsMass[idxi][:])
        np.shape(tempMolsCharge[idxi][:])
        np.shape(tempMolsBondNum[idxi])
        np.shape(tempMolsAngleNum[idxi])
        np.shape(tempMolsDihedralNum[idxi])