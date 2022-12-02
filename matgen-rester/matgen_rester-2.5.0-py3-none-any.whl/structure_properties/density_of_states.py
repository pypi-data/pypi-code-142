# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:33:37 2020

@author: Q Mo
"""

import warnings

class DensityOfStates:
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
  
  def get_total_dos(self):
    return self.TDOS
  
  def get_partial_dos(self, specific_structure=None):
    if specific_structure is None:
      return self.PDOS
    elif specific_structure not in self.structure:
      return "no such structure"
    else:
      return self.PDOS[specific_structure]
  
  def as_dict(self):
    return {"tods":self.total_dos,"pdos":self.partial_dos}
  
  def obj_to_string(self):
    if not isinstance(self, DensityOfStates):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(DensityOfStates.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(DensityOfStates.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()  
  def __eq__(self,other):
    return self == other