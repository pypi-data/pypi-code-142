# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:31:20 2022

@author: Darshan Rathod
"""


import numpy as _np
import pandas as _pd
import time as _time
import os as _os
import pickle as _pickle

from alicat import FlowController as _fc

def make_dir(path1):
    try:
        _os.mkdir(path1)
    except FileExistsError as e:
        pass


class mfc(_fc):
    
    def __init__(self,port='COM5',address='A',name='mfc',task_type='mfc',foldpath=''):
        super().__init__(port=port,address=address)
        self.foldpath = foldpath
        self.setter_filepath = _os.path.join(self.foldpath,'setter.pickle')
        self.SLPM = 0
        
        self.make_folders()
        
        self._info = None
        self._data_units = None
        self._name = name
        self.task_type = task_type.lower()
    
    def make_folders(self):
        if self.foldpath == '':
            return
        else:
            make_dir(self.foldpath)
            return
    
    @property
    def SLPM(self):
        with open(self.setter_filepath,'rb') as f:
            a = _pickle.load(f)
        return a
    
    @SLPM.setter
    def SLPM(self,n):
        self.set_flow_rate(n)
        with open(self.setter_filepath,'wb') as f:
            _pickle.dump(n,f)
        return
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
    
    @property
    def is_closed(self):
        return not(self.open)
    
    def read(self,n=1,sleep_time=0):
        d1 = _pd.DataFrame()
        for i in range(n):
            d1 = d1.append(_pd.DataFrame(self.get(),index=[i]))
            _time.sleep(sleep_time)
        d1.columns = [self._name+'_'+ky for ky in d1.keys()]
        self.data = d1
        return d1
        
    def read_mean(self):
        return self.read(n=1)
    
    def _make_plot(self):
        fig,ax = _plt.subplots(figsize=(10,5))
        return fig,ax
        
    @property
    def info(self):
        if self._info is None:
            dict1 = {
                'pressure':'Upstream pressure in PSIA',
                'temperature':'gas temperature in deg C',
                'volumetric_flow':'LPM',
                'mass_flow':'SLPM',
                'setpoint':'set point in SLPM',
                'gas':'selected gas media',
                'control_point':'None',
                }
            return dict1
        else:
            return self._info
        
    @info.setter
    def info(self,dict1):
        self._info = dict1
    
    @property
    def data_units(self):
        if self._data_units is None:
            dict1 = {
                'pressure':'PSIA',
                'temperature':'deg C',
                'volumetric_flow':'LPM',
                'mass_flow':'SLPM',
                'setpoint':'SLPM',
                'gas':'string',
                'control_point':'None',
                }            
            return dict1
        else:
            return self._data_units
    
    @data_units.setter
    def data_units(self,dict1):
        self._data_units = dict1
    