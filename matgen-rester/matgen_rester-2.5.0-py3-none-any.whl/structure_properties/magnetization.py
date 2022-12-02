# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:19:29 2020

@author: Q Mo
"""

from .MatgenError import MatgenError

class Magnetization(object):
  def __init__(self, entries: dict={}):
    self.__dict__.update(entries)
  
  def get_labels(self):
    if 'labels' in dir(self):
      return self.labels
    else:
      raise MatgenError("KeyError, can't get value of magnetization.labels")
  
  def __getattribute__(self, name):
    return object.__getattribute__(self, name)
  
  def __getattr__(self,name):
    return 'Not Found {}'.format(name)
  
  def get_mag_by_elements(self,elements, mag):
    if (elements in dir(self)) and ('labels' in dir(self)) and (mag in self.get_labels()):
      if len(self.__getattribute__(elements))> self.get_labels().index(mag):
        return self.__getattribute__(elements)[self.get_labels().index(mag)]
    else:
      raise MatgenError("KeyError, can't get value of magnetization.{}.{}".format(elements,mag))

  def obj_to_string(self):
    if not isinstance(self, Magnetization):
        raise TypeError("obj_to_string func: 'the object is not an instance of the specify class.'")
    to_string = str(Magnetization.__name__) + "("
    items = self.__dict__
    n = 0
    for k in items:
        if k.startswith("_"):
            continue
        to_string = to_string + str(k) + ":" + str(items[k]) + ","
        n += 1
    if n == 0:
        to_string += str(Magnetization.__name__).lower() + ": 'Instantiated objects have no property values'"
    return to_string.rstrip(",") + ")"
  
  def __str__(self):
    return self.obj_to_string()
  
if __name__=="__main__":
  m = Magnetization({"labels":["sp","ps"],"s":[1,2],"p":[2,1]})
  print(m.get_labels())
  print(m.get_mag_by_elements("s", "ps"))