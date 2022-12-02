from datetime import datetime
from enum import Enum, auto

class GlobalVariable(): 
    
    class eCLOUD_TYPE(Enum):
        GCP = auto()
        AWS = auto()
        AZURE = auto()
        

    class eDATASET_SOURCE_TYPE(Enum):
        TENSRORFLOW = auto()
        COCO = auto()

        
    class eDEEPLEARNING_FRAMEWORK_TYPE(Enum):
        TENSRORFLOW = auto()
        PYTORCH = auto()


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)  
        return cls._instance
    
    
    def __init__(self, project, account):
        cls = type(self)
        if not hasattr(cls, "_init"):
            self.PROJECT_ID = project
            self.SERVICE_ACCOUNT_ID = account
            self.COMPONENT_CONTAINER_URI = f"{self._CONTAINER_URI_PREFIX}/{self.PROJECT_ID}/{self._COMPONENT_CONTAINER_URI_POSTFIX}"
            self.TRAIN_CONTAINER_URI = f"{self._CONTAINER_URI_PREFIX}/{self.PROJECT_ID}/{self._TRAIN_CONTAINER_URI_POSTFIX}"
            self.SERVING_CONTAINER_URI = f"{self._CONTAINER_URI_PREFIX}/{self.PROJECT_ID}/{self._SERVING_CONTAINER_URI_POSTFIX}"
            cls._init = True
            
            print(f"PROJECT_ID={self.PROJECT_ID}")
            print(f"SERVICE_ACCOUNT_ID={self.SERVICE_ACCOUNT_ID}")
            print(f"COMPONENT_CONTAINER_URI={self.COMPONENT_CONTAINER_URI}")
            print(f"TRAIN_CONTAINER_URI={self.TRAIN_CONTAINER_URI}")
            print(f"SERVING_CONTAINER_URI={self.SERVING_CONTAINER_URI}")
    
    
    VERSION = "0.0.3"
    PROJECT_ID = ""
    SERVICE_ACCOUNT_ID = ""
    
    #############
    TIMESTAMP = datetime.now().strftime('%m%d%Y-%H%M%S')
    LOGGER_NAME = "vertex-ai-rokit-tutorial-logger"

    #############
    REGION = 'us-central1'
    #BUCKET = 'vertex_ai_rokit_tutorial_lsm' #BUCKET => PIPELINE_BUCKET
    PIPELINE_BUCKET = 'vertex_ai_rokit_tutorial_lsm' #BUCKET => PIPELINE_BUCKET #stagin_bucket
    #BUCKET_NAME = f"gs://{BUCKET}"  #BUCKET_NAME => PIPELINE_BUCKET_PATH
    PIPELINE_BUCKET_PATH = f"gs://{PIPELINE_BUCKET}"
    PIPELINE_BUCKET_STAGING_PATH = PIPELINE_BUCKET_PATH + "/stage/"
    
    #BUCKET_PROJECT_PATH = PIPELINE_BUCKET_PATH
    
    
    
    IMG_DATASET_FEATURE_NAME = ("image", "segmentation_mask")
    

    #############
    PIPELINE_NAME = "vertex-ai-tutorial-pipeline-lsm"
    PIPELINE_ROOT = f"{PIPELINE_BUCKET_PATH}/{PIPELINE_NAME}"
    PIPELINE_DISPLAY_NAME = f"{PIPELINE_NAME}-{TIMESTAMP}"
    
    PIPELINE_FOLDER = "pipelines"
    PIPELINE_TEMPLATE_PATH = f"{PIPELINE_BUCKET_PATH}/{PIPELINE_FOLDER}/{PIPELINE_NAME}.json"

    #############
    MODEL_DISPLAY_NAME = "vertex-ai-tutorial"
    DOCKER_REPOSITORY_NAME = MODEL_DISPLAY_NAME
    EXPERIMENT_NAME = MODEL_DISPLAY_NAME + "-experiment"
    TRAIN_NAME = MODEL_DISPLAY_NAME + "-train"  #The user-defined name of this TrainingPipeline
    MODEL_NAME = MODEL_DISPLAY_NAME + "-model"
    ENDPOINT_NAME = MODEL_DISPLAY_NAME + "-endpoint"
    
    #############
    EXPERIMENT_DESCRIPTION = "Pet Segmentation Experiment"
    
    #############
    DATASET_BUCKET = ['oxford_iiit_pet_3_2_0_rgb', 'oxford_iiit_pet_lsm']
    #DATASET_BUCKET = 'oxford_iiit_pet_lsm'

    DATASET_BUCKET2 = 'oxford_iiit_pet_lsm' #'oxford_iiit_pet_3_2_0_rgb'
    #DATASET_BUCKET2 = 'oxford_iiit_pet_lsm2'

    DATASET_COMPRESS_TYPE = 'GZIP'
    DATASET_METADATA_NAME = "metadata.json"
    DATASET_METADATA_KEY_SOURCE_REF = "source-ref"
    DATASET_METADATA_KEY_LABEL_REF = "label-ref"
    DATASET_METADATA_KEY_DATA_TYPE = "data-type"
    
    ############
    COMPONENT_CONTAINER_IMAGE_NAME = "vertex-ai-custom-component"
    TRAIN_CONTAINER_IMAGE_NAME = "vertex-ai-custom-train"
    DEPLOY_CONTAINER_IMAGE_NAME = "vertex-ai-custom-deploy"

    _CONTAINER_URI_PREFIX = f"{REGION}-docker.pkg.dev"
    _COMPONENT_CONTAINER_URI_POSTFIX = f"{DOCKER_REPOSITORY_NAME}/{COMPONENT_CONTAINER_IMAGE_NAME}"
    _TRAIN_CONTAINER_URI_POSTFIX = f"{DOCKER_REPOSITORY_NAME}/{TRAIN_CONTAINER_IMAGE_NAME}"
    _SERVING_CONTAINER_URI_POSTFIX = f"{DOCKER_REPOSITORY_NAME}/{DEPLOY_CONTAINER_IMAGE_NAME}"
    
    COMPONENT_CONTAINER_URI = ""
    TRAIN_CONTAINER_URI = ""
    SERVING_CONTAINER_URI = ""
    
    SERVING_CONTAINER_PREDICT_ROUTE = "/inference"
    SERVING_CONTAINER_HEALTH_ROUTE = "/health"
    SERVING_CONTAINER_ENVIRONMENT_VARIABLES = {"PORT": "8080"}
    SERVING_CONTAINER_PORTS = [8080]
    
    #############
    # MACHINE_TYPE = "n1-standard-4"
    # REPLICA_COUNT = 1
    # ACCELERATOR_TYPE = 'NVIDIA_TESLA_P4'
    # ACCELERATOR_COUNT = 1
    
    #############Train Parameter
    DATASET_SIZE = 1#1000
    DATASET_SPLIT = [0.9, 0.1] #[0.8, 0.2]
    DATASET_SPLIT_RANDOM_SEED = 0
    
    
    TRAIN_OUTPUT_CLASS = 3
    TRAIN_BATCH_SIZE = 64
    TRAIN_BUFFER_SIZE = 1000
    TRAIN_EPOCHS = 20 #os.environ["_EPOCHS"] #30
    TRAIN_VAL_SUBSPLITS = 5 #os.environ["VAL_SUBSPLITS"] #5 

    # TRAIN_LENGTH = info.splits['train'].num_examples
    # STEPS_PER_EPOCH_S = TRAIN_LENGTH // BATCH_SIZE

    # _TRAIN_LENGTH = int(_DATASET_SIZE * _DATA_SPLIT[0])
    # _VALIDATION_LENGTH = int(_DATASET_SIZE * _DATA_SPLIT[1])
    TRAIN_MODEL_NAME = "U-NET"

    # ##############
    BATCH_PREDICTION_FLAG = False
    
    
    ################
    # For TEST
    LOCAL_EXEC = 1
    PACKAGE_INSTALL_MODE = 1
    DEV_MODE = 1 # 1 / 0
    DEV_DATASET_METADATA_NAME = "metadata_dev.json" 
    DEV_MODE_DATASET_SIZE = 100


    ################
    TRAIN_REPLICA_COUNT = 1
    TRAIN_MACHINE_TYPE = "n1-standard-4"
    TRAIN_ACCELERATOR_TYPE = "NVIDIA_TESLA_P4"
    TRAIN_ACCELERATOR_COUNT = 1
    TRAIN_SYNC = True
    
    VALIDATE_REPLICA_COUNT = 1
    VALIDATE_MACHINE_TYPE = "n1-standard-4"
    VALIDATE_ACCELERATOR_TYPE = "NVIDIA_TESLA_P4"
    VALIDATE_ACCELERATOR_COUNT = 1
    VALIDATE_SYNC = True
    
    DEPLOY_REPLICA_COUNT = 1
    DEPLOY_MACHINE_TYPE = "n1-standard-4"
    DEPLOY_ACCELERATOR_TYPE = "NVIDIA_TESLA_P4"
    DEPLOY_ACCELERATOR_COUNT = 1
    DEPLOY_SYNC = True