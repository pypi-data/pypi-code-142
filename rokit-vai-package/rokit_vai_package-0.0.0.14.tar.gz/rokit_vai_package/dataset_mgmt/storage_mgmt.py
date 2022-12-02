import os    
import sys
from .. import global_variable as gv
from . import gcp_dataset_mgmt as gcp_tf_dsmgmt
from . import aws_dataset_mgmt as aws_tf_dsmgmt
#######################################################################
# import new cloud package
# Example:
# from . import {new_cloud_typ}_dataset_mgmt as {new_cloud_typ}_dsmgmt
#######################################################################


class Storage():
    
    gv = None
    log = None
    dsmgmt = None
    dsmgmt_module = None
    cloud_platform_type = None
    
    
    def __init__(self, global_variable, log):
        self.gv = global_variable
        self.log = log
        
        
    def __set_cloud_dataset_mgmt(self, dsmgmt):
        self.dsmgmt_module = dsmgmt
        self.dsmgmt = self.dsmgmt_module.MiddleDatasetMgmt(self.gv, self.log)

        
    def activate_cloud_platform(self, cloud_platform_type):
        if isinstance(self.gv.eCLOUD_TYPE.GCP, type(cloud_platform_type)):
            self.cloud_platform_type = cloud_platform_type
        else: 
            print("cloud_platform_type error")

    # dataset source type과 deeplearning framework type(tensorflow, pythorch)을 분리해야 함 
    def activate_dataset_source(self, dataset_source_type):
        if isinstance(self.gv.eDATASET_SOURCE_TYPE.TENSRORFLOW, type(dataset_source_type)):
            if self.gv.eDATASET_SOURCE_TYPE.TENSRORFLOW == dataset_source_type:
                self.dsmgmt = self.dsmgmt_module.TensorflowDatasetMgmt(self.gv, self.log)
            if self.gv.eDATASET_SOURCE_TYPE.COCO == dataset_source_type:
                self.dsmgmt = self.dsmgmt_module.COCODatasetMgmt(self.gv, self.log)
            #######################################################################   
            # Add {new_dataset_source_type} activation code in here
            # Example:
            # if self.gv.eDATASET_SOURCE_TYPE.{NEW_DATASET_SOURCE_TYPE} == dataset_source_type:
            #    self.dsmgmt = self.dsmgmt_module.{NewDatasetSourceType}Mgmt(self.gv, self.log)
            #######################################################################
        else: 
            print("dataset_source_type error")
            
            
    def activate_deeplearning_framework(self, dl_framework_type):
        if isinstance(self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.TENSRORFLOW, type(dl_framework_type)):
            if isinstance(self.gv.eCLOUD_TYPE.GCP, type(self.cloud_platform_type)):
                if self.gv.eCLOUD_TYPE.GCP == self.cloud_platform_type:
                    if self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.TENSRORFLOW == dl_framework_type:
                        self.__set_cloud_dataset_mgmt(gcp_tf_dsmgmt)
                    elif self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.PYTORCH == dl_framework_type:
                        self.__set_cloud_dataset_mgmt(gcp_tf_dsmgmt)  #pytorch로 수정 필요
                if self.gv.eCLOUD_TYPE.AWS == self.cloud_platform_type:
                    if self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.TENSRORFLOW == dl_framework_type:
                        self.__set_cloud_dataset_mgmt(aws_tf_dsmgmt)
                    elif self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.PYTORCH == dl_framework_type:
                        self.__set_cloud_dataset_mgmt(aws_tf_dsmgmt) #pytorch로 수정 필요
                #######################################################################   
                # Add {NEW_CLOUD_TYPE} or {new NEW_DL_FRAMEWORK_TYPE} activation code in here
                # Example:
                # if self.gv.eCLOUD_TYPE.{NEW_CLOUD_TYPE} == self.cloud_platform_type:
                #    if self.gv.eDEEPLEARNING_FRAMEWORK_TYPE.{NEW_DL_FRAMEWORK_TYPE} == dl_framework_type:
                #         self.__set_cloud_dataset_mgmt({new_cloud_type}_{NEW_DL_FRAMEWORK_TYPE}_dsmgmt)
                #######################################################################
            else:
                print("cloud_platform_type error")
        else: 
            print("deeplearning_framework error")
   
    
    def activate_platform(self, cloud_type, dl_framework_type, dataset_source_type):
        self.activate_cloud_platform(cloud_type)
        self.activate_deeplearning_framework(dl_framework_type)
        self.activate_dataset_source(dataset_source_type)

        
            
    def make_bucket(self, bucket_name):
        self.dsmgmt.make_bucket(bucket_name)
    
    
    def download_upload_dataset(self, dataset_name, bucket_name):
        self.dsmgmt.make_bucket(bucket_name)
        self.dsmgmt.download(dataset_name)
        self.dsmgmt.upload(bucket_name)

        
    def read_and_split_dataset(self, bucket_name, dataset_bucket_idx, data_split):
        return self.dsmgmt.read_and_split(bucket_name, dataset_bucket_idx, data_split)

        
    def write_dataset(self, path, dataset): 
        print("a")
        self.dsmgmt.write(path, dataset)
        print("b")
        self.dsmgmt.write_dataset_count(path, len(dataset))
        
        
    def read_images(self, path):# -> images, count:
        return self.dsmgmt.read_images(path)
    
    
    def augmentation(self, image_dataset, augmente_type):
        return self.dsmgmt.augmente_image(image_dataset, augmente_type)
    
    
    def merge_image_dataset(self, dataset_paths):
        return self.dsmgmt.merge_image_dataset(dataset_paths)
    
    
    def create_dev_dataset_metadata(self, bucket_name, start_idx, end_idx):
        self.dsmgmt.create_dev_dataset_metadata(bucket_name, start_idx, end_idx)