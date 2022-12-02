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
import pandas as pd
from multiprocessing import Pool

from . import getinfofromlammpsdatafile
from . import getadjacencyanddistancematrices
from . import getinfofromlammpstrajfile 
from . import rdf
from . import morse
from . import moreaubroto 
from . import geary
from . import moran 
from . import whim  
from . import geometricdescriptors 
from . import topologyconnectivity3Ddescriptors 

"""
############################################ ADDITIONAL FUNCTIONS ###########################################
"""
def findidxofmatchingelements(listName, a):
    """
    Retun indexes of the elements in the list "listName" matches with "a"
    """
    return [i for i, x in enumerate(listName) if x == a]

def caldensity(atomMasses, vol):
    """
    Parameters ----------
    mass : mass of all atoms in the simulation box [], numpy.array - (numAtoms x 1) 
    vol : volume of the simulation box [ÅxÅxÅ], float - 1
    
    Returns -------
    rho : simulation calculated density of the fluid [g/cc], float - 1
    """
    NA = 6.0221408e+23              # Avogadro's number [1/mol]
    volcc = vol*1.0E-24             # volume of the simulation box [cc]
    
    # Simulation-calculated density [g/cc]
    rho = (np.sum(atomMasses)/volcc)*(1.0/NA) 
    return rho

def calgeometricdistancematrix(xyz):
    """
    Calculate Euclidean Distance of atoms in a molecule - (numAtoms x numAtoms)
        G = Geometric Distance Matrix
        Ginv = Inverse Geometric Distance Matrix
        Gx = Euclidean distance of atoms in a molecule in x-direction
        Gy = Euclidean distance of atoms in a molecule in y-direction
        Gz = Euclidean distance of atoms in a molecule in z-direction
    """
    onesMat = np.ones([len(xyz),len(xyz)])
    Gx = onesMat*xyz[:,0]-np.transpose(onesMat*xyz[:,0])
    Gy = onesMat*xyz[:,1]-np.transpose(onesMat*xyz[:,1])
    Gz = onesMat*xyz[:,2]-np.transpose(onesMat*xyz[:,2])
    G = np.sqrt(Gx**2 + Gy**2 + Gz**2)
    return (G, Gx, Gy, Gz)



