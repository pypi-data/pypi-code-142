import os
import sys
from abc import *

from .. import global_variable as gv

#GCP, AWS 등 Cloud storage가 대상
#bucket 생성
#dataset loading
#save dataset to gcs
#save meta to blob 


# pipeline
# PROJECT_ID -> REGION -> PIPELINE_ROOT (PIPELINE_BUCKET_PATH / PIPELINE_NAME) / ID / PIPELINE_DISPLAY_NAME / Pipeline Output
# ex) gs://vertex_ai_rokit_tutorial_lsm/vertex-ai-tutorial-pipeline-lsm/1064916457437/vertex-ai-tutorial-pipeline-lsm-20221110071809/oxford-iiit-pet-load_4365227738282328064
# 
# PROJECT_ID -> REGION -> PIPELINE_TEMPLATE_PATH (PIPELINE_BUCKET_PATH / PIPELINE_FOLDER / PIPELINE_NAME.json)
# ex) vertex_ai_rokit_tutorial_lsm/pipelines/vertex-ai-tutorial-pipeline-lsm.json


# dataset source
# PROJECT_ID -> REGION -> gs://DATASET_BUCKET / original / train / image / file_name.jpg ...
# PROJECT_ID -> REGION -> gs://DATASET_BUCKET / original / train / label / file_name.png ...
# PROJECT_ID -> REGION -> gs://DATASET_BUCKET / original / test / image / file_name.jpg ...
# PROJECT_ID -> REGION -> gs://DATASET_BUCKET / original / test / label / file_name.png ...
# PROJECT_ID -> REGION -> gs://DATASET_BUCKET / label.json
# 
# ex) gs://oxford_iiit_pet_3_2_0/original/train/image/Abyssinian_1.jpg
# 
# label.json : image uri info
# [
#   {
#     "source-ref": "original/train/image/Sphynx_158.jpg",
#     "label-ref": "original/train/label/Sphynx_158.png",
#     "data-type": "train"
#   },

    
class DatasetMgmt(metaclass=ABCMeta):
    def __init__(self, global_variable, log):
        self.gv = global_variable
        self.log = log
    
    @abstractmethod
    def make_bucket(self, bucket_name):
        pass
    
    @abstractmethod
    def download(self, dataset_name):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def upload(self, bucket_name):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass

    @abstractmethod
    def read(self, bucket_name): 
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass

    @abstractmethod
    def read_and_split(self, bucket_name, dataset_bucket_idx, data_split):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def write_dataset_count(self, path, count):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
        
    @abstractmethod
    def write(self, path, dataset): 
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def read_images(self, path):# -> images, count: 
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def augmente_image(self, image_dataset, augmente_type):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def merge_image_dataset(self, dataset_paths):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
    
    @abstractmethod
    def create_dev_dataset_metadata(self, bucket_name, start_idx, end_idx):
        self.log.info(f"{sys._getframe(0).f_code.co_name} function called")
        pass
        
    
    
#      #for batch prediction
#     def load_image(datapoint):  
#         input_image = tf.io.decode_image(datapoint['image'], expand_animations = False, channels=3)
#         input_mask = tf.io.decode_png(datapoint['segmentation_mask'], channels=1)

#         input_image = tf.image.resize(input_image, (128, 128))
#         input_mask = tf.image.resize(input_mask, (128, 128))     
        
#         return input_image, input_mask    
    

#     def dataset2jsonl(x_images, path):
#         path = os.path.split(path)[0] #PIPELINE_BUCKET_PATH
#         BATCH_PREDICTION_INSTANCES_FILE = "batch_prediction_instances.jsonl"
#         BATCH_PREDICTION_GCS_SOURCE = (
#             path + "/batch_prediction_instances/" + BATCH_PREDICTION_INSTANCES_FILE
#         )

#         log.info(f"BATCH_PREDICTION_INSTANCES_FILE = {BATCH_PREDICTION_INSTANCES_FILE}")
#         log.info(f"BATCH_PREDICTION_GCS_SOURCE = {BATCH_PREDICTION_GCS_SOURCE}")

#         # Write instances at JSONL
#         with open(BATCH_PREDICTION_INSTANCES_FILE, "w") as f:
#             x_test = [np.asarray(image[0]).astype(np.float32).tolist() for image in x_images]
#             for x in x_test:
#                 f.write(json.dumps(x) + "\n")

#         # Upload to Cloud Storage bucket
#         !gsutil cp $BATCH_PREDICTION_INSTANCES_FILE $BATCH_PREDICTION_GCS_SOURCE
#         log.info(f"Uploaded instances to: {BATCH_PREDICTION_GCS_SOURCE}")
        
      
#     def batch_prediction_input_make(dataset_path):
#         dataset = tf.data.TFRecordDataset(dataset_path, dataset_compression_type).map(_parse_image_function, num_parallel_calls=tf.data.experimental.AUTOTUNE)
#         dataset = dataset.map(load_image, num_parallel_calls=tf.data.experimental.AUTOTUNE)         
#         dataset2jsonl(dataset, dataset_path) 
        