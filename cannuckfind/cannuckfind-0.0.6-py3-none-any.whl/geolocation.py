# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:01:21 2022

@author: HEHenson
"""

#from enum import Enum

# should be moved into some sort of universal toolbox

class unknownC(object):

    '''
    Expands on the concept of unknown variables.
    '''
    def __init__(self):
        # uninitialized
        self.UNKNOWN = int(101)
        # known to be private
        self.PRIV = int(102)
        # unknown to be not available
        self.NA = int(103)
        # invalid value
        self.NL = int(104)
        # Joke
        self.JK = int(105)
        # maximum number of records in run
        self.MX = int(106)
 
 
