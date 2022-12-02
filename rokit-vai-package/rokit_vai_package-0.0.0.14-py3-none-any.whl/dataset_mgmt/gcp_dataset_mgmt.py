import os
import sys
import json
import cv2 as cv
import numpy as np
from io import BytesIO
import tensorflow as tf
import tensorflow_datasets as tfds
from google.cloud import storage
from google.cloud.storage import Blob
from sklearn.model_selection import train_test_split
from .. import global_variable as gv
from . import dataset_mgmt as dsmgmt

import pandas as pd


class MiddleDatasetMgmt(dsmgmt.DatasetMgmt):
    
    def __init__(self, global_variable, log):
        super(MiddleDatasetMgmt, self).__init__(global_variable, log)
        self.client = storage.Client(self.gv.PROJECT_ID)
        
        
    def _bytes_feature(self, value):
        """Returns a bytes_list from a string / byte."""
        if isinstance(value, type(tf.constant(0))):
            value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

    
    def _float_feature(self, value):
        """Returns a float_list from a float / double."""
        return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

    
    def _int64_feature(self, value):
        """Returns an int64_list from a bool / enum / int / uint."""
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
    
    
    def _make_example_image(self, image_bytes, label_bytes): #write
        feature = {'image': self._bytes_feature(image_bytes),
                   'segmentation_mask': self._bytes_feature(label_bytes)}
        return tf.train.Example(features=tf.train.Features(feature=feature))
    
    
    def _make_example_metadata(self, label, value): #write
        feature = {label: self._int64_feature(value)}
        return tf.train.Example(features=tf.train.Features(feature=feature))
    
    
    def _get_dataset_metadata(self, bucket):
        blob = bucket.blob(self.gv.DEV_DATASET_METADATA_NAME) if self.gv.DEV_MODE else bucket.blob(self.gv.DATASET_METADATA_NAME)
        
        if self.gv.DEV_MODE and None is blob:
            print(f"{self.gv.DEV_DATASET_METADATA_NAME} is not exist")
            blob = bucket.blob(self.gv.DATASET_METADATA_NAME)
        
        with blob.open("r") as f:
            metadata_list = json.loads(f.read())
            
        return metadata_list
    
    
    def _parse_image_function(self, example_proto): # read
        image_feature_description = {
            'image': tf.io.FixedLenFeature([], tf.string),
            'segmentation_mask':tf.io.FixedLenFeature([], tf.string),
        }
        return tf.io.parse_single_example(example_proto, image_feature_description)
                           
                           
    def _parse_image_count_function(self, example_proto): # read
        image_count_feature_description = {
            'count': tf.io.FixedLenFeature([], tf.int64),
        }
        return tf.io.parse_single_example(example_proto, image_count_feature_description)
    
    
    def _augmentation(self, image, segmentation_mask, augmente_type):
        image_aug = tf.image.flip_left_right(image)
        segmentation_mask_aug = tf.image.flip_left_right(segmentation_mask)
        return image_aug, segmentation_mask_aug
    
    ###
    
    def make_bucket(self, bucket_name):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        
        try:
            self.client.get_bucket(bucket_name) #lockup_bucket을 대신 사용할 수도 있음
            self.log.info(f"{bucket_name} bucket already exists")
        except:
            self.log.info(f"{bucket_name} bucket doesn't exists")
            bucket = self.client.bucket(bucket_name)
            bucket.storage_class = "STANDARD"
            
            #mb : make bucket (PROJECT_ID와 REGION에 종속된 DATA_BUCKET 생성)
            #!gsutil mb -p $self.gv.PROJECT_ID -c standard -l $self.gv.REGION gs://$gv.DATA_BUCKET 
            new = self.client.create_bucket(bucket, project=self.gv.PROJECT_ID, location=self.gv.REGION)
            self.log.info(f"Created bucket {new.name} in {new.location} with storage class {new.storage_class}")  
        
    
    def download(self, dataset_name):
        self.log.info("under contruction")
    
    
    def upload(self, bucket_name):
        self.log.info("under contruction")
    
    
    ###
    
    def read(self, bucket_name): #TFRecord format
        self.log.info("under contruction")
    
    
    def create_dev_dataset_metadata(self, bucket_name, start_idx, end_idx):
        bucket = self.client.get_bucket(bucket_name)
        metadata_list = self._get_dataset_metadata(bucket)
        
        blob = Blob(self.gv.DEV_DATASET_METADATA_NAME, self.client.get_bucket(bucket_name))
        blob.upload_from_string(json.dumps(metadata_list[start_idx:end_idx]))
        
        
    #dataset_begin_idx는 raw dataset source가 다른 것을 적용하는 시점에는 반듯이 삭제해야 함 
    def read_and_split(self, bucket_name, dataset_bucket_idx, data_split): #TFRecord format : storing a sequence of binary records
        test_set = []
        train_val_set = []
        
        bucket = self.client.get_bucket(bucket_name)
        metadata_list = self._get_dataset_metadata(bucket)
        
        print(f"bucket_name={bucket_name}")
        
        for metadata in metadata_list:
            blob = bucket.blob(metadata[self.gv.DATASET_METADATA_KEY_SOURCE_REF]) 
            with blob.open("rb") as f:
                image_bytes = f.read()

            blob = bucket.blob(metadata[self.gv.DATASET_METADATA_KEY_LABEL_REF])
            with blob.open("rb") as f:
                label_bytes = f.read()

            if metadata[self.gv.DATASET_METADATA_KEY_DATA_TYPE] == 'train':
                train_val_set.append(self._make_example_image(image_bytes, label_bytes))
            else:
                test_set.append(self._make_example_image(image_bytes, label_bytes))

        train_set, val_set = train_test_split(train_val_set,
                                              test_size=data_split[1], 
                                              train_size=data_split[0], 
                                              shuffle=False)
        
        return train_set, val_set, test_set
    
    
    def write_dataset_count(self, path, count): ############# 수정필요
        print(f"dataset_len = {count}")
        data = []
        data.append(self._make_example_metadata('count', count))
        self.write(path+"_"+self.gv.DATASET_METADATA_NAME, data)
            
    
    def write(self, path, dataset):  #TFRecord format
        print(f"write_path={path}")
        with tf.io.TFRecordWriter(path, self.gv.DATASET_COMPRESS_TYPE) as writer:
            for tf_example in dataset:
                writer.write(tf_example.SerializeToString())
                
    
    def read_images(self, path):# -> images, count:  #TFRecord format
        image_dataset = tf.data.TFRecordDataset(path, self.gv.DATASET_COMPRESS_TYPE)
        assert isinstance(image_dataset, tf.data.Dataset)
        parsed_image_dataset = image_dataset.map(self._parse_image_function, num_parallel_calls=tf.data.experimental.AUTOTUNE)
                                      
        image_count = tf.data.TFRecordDataset(path+"_"+self.gv.DATASET_METADATA_NAME, self.gv.DATASET_COMPRESS_TYPE)
        assert isinstance(image_count, tf.data.Dataset)
        parsed_image_count = image_count.map(self._parse_image_count_function, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        
        count = [image_count['count'].numpy() for image_count in parsed_image_count]
        return parsed_image_dataset, count[0]
                
        
    def augmente_image(self, parsed_image_dataset, augmente_type):
        train_aug_set = []
        for image_features in parsed_image_dataset:
            img = image_features['image']
            segment_mask = image_features['segmentation_mask']

            train_aug_set.append(self._make_example_image(img, segment_mask))

            image_aug, segment_mask_img_aug = self._augmentation(tf.io.decode_image(img, channels=3), tf.io.decode_png(segment_mask, channels=1), augmente_type)
            train_aug_set.append(self._make_example_image(tf.io.encode_jpeg(image_aug), tf.io.encode_png(segment_mask_img_aug)))
            
        return train_aug_set


    def merge_image_dataset(self, dataset_paths):
        self.log.info(f"merge dataset {dataset_paths[0]} and {dataset_paths[1]}")
        
        dataset1, count = self.read_images(dataset_paths[0])
        print(f"dataset1={dataset1}, {count}\n\n")
        dataset2, count = self.read_images(dataset_paths[1])
        print(f"dataset2={dataset2}, {count}\n\n")
        dataset = dataset1.concatenate(dataset2)
        print(f"dataset_concatenate={dataset}\n\n")
        # dataset = pd.merge(dataset, dataset_append)
        # print(f"dataset_concatenate={dataset}\n\n")
        
       
        data_set = [] 
        for image in dataset:
            data_set.append(self._make_example_image(image['image'], image['segmentation_mask']))
            
        return data_set
       
        

# Cloud와 독립되도록 보완하자 => Module 분리
# Download, Upload to GCS
class TensorflowDatasetMgmt(MiddleDatasetMgmt):
    
    def download(self, dataset_name):
        self.dataset = tfds.load(dataset_name, with_info=False)
    
    
    def upload(self, bucket_name):
        self.bucket_name = bucket_name
        
        dataset_label = self.__upload_dataset_to_bucket(self.dataset['train'], 'train')
        dataset_label.extend(self.__upload_dataset_to_bucket(self.dataset['test'], 'test'))
        self.__upload_dataset_label_to_bucket(dataset_label)
    
    
    # {
    #   "source-ref": "original/train/image/Sphynx_158.jpg",
    #   "label-ref": "original/train/label/Sphynx_158.png",
    #   "data-type": "train"
    # },
    def __upload_dataset_to_bucket(self, dataset, data_type_name):
        dataset_label = []
        bucket = self.client.get_bucket(self.bucket_name)
      
        data_iterator = dataset.as_numpy_iterator()
        for idx, data in enumerate(data_iterator):
            # if self.gv.DEV_MODE and self.gv.DEV_MODE_DATASET_SIZE == idx:
            #     break
            
            f_name = data['file_name'].decode('utf-8')
            
            image = data['image']
            label = data['segmentation_mask']

            blob = Blob(f"original/{data_type_name}/image/{f_name}", bucket)
            blob.upload_from_file(BytesIO(cv.imencode('.jpg', image)[1]))

            blob = Blob(f"original/{data_type_name}/label/{os.path.splitext(f_name)[0]}.png", bucket)
            blob.upload_from_file(BytesIO(cv.imencode('.png', label)[1]))

            dataset_label.append({'source-ref': f"original/{data_type_name}/image/{f_name}", 
                                 'label-ref': f"original/{data_type_name}/label/{os.path.splitext(f_name)[0]}.png", 
                                 'data-type': data_type_name})

        return dataset_label
    
    
    def __upload_dataset_label_to_bucket(self, dataset_label): 
        blob = Blob(self.gv.DATASET_METADATA_NAME, self.client.get_bucket(self.bucket_name))
        blob.upload_from_string(json.dumps(dataset_label))
        
        

# Download, Upload to GCS   
class COCODatasetMgmt(MiddleDatasetMgmt):
    
    def download(self, dataset_name):
        self.log.info("under contruction")
    
    
    def upload(self, bucket_name):
        self.bucket_name = bucket_name
        self.log.info("under contruction")
    
    
    def __upload_dataset_to_bucket(self, dataset, data_type_name):
        self.log.info("under contruction")
        
        
    def __upload_dataset_label_to_bucket(self, dataset_list): 
        self.log.info("under contruction")
    