import os,sys
import logging
import subprocess
import boto3
import awscli
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import time
import pytz

from SharedData.Logger import Logger
from SharedData.MultiProc import io_bound_process

def S3GetSession():
    if 'S3_ENDPOINT_URL' in os.environ:
        _s3 = boto3.resource('s3',endpoint_url=os.environ['S3_ENDPOINT_URL'])
    else:
        _s3 = boto3.resource('s3')
    _bucket = _s3.Bucket(os.environ['S3_BUCKET'].replace('s3://',''))
    return _s3,_bucket

def S3SyncDownloadDataFrame(path,shm_name):
   
    npypath = (os.environ['DATABASE_FOLDER']+'\\'+str(shm_name)).replace('/','\\')+'.npy'
    success = S3Download(npypath)
    jsonpath = npypath.replace('.npy','.json')
    success = (success) & (S3Download(jsonpath))

    if success:
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('AWS S3 Sync DataFrame %s,%s DONE!' % (Logger.user,shm_name))
    else:
        Logger.log.error('AWS S3 Sync DataFrame %s,%s ERROR!' % (Logger.user,shm_name))
    return success

def S3SyncDownloadTimeSeries(path,shm_name):    
    tini = time.time()
    bucket_name = os.environ['S3_BUCKET'].replace('s3://','')
    s3,bucket = S3GetSession()
    bucket = s3.Bucket(bucket_name)
    success=True
    dbfolder = os.environ['DATABASE_FOLDER']
    
    files = np.array([dbfolder+'\\'+obj_s.key.replace('/','\\')\
        for obj_s in bucket.objects.filter(Prefix=shm_name+'/')])
    idx = ['shm_info.json' not in f for f in files]
    files = files[idx]
    if len(files)>0:
        result = io_bound_process(S3DownloadThread,files,[s3])

    if success:
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('AWS S3 Sync timeseries %s,%s DONE!' % (Logger.user,shm_name))
    else:
        Logger.log.error('AWS S3 Sync timeseries %s,%s ERROR!' % (Logger.user,shm_name))
    return success

def S3SyncDownloadMetadata(pathpkl,name):    
    
    success = S3Download(str(pathpkl))
    
    if success:
        if os.environ['LOG_LEVEL']=='DEBUG':
            Logger.log.debug('AWS S3 Sync download metadata %s,%s DONE!' % (Logger.user,name))
    else:
        Logger.log.error('AWS S3 Sync download metadata %s,%s ERROR!' % (Logger.user,name))        
    return success

def S3Download(local_path,s3=None):
    bucket_name = os.environ['S3_BUCKET'].replace('s3://','')
    s3_path = str(local_path).replace(os.environ['DATABASE_FOLDER'],'').replace('\\','/')[1:]
    if s3 is None:
        s3,bucket = S3GetSession()
    # load obj
    obj = s3.Object(bucket_name, s3_path)
    isnewer = False
    ischg = False
    try:
        # remote mtime size
        remote_mtime = obj.last_modified.timestamp()
        if 'mtime' in obj.metadata:
            remote_mtime = float(obj.metadata['mtime'])
        #remote_size = obj.content_length
    except:
        # remote file dont exist 
        return True
    
    if os.path.isfile(str(local_path)):
        # local mtime size
        local_mtime = datetime.utcfromtimestamp(os.path.getmtime(local_path)).timestamp()
        #local_size = os.path.getsize(local_path)
        #compare
        isnewer = remote_mtime>local_mtime
        #ischg = remote_size!=local_size
    else:
        # local file dont exist 
        isnewer = True
        #ischg = True

    if isnewer:
        try:            
            obj.download_file(local_path)
            # update modification time
            remote_mtime_dt = datetime.fromtimestamp(remote_mtime)
            offset =  remote_mtime_dt - datetime.utcfromtimestamp(remote_mtime)        
            remote_mtime_local_tz = remote_mtime_dt+offset
            remote_mtime_local_tz_ts = remote_mtime_local_tz.timestamp()
            os.utime(local_path, (remote_mtime_local_tz_ts, remote_mtime_local_tz_ts))
            if os.environ['LOG_LEVEL']=='DEBUG':
                Logger.log.debug('downloading metadata %s,%s DONE!' % (Logger.user,local_path))
        except Exception as e:
            Logger.log.error('downloading metadata %s,%s ERROR!\n%s' % (Logger.user,local_path,str(e)))
            return False
    return True
    
def S3DownloadThread(iteration, args):
    return [S3Download(iteration,s3=args[0])]

def S3Upload(localfilepath):
    remotefilepath = str(localfilepath).replace(\
            os.environ['DATABASE_FOLDER'],os.environ['S3_BUCKET'])
    remotefilepath = remotefilepath.replace('\\','/')        
    localfilepath = str(localfilepath).replace('\\','/')
      
    trials = 3
    success=False
    while trials>0:        
        try:                
            s3,bucket = S3GetSession()            
            mtime = os.path.getmtime(localfilepath)
            mtime_utc = datetime.utcfromtimestamp(mtime).timestamp()
            mtime_str = str(mtime_utc)
            bucket.upload_file(localfilepath,remotefilepath.replace(os.environ['S3_BUCKET'],'')[1:],\
                ExtraArgs={'Metadata': {'mtime': mtime_str}})
            if os.environ['LOG_LEVEL']=='DEBUG':
                Logger.log.debug(Logger.user+' Uploading to S3 '+str(localfilepath)+' DONE!')
            success = True
            break
        except Exception as e:
            Logger.log.warning(Logger.user+' Uploading to S3 '+localfilepath+' FAILED! retrying(%i,3)...\n%s ' % (trials,str(e)))
            trials = trials - 1

    if not success:
        Logger.log.error(Logger.user+' Uploading to S3 '+localfilepath+' ERROR! \n%s ' % str(e))