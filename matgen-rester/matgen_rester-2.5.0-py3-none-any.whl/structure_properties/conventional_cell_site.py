# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:30:34 2020

@author: Q Mo
"""

import warnings
import numpy as np
import json

class ConventionalCellSite:
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
    
  def get_atom_coord(self,structure=None):
    if not structure:
      structure = set(self.atomOrder)
    index_list = []
    arr = []
    for index in range(0,len(self.atomOrder)):
      if self.atomOrder[index] == structure:
        index_list.append(index)
    if index_list is []:
      return None
    else:
      for index in index_list:
        arr.append(self.atomCoord[index])
      return np.mat(arr)
    
  def get_atom_order(self):
    return self.atomOrder
  
  def as_dict(self):
    return json.dumps({"atomOrder":self.get_atom_order(),"atomCoord":self.get_atom_coord()})
  
  def obj_to_string(self):
    if not isinstance(self, ConventionalCellSite):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(ConventionalCellSite.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(ConventionalCellSite.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()
  
  def __eq__(self,other):
    return self == other  