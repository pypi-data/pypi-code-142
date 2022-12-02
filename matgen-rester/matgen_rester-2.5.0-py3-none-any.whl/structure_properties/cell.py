# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:51:30 2020

@author: Q Mo
"""

import warnings
import numpy as np

class Cell:
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
  
  def get_matrix(self,i=-1,j=-1):
    if i is not -1 and j is not -1:
      return self.matrix[i][j]
    elif i is not -1:
      return self.matrix[i]
    else:
      return np.mat(self.matrix)
  
  def get_a(self):
    return self.a
  
  def get_b(self):
    return self.b
  
  def get_c(self):
    return self.c
  
  def get_alpha(self):
    return self.alpha
  
  def get_beta(self):
    return self.beta
  
  def get_gamma(self):
    return self.gamma
  
  def get_volume(self):
    return self.volume
  
  def as_dict(self):
    return {"matrix":self.get_matrix().tolist(),"a":self.get_a(),"b":self.get_b(),"c":self.get_c(),"alpha":self.get_alpha(),"beta":self.get_beta(),"gamma":self.get_gamma(),"volume":self.get_volume()}
  
  def obj_to_string(self):
    if not isinstance(self, Cell):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(Cell.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(Cell.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()
  
  def __eq__(self,other):
    return self == other