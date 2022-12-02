# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:20:44 2020

@author: Q Mo
"""

import argparse
def parse_cml_args(cml):
	parser = argparse.ArgumentParser(description="manual to this script")
	parser.add_argument("-idType", "--idType",dest='idType', action='store',help="specify the idType for search, such as matid, icsd_id, cod_id, oqmd_id",type=str,default = None)
	parser.add_argument("-id", "--id",dest='id', action='store',help="find the structure with the target id,such as mat_8886 as matid",type=str,default = None)
	parser.add_argument("-size","--size", dest='size', action='store',help="specify the number of return data",type=int,default = 0)
	parser.add_argument("-pindex", "--pindex",dest='pindex', action='store',type=int,help="specify the page index after pagination",default = 0)
	parser.add_argument("-in", "--in",dest='in', action='store',help="find the structures that contain the specific elements, for more than one elements, connect elements by '-', ex. Ba-S",type=str)
	parser.add_argument("-not", "--not",dest='not', action='store',help="find the structures that don't contain the specific elements, for more than one elements, connect elements by '-', ex. Ba-S",type=str)
	parser.add_argument("-searchType", "--searchType",dest='searchType', action='store',help="specify the search type for searching structures, 'only' means finding the structures that only contain the specific elements, 'all' means finding the structures that not only contain the specific elements, but also, sometimes, other elements",type=str)	
	parser.add_argument("-crystalSystem", "--crystalSystem",dest='crystalSystem', action='store',help="filter data by its crystal_system, such as cubic,tetragonal,hexagonal,trigonal,orthorhombic,monoclinic,triclinic,amorphous",type=str)
	parser.add_argument("-pointGroup", "--pointGroup",dest='pointGroup', action='store',help="filter data by its point_group, such as cubic,tetragonal,hexagonal,trigonal,orthorhombic,monoclinic,triclinic,amorphous",type=str)	
	parser.add_argument("-spacegroup","--spacegroup", dest='spacegroup', help="filter data by its spacegroup, specify space group type, such as P1,P-1,P2,P21,C2,Pm,Pc,Cm,Cc,P2/m,P21m,P2/c,P21c,C2/m,C2/c,P222,P2221,P21212,P212121,C222,C2221,F222,I222,I212121,Pmm2,Pmc21,Pcc2,Pma2,Pca21,Pnc2,Pmn21,Pba2,Pna21,Pnn2,Cmm2,Cmc21,Ccc2,Amm2,Abm2,Ama2,Aba2,Fmm2,Fdd2,Imm2,Iba2,Ima2,Pmmm,Pnnn,Pccm,Pban,Pmma,Pnna,Pmna,Pcca,Pbam,Pccn,Pbcm,Pnnm,Pmmn,Pbcn,Pbca,Pnma,Cmmm,Cmcm,Cmca,Cccm,Cmma,Ccca,Fmmm,Fddd,Immm,Ibam,Ibcm,Imma,P4,P41,P42,P43,I4,I41,P-4,I-4,P4/m,P42/m,P4/n,P42/n,I4/m,I41/a,P422,P4212,P4122,P41212,P4222,P42212,P4322,P43212,I422,I4212,P4mm,P4bm,P42cm,P42nm,P4cc,P4nc,P42mc,P42bc,I4mm,I4cm,I41md,I41cd,P-42m,P-42c,P-421m,P-421c,I-42m,I-42d,P-4m2,P-4c2,P-4b2,P-4n2,I-4m2,I-4c2,P4/mmm,P4/mcc,P4/nbm,P4/nnc,P4/mbm,P4/mnc,P4/nmm,P4/ncc,P42/mmc,P42/mcm,P42/nbc,P42/nnm,P42/mbc,P42/mcm,P42/nmc,P42/ncm,I4/mmm,I4/mcm,I41/amd,I41/acd,P3,P31,P32,R3,P-3,R-3,P312,P3112,P3212,P321,P3121,P3221,R32,P31m,P31c,P3m1,P3c1,R3m,R3c,P-31m,P-31c,P-3m1,P-3c1,R-3m,R-3c,P6,P61,P62,P63,P64,P65,P-6,P6/m,P63/m,P622,P6122,P6222,P6322,P6422,P6522,P6mm,P6cc,P63cm,P63mc,P-6m2,P-6c2,P-62m,P62c,P6/mmm,P6/mcc,P63/mcm,P63/mmc,P23,P213,F23,I23,I213,Pm-3,Pn-3,Pa-3,Fm-3,Fd-3,Im-3,Ia-3,P432,P4232,P4332,P4132,F432,F4132,I432,I4132,P-43m,P-43n,F-43m,F-43c,I-43m,I-43d,Pm-3m,Pn-3n,Pm-3n,Pn-3m,Fm-3m,Fm-3m,Fd-3m,Fd-3c,Im-3m,Ia-3d", action='store',type=str)
	parser.add_argument("-volume", "--volume",dest='volume', action='store',help="filter data by its volume, specify volume scope, such as '0,100'", type=str,default = None)
	parser.add_argument("-density", "--density",dest='density', action='store',help="filter data by its density, specify volume scope, such as '0,100'", type=str)
	parser.add_argument("-icsdid", "--icsdid",dest='icsdid', action='store',help="filter data if it contains a icsdid", type=bool)
	parser.add_argument("-codid", "--codid",dest='codid', action='store',help="filter data if it contains a codid", type=bool)
	parser.add_argument("-oqmdid", "--oqmdid",dest='oqmdid', action='store',help="filter data if it contains a oqmdid", type=bool)
	parser.add_argument("-fields", "--fields", dest='fields', action='store',type=str,help="specify return data fields, such as 'structure', 'bandStructure', 'densityOfStates', 'cif', 'elasticProperty', 'fermiSurface', 'magneticProperty', 'pdf', 'xrd'",default = None)
	parser.add_argument("-o", dest='o', action='store',help="set file for downloading",type=str,default = None)
	parser.add_argument("-token","--token", dest='token', action='store',help="upload matgen token for seaching",type=str,default = None)
	return parser.parse_args(cml)

