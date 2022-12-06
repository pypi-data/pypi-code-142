import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd

from SharedData.Logger import Logger
from SharedData.SharedDataFeeder import SharedDataFeeder
from SharedData.Metadata import Metadata
from SharedData.SharedDataRealTime import SharedDataRealTime

class SharedData:
    
    def __init__(self, database, mode='rw', user='master',\
        debug=None,sync_frequency_days=None):        
        
        if Logger.log is None:            
            Logger('SharedData')

        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('Initializing SharedData %s,%s,%s ...' % (user,database,mode))
        
        self.database = database        
        self.user = user
        
        self.s3read = False
        self.s3write = False
        if mode == 'r':
            self.s3read = True
            self.s3write = False
        elif mode == 'w':
            self.s3read = False
            self.s3write = True
        elif mode == 'rw':
            self.s3read = True
            self.s3write = True

        if (Logger.user!='master') & (user=='master'):
            self.s3write=False
            mode = 'r'
        
        self.mode = mode
            
        # DATA DICTIONARY
        # SharedDataTimeSeries: data[feeder][period][tag] (date x symbols)
        # SharedDataFrame: data[feeder][period][date] (symbols x tags)
        self.data = {} 

        # Symbols collections metadata
        self.metadata = {}

        # static metadata
        self.static = pd.DataFrame([])
        
        Logger.log.debug('Initializing SharedData %s,%s,%s DONE!' % (user,database,mode))

    def __setitem__(self, feeder, value):
        self.data[feeder] = value
                
    def __getitem__(self, feeder):        
        if not feeder in self.data.keys():
            self.data[feeder] = SharedDataFeeder(self, feeder)
        return self.data[feeder]

    def getMetadata(self, collection):
        if not collection in self.metadata.keys():              
            self.metadata[collection] = Metadata(collection,\
                mode=self.mode,\
                user=self.user)
            self.mergeUpdate(self.metadata[collection].static)            
        return self.metadata[collection]

    def getSymbols(self, collection):        
        return self.getMetadata(collection).static.index.values

    def mergeUpdate(self,newdf):
        ddidx = newdf.index.duplicated()
        if ddidx.any():
            newdf = newdf[~newdf.index.duplicated(keep='first')]            
            Logger.log.warning('Metadata merge duplicated index for new dataframe!')
        
        ddidx = self.static.index.duplicated()        
        if ddidx.any():
            self.static = self.static[~self.static.index.duplicated(keep='first')]            
            Logger.log.warning('Metadata merge duplicated index for static dataframe!')

        newcolsidx = ~newdf.columns.isin(self.static.columns)
        if newcolsidx.any():
            newcols = newdf.columns[newcolsidx]
            for c in newcols:
                self.static.loc[:,c] = newdf[c]                

        newidx = ~newdf.index.isin(self.static.index)
        if newidx.any():
            self.static = self.static.reindex(index=self.static.index.union(newdf.index))

        newcol = ~newdf.columns.isin(self.static.columns)
        if newcol.any():
            self.static = self.static.reindex(columns=self.static.columns.union(newdf.columns))
            
        self.static.update(newdf)
  
    def SubscribeRealTime(self):
        SharedDataRealTime.Subscribe(self)