import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHONPATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHONPATH)


if True:
    from alphafed.auto_ml import from_pretrained
    from alphafed.auto_ml.skin_lesion_diagnosis.auto import \
        SkinLesionDiagnosisFamily
    from alphafed.examples.auto_ml.skin_lesion_diagnosis import (AGGREGATOR_ID,
                                                                 DEV_TASK_ID)


if __name__ == '__main__':
    auto_model = from_pretrained(
        name=SkinLesionDiagnosisFamily.SKIN_LESION_DIAGNOSIS_FED_AVG,
        meta_data={
            "lr": 1e-4,
            "name": "skin_lesion_diagnosis_fed_avg",
            "epochs": 1,
            "version": 1,
            "batch_size": 8,
            "input_meta": {
                "data_type": "Image",
                "image_size": [
                    224,
                    224
                ]
            },
            "model_file": "res_net.py",
            "module_dir": None,
            "param_file": "resnet18.pth",
            "model_class": "ResNet18"
        },
        resource_dir=os.path.join(CURRENT_DIR, 'res')
    )
    auto_model.fine_tune(id=AGGREGATOR_ID,
                         task_id=DEV_TASK_ID,
                         dataset_dir=os.path.join(CURRENT_DIR, 'data'),
                         is_initiator=True)
