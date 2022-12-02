# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:14:56 2020

@author: Q Mo
"""

import warnings
import numpy as np
import json

class PrimitiveCellSite:
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
  
  def get_crystal_system(self):
    return self.crystal_system
  
  def get_point_group(self):
    return self.point_group
  
  def as_dict(self):
    return json.dumps({"crystal_system":self.crystal_system,"point_group":self.point_group})

  def obj_to_string(self):
    if not isinstance(self, PrimitiveCellSite):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(PrimitiveCellSite.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(PrimitiveCellSite.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()
  
  def __eq__(self,other):
    return self == other
  
  