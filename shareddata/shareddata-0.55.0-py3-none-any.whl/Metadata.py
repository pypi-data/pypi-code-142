import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import numpy as np
import time
import subprocess
from datetime import datetime, timedelta

from SharedData.Logger import Logger
from SharedData.SharedDataAWSS3 import S3SyncDownloadMetadata,S3Upload

class Metadata():
    
    def __init__(self, name, mode='rw', user='master',\
        sync_frequency_days=None, debug=None):
        
        if Logger.log is None:
            Logger('Metadata')
        
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

        self.name = name
        self.xls = {}
        self.static = pd.DataFrame([])                
        self.fpath = Path(os.environ['DATABASE_FOLDER']) / user

        self.pathxls = self.fpath /  ('Metadata/'+name+'.xlsx')
        self.pathpkl = self.fpath /  ('Metadata/'+name+'.pkl')        

        if (self.s3read):            
            S3SyncDownloadMetadata(self.pathpkl,self.name)
                    
        # prefer read pkl
        # but read excel if newer
        readpkl = self.pathpkl.is_file()
        readxlsx = self.pathxls.is_file()
        if (readpkl) & (readxlsx):
            readxlsx = os.path.getmtime(self.pathxls)>os.path.getmtime(self.pathpkl)
            readpkl = not readxlsx
        
        if readpkl:
            tini = time.time()

            self.static = pd.read_pickle(self.pathpkl)
            self.static = self.static.sort_index()

            if os.environ['LOG_LEVEL']=='DEBUG':
                Logger.log.debug('Loading metadata pkl %s %.2f done!' % (name,time.time()-tini))

        elif readxlsx:
            tini = time.time()
            
            self.xls = pd.read_excel(self.pathxls,sheet_name=None)
            if 'static' in self.xls:
                self.static = self.xls['static']

            if not self.static.empty:
                self.static = self.static.set_index(self.static.columns[0])

            if os.environ['LOG_LEVEL']=='DEBUG':
                Logger.log.debug('Loading metadata xlsx %s %.2f done!' % (name,time.time()-tini))
        
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('Initializing Metadata %s,%s DONE!' % (name,mode))

    def save(self,save_excel=False):
        tini = time.time()
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('Saving metadata ' + self.name + ' ...')  
        if not os.path.isdir(self.pathpkl.parents[0]):
            os.makedirs(self.pathpkl.parents[0])                   

        # save excel first so that last modified
        # timestamp is older        
        if save_excel:
            with open(self.pathpkl, 'wb') as f:
                writer = pd.ExcelWriter(f, engine='xlsxwriter')            
                self.static.to_excel(writer,sheet_name='static')
                writer.save()
                f.flush()

            if self.s3write:
                S3Upload(self.pathxls)

        with open(self.pathpkl, 'wb') as f:
            self.static.to_pickle(f)
            f.flush()

        if self.s3write:
            S3Upload(self.pathpkl)

        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('Saving metadata ' + self.name + ' %.2f done!' % (time.time()-tini))
    
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

    def __setitem__(self, tag, value):
        self.static[tag] = value
                
    def __getitem__(self, tag):
        return self.static[tag]