from abc import *

import os
import sys
import json
import cv2 as cv
from io import BytesIO
# from google.cloud import storage
# from google.cloud.storage import Blob
import tensorflow_datasets as tfds

from .. import global_variable as gv
from . import dataset_mgmt as dsmgmt

class MiddleDatasetMgmt(dsmgmt.DatasetMgmt):
    
    def __init__(self, global_variable, log):
        super(MiddleDatasetMgmt, self).__init__(global_variable, log)
        #self.client = storage.Client(self.gv.PROJECT_ID)
        
        
    def make_bucket(self, bucket_name):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")  
        self.log.info("under contruction") 
        
            
    def download(self, dataset_name):
        self.log.info("under contruction")
        
    
    def upload(self, bucket_name):
        self.bucket_name = bucket_name
        self.log.info("under contruction")


        
class TensorflowDatasetMgmt(MiddleDatasetMgmt):
    
    def download(self, dataset_name):
        self.dataset = tfds.load(dataset_name, with_info=False)
    
    
    def upload(self, bucket_name):
        self.log.info("under contruction")
    
    
    def __upload_dataset_to_bucket(self, dataset, data_type_name):
        self.log.info("under contruction")
    
    
    def __upload_dataset_label_to_bucket(self, dataset_list): 
        self.log.info("under contruction")
    
    
    
class COCODatasetMgmt(MiddleDatasetMgmt):
    
    def download(self, dataset_name):
        self.log.info("under contruction")
    
    
    def upload(self, bucket_name):
        self.log.info("under contruction")
      
    
    def __upload_dataset_to_bucket(self, dataset, data_type_name):
        self.log.info("under contruction")
    
    
    def __upload_dataset_label_to_bucket(self, dataset_list): 
        self.log.info("under contruction")
