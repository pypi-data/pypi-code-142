import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)


if True:
    from alphafed.auto_ml import from_pretrained
    from alphafed.auto_ml.breast_density_classification.auto import \
        BreastDensityClassificationFamily
    from alphafed.examples.auto_ml.breast_density_classification import (
        DATA_OWNER_5_ID, DEV_TASK_ID)


if __name__ == '__main__':
    auto_model = from_pretrained(
        name=BreastDensityClassificationFamily.BREAST_DENSITY_CLASSIFICATION_FED_AVG,
        meta_data={
            "lr": 0.001,
            "name": "breast_density_classification_fed_avg",
            "epochs": 1,
            "version": 1,
            "batch_size": 8,
            "input_meta": {
                "data_type": "Image",
                "image_size": [
                    299,
                    299
                ]
            },
            "model_file": "inception3.py",
            "module_dir": None,
            "param_file": "inception3.pt",
            "model_class": "Inception3"
        },
        resource_dir=os.path.join(CURRENT_DIR, 'res')
    )
    auto_model.fine_tune(id=DATA_OWNER_5_ID,
                         task_id=DEV_TASK_ID,
                         dataset_dir=os.path.join(CURRENT_DIR, 'data'))
