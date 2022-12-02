# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:23:53 2020

@author: Q Mo
"""

from unittest import TestCase
import matgen_rester as mr

class TestRester(TestCase):
  def test_rester_matid_by_id_output_MatData(self):
    with mr.Matgenrester() as m:
      data = m.get_structure_by_id(idType="matid",targetId="mat_16680",fields=["structure.matid","structure.formula"])
    self.assertTrue(isinstance(data,mr.matdata.MatData))
    
  def test_rester_matid_by_id_dict(self):
    with mr.Matgenrester() as m:
      data = m.get_strcuture_by_id(idType="matid",targetId="mat_16680",fields=["structure.formula"],matgen_decode=False)
    self.assertEqual(data,{'structure.formula', "Ba4 Cu16 S12"})
  
  def test_rester_filter_by_ne_dict(self):
     with mr.Matgenrester() as m:
      data = m.get_structure_with_filter(elements="Ba-S", filter={"_nelements":"O-Ti"}, fields=['matid'], matgen_decode=False,pages=5, pageno=0)
     self.assertEqual(data,[{"matid":"mat_16736"},{"matid":"mat_3"},{"matid":"mat_52"},{"matid":"mat_291"},{"matid":"mat_886"}])
   
  def test_rester_filter_by_filter_dict(self):
    with mr.Matgenrester() as m:
      data = m.get_structure_with_filter(elements="Ba-S", filter={"_voume":[0,100],"_crystal_system":["cubic","tetragonal","hexagonal","trigonal","orthorhombic","monoclinic","triclinic","amorphous"]}, fields=['matid'], matgen_decode=False,pages=5, pageno=0)
    self.assertEqual(data,[{'matid': 'mat_32840'}, {'matid': 'mat_82034'}])
