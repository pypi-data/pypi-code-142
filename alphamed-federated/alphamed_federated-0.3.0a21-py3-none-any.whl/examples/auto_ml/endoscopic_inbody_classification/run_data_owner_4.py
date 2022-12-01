import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)


if True:
    from alphafed.auto_ml import from_pretrained
    from alphafed.auto_ml.endoscopic_inbody_classification.auto import \
        EndoscopicInbodyClassificationFamily
    from alphafed.examples.auto_ml.endoscopic_inbody_classification import (
        DATA_OWNER_4_ID, DEV_TASK_ID)


if __name__ == '__main__':
    auto_model = from_pretrained(
        name=EndoscopicInbodyClassificationFamily.ENDOSCOPIC_INBODY_CLASSIFICATION_FED_AVG,
        meta_data={
            "lr": 0.001,
            "name": 'endoscopic_inbody_classification_fed_avg',
            "epochs": 20,
            "version": 1,
            "batch_size": 8,
            "input_meta": {
                "data_type": "Image",
                "image_size": [
                    256,
                    256
                ]
            },
            "model_file": None,
            "module_dir": "senet",
            "param_file": "se_resnet50.pth",
            "model_class": "SEResNet50"
        },
        resource_dir=os.path.join(CURRENT_DIR, 'res')
    )
    auto_model.fine_tune(id=DATA_OWNER_4_ID,
                         task_id=DEV_TASK_ID,
                         dataset_dir=os.path.join(CURRENT_DIR, 'data'))
