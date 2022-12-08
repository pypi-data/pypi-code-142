# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:01:21 2022

@author: HEHenson
"""
import sys
from enum import Enum
from geograpy import get_geoPlace_context

# Takes a string and returns locational information

# the 3countries

import geolocation
import geocasual

class C3:
    def __init__(self,useNLTK=False,useGEOGRPY=False,mxREC = 100000000000):
       """ Determine country from text location string.
       
       Creates object given in response to location field is classified as either
       Canadian, American or Other
       
       Parameters
       __________
       useNLTK  : bool
           Make use of the NLTK library
       useGEOGRPY : bool
           Make use of the geograpy
       mxREC : int
           Maximum number of records to process
           
       Examples
       ________
       >>>  MyC3 = C3()
       """ 
       import geolocation
       import geocasual
       self.geocasual = geocasual.geocasual()
       self.retval = geolocation.unknownC().UNKNOWN
       self.country = geolocation.unknownC().UNKNOWN
       self.CAN = 11
       self.US = 12
       self.OTHER = 13
       self.useNLTK = useNLTK
       self.useGEOGRPY = useGEOGRPY
       self.MAXREC = mxREC
       # Number of records search for in session
       self.RecNo = 0
       self.CasCoun = geolocation.unknownC().UNKNOWN
    def getC3(self,rawLoc):
       
        self.RecNo += 1
        # two stage exit
        # first warn max is hit
        if self.RecNo == self.MAXREC:
            print('RecNo = ',self.RecNo)
            return unknownC.MX
        # second halt operation
        if self.RecNo > self.MAXREC:
            print('RecNo = ',self.RecNo)
            sys.exit('Maximum Record Hit of ')
        # give Canada Priority
        if self.isCan(rawLoc):
            return self.CAN
        # if it is not Canadian and 
        # we are not going to use NLTK then unknown
        if self.geocasual.isjoke(rawLoc):
            return geolocation.unknownC.JK
        if self.geocasual.isNonUS_Can(rawLoc):
            return self.OTHER
        if self.useGEOGRPY is False:
            return self.OTHER
        if self.geocasual.isUS(rawLoc) is True:
             return self.US
        return self.OTHER
    def isUS(self,rawLoc):
        if self.geocasual.isUS(rawLoc):
            return True
        try:
            if self.places.countries[0] == 'United States of America':
                return True
            else:
                return False
        except:
            print('error rawLoc invalid',rawLoc)
            return False
    def isCan(self,rawLoc):
        if "Canada" in rawLoc:
            return True
        if ",Can " in rawLoc:
            return True
        if "ALBERTA" in rawLoc:
            return True
        if "canada" in rawLoc:
            return True
        if self.geocasual.isCan(rawLoc):
            return True
        if self.useGEOGRPY == False: 
          return False
        # from this point on use geograpy
        # unable to install properly
        self.places = get_geoPlace_context(text=rawLoc)
        try:
            if self.places.countries[0] == "Canada":
                return True
        except:
            return False
        self.country = self.places.countries[0]
        
        return False
            


    
         
