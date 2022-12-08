import logging
import json

from outliers.utils.data import create_data
from .detectors.detection_models import DetectionModels
from .detectors import pipelines
from .definitions import MODEL_CONFIG_PATH


if __name__ == "__main__":
    data = create_data()
    logging.info("Reading in models")
    models = DetectionModels(MODEL_CONFIG_PATH).get_models()
    logging.info("iterating over models")
    for model in models:
        logging.info("Create detector")
        detector = pipelines.OutlierDetector(model=model)
        logging.info("Detector created")
        result = detector.detect(data)
        logging.info("Result calculated")
        result = json.dumps({'results':result.tolist()})
        
        with open('target.json', 'w') as f:
            f.write(result)
