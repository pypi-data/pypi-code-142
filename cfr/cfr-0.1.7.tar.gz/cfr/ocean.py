from datetime import datetime
import xarray as xr
import pandas as pd
import numpy as np
import copy
import plotly.express as px
from tqdm import tqdm
from . import visual
from . import utils

class OceanField:
    ''' The class for the gridded ocean field data.
    
    Args:
        da (xarray.DataArray): the gridded data array.
        time_name (str): the name of the time dimension.
        lat_name (str): the name of the latitude dimension.
        lon_name (str): the name of the longitude dimension.
        depth_name (str): the name of the depth dimension.
    '''
    def __init__(self, da=None, time_name=None, lat_name=None, lon_name=None, depth_name=None):
        self.da = da
        if self.da is not None:
            self.refresh(time_name=time_name, lat_name=lat_name, lon_name=lon_name, depth_name=depth_name)

    def __getitem__(self, key):
        ''' This makes the object subscriptable. '''
        new = self.copy()
        new.da = new.da[key]
        if type(key) is tuple:
            new.time = new.time[key[0]]
        else:
            new.time = new.time[key]
        return new

    def refresh(self, time_name=None, lat_name=None, lon_name=None, depth_name=None):
        ''' Refresh a bunch of attributes.
        '''
        time_name = 'time' if time_name is None else time_name
        lat_name = 'lat' if lat_name is None else lat_name
        lon_name = 'lon' if lon_name is None else lon_name
        depth_name = 'depth' if depth_name is None else depth_name

        self.lat = self.da[lat_name].values
        self.lon = self.da[lon_name].values
        self.depth = self.da[depth_name].values
        if time_name == 'year':
            self.time = self.da[time_name].values
        elif time_name == 'time':
            self.time = utils.datetime2year_float(self.da[time_name].values)
        else:
            raise ValueError('Wrong time_name; should be either "time" or "year".')

        self.vn = self.da.name
        self.depth_name = depth_name
        self.lon_name = lon_name
        self.lat_name = lat_name
        self.time_name = time_name
        try:
            self.unit = self.da.attrs['units']
        except:
            self.unit = None