def Descriptors(datafilename, dumpfilename, fromWhichFrame, toWhichFrame):

    """
    ############################################ DEFINE/PROVIDE REQUIRED INFORMATION ###########################################
    """
    # locationDataFile = './'
    # locationDumpFile = './'
    # datafilename = locationDataFile + 'methylpentaneAA.txt'
    # dumpfilename = locationDumpFile + 'NPT_w_methylpentaneAA_T100CP1atm.lammpstrj'
    # fromwhichframe = 0
    # numCores = 4



    """
    ######################################## GET ALL INFORMATIONS FROM LAMMPS DATA FILE ########################################
    """
    idAtoms, idMols, atomTypes, atomCharges, atomMasses, atomSection, bondSection, angleSection, dihedralSection =  getinfofromlammpsdatafile.getalldatafileinfo(datafilename)
    eachMolsNumIdx,eachMolsIdx,eachMolsMass,eachMolsCharge,eachMolsBonds,eachMolsAngles,eachMolsDihedrals = getinfofromlammpsdatafile.arragebymolecule(idAtoms, idMols, atomMasses, atomCharges, bondSection, angleSection, dihedralSection)
    numAtoms = len(idAtoms) # num of atoms in the simulation box        
    numMols = max(idMols)   # num of molecules in the simulation box



    """
    ######################################## Get adjacency and distnace matrices from rdkit ########################################
    """
    eachMolsAdjMat, eachMolsDisMat = getadjacencyanddistancematrices.getadjANDdismatrices(atomSection, eachMolsIdx, eachMolsBonds, eachMolsMass)



    """
    ######################################## GET ALL INFORMATIONS FROM LAMMPS DUMP FILE ########################################
    """

    import time

    start = time.perf_counter()



    xmin, xmax, ymin, ymax, zmin, zmax, lx, ly, lz = getinfofromlammpstrajfile.getboxboundariesANDlengths(dumpfilename)
    colid, colmol, coltype, colx, coly, colz, needToUnwrap = getinfofromlammpstrajfile.getcolumns(dumpfilename)
    datadump, datadumpdict, nframes = getinfofromlammpstrajfile.readlammpsdumpfile(dumpfilename, numAtoms, colid, colmol, coltype, colx, coly, colz, needToUnwrap, lx, ly, lz)
    tsfirst = getinfofromlammpstrajfile.gettsfirst(dumpfilename)      # [fs]
    tsjump = getinfofromlammpstrajfile.gettsjump(dumpfilename)        # [fs]
    tslast = tsfirst + (nframes-1)*tsjump   # [fs]

    # Volume of the simulation box 
    vol = lx*ly*lz                          # [ÅxÅxÅ]

    # Density at a time frame
    rho = caldensity(atomMasses, vol)       # [g/cc]

    eachMolsVolume = {}
    for i in range(numMols):
        NA = 6.0221408e+23              # Avogadro's number [1/mol]        
        Mw = np.sum(eachMolsMass[i])    # Molar mass [g/mol]
        eachMolsVolume[i] = Mw/(rho*NA)*1.0E24 # volume of the simulation box [Å^3]
        

    avgRg = []
    moleculeList = []
    Empty_dic = {} # initialize a dictionary for the current model

    df_average = pd.DataFrame(Empty_dic) # average of all molecules
    for i in range(numMols):
    # for i in range(4):
        moleculeList.append(i)
        frameList = [] # initialize a list for time frame

        df_RDF = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_MoRSE = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_ATS = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_GATS = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_MATS = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_WHIM = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_GMdes = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_DDMdes = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        df_TCdes = pd.DataFrame(Empty_dic) # initialize a pandas dataframe for the current molecule
        mass = eachMolsMass[i]
        charge = eachMolsCharge[i]
        bond = eachMolsBonds[i]
        angle = eachMolsAngles[i]
        dihedral = eachMolsDihedrals[i]
        molvolume = eachMolsVolume[i]
        disMat = eachMolsDisMat[i]
        adjMat = eachMolsAdjMat[i]
        Rg = []
        # for j in range(fromwhichframe, nframes):
        for j in range(fromWhichFrame, toWhichFrame):
            frameList.append(j)
            # print(i,' ',j)
            # xyz coordinates
            xyz = datadumpdict[j][i][:,3:6]
            # Geometric matrix
            G, _, _, _ = calgeometricdistancematrix(xyz)  
            
            # Descriptors
            RDF = rdf.calrdfdescriptors(G, mass, charge)            # 30*3 = 90
            MoRSE = morse.calmorsedescriptors(G, mass, charge)        # 30*3 = 90
            ATS = moreaubroto.calmoreaubrotodescriptors(G, mass, charge)    # 20*2 = 40
            GATS = geary.calgearyindices(G, mass, charge)             # 20*2 = 40
            MATS = moran.calmorandescriptors(G, mass, charge)         # 20*2 = 40
            WHIM = whim.calwhimdescriptors(xyz,mass,charge)          # 14*3 = 42
            GMdes, DDMdes = geometricdescriptors.calgeometricdescriptors(xyz, mass, charge, bond, angle, dihedral, molvolume, disMat) # GMdes = 83, DDMdes = 10
            TCdes = topologyconnectivity3Ddescriptors.caltopologyconnectivitydescriptors(xyz, mass, bond, angle, dihedral, adjMat, disMat) # TCdes = 27
            df_RDF = df_RDF.append(RDF, ignore_index = True)
            df_MoRSE = df_MoRSE.append(MoRSE, ignore_index = True)
            df_ATS = df_ATS.append(ATS, ignore_index = True)
            df_GATS = df_GATS.append(GATS, ignore_index = True)
            df_MATS = df_MATS.append(MATS, ignore_index = True)
            df_WHIM = df_WHIM.append(WHIM, ignore_index = True)
            df_GMdes = df_GMdes.append(GMdes, ignore_index = True)
            df_DDMdes = df_DDMdes.append(DDMdes, ignore_index = True)
            df_TCdes = df_TCdes.append(TCdes, ignore_index = True)
        
        # Dump descriptors of a molecule for all time frames
        df = pd.concat([df_RDF, df_MoRSE, df_ATS, df_GATS, df_MATS, df_WHIM, df_GMdes, df_TCdes], axis=1)
        df.insert(0, "Frame", frameList) # insert frame index to the first column of the table
        df.to_csv(str(dumpfilename)+'-molecule_'+str(i)+'.csv')
        average = df.mean()
        average.pop('Frame')
        df_average[i] = average
        # df.to_csv('Molecule_'+str(i)+'.csv')
    # Average descriptors of each moleculer over all time frames
    df_average.to_csv(str(dumpfilename)+'-Frame_'+str(fromWhichFrame)+'-' +str(fromWhichFrame)+'-average'+'.csv')
            
        
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 6)} second(s)')        
        