import json
import os
import sys

import requests

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_PATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHON_PATH)

if True:
    from alphafed.auto_ml.auto_model import DataType, TaskMode, TaskType
    from alphafed.auto_ml.skin_lesion_diagnosis.auto import \
        SkinLesionDiagnosisFamily


# url = 'http://localhost:8000/alphamed-modelzoo/manage/pretrained'  # dev
url = 'https://service.sspedu.cn/alphamed-modelzoo/manage/pretrained'  # test
url = 'https://service-prod.sspedu.cn/alphamed-modelzoo/manage/pretrained'  # prod
headers = {
    'content-type': 'application/json',
    'x-token': 'FxvCl1ihqb2VPQf393yinmjRV4aPYudN'
}


def upload_local():
    name = SkinLesionDiagnosisFamily.SKIN_LESION_DIAGNOSIS
    version = 1
    meta_json = {
        "lr": 1e-4,
        "name": "skin_lesion_diagnosis",
        "epochs": 20,
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
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/resnet18.zip'
    data_type = DataType.IMAGE
    task_type = TaskType.MEDICINE
    task_mode = TaskMode.LOCAL
    post_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
        },
        'data_type': data_type,
        'task_type': task_type,
        'task_mode': task_mode
    }
    return requests.post(url=url, json=post_json, headers=headers)


def update_local():
    name = SkinLesionDiagnosisFamily.SKIN_LESION_DIAGNOSIS
    version = 1
    meta_json = {
        "lr": 1e-4,
        "name": "skin_lesion_diagnosis",
        "epochs": 20,
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
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/resnet18.zip'
    put_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
            'display_name': 'Skin Lesion Diagnosis',
            'summary': '皮肤疾病检测',
            'desc': '待补充 ...',
            'author': 'ssplab',
            'github_link': 'N/A',
            'license': 'Apache Software License 2.0',
            'reference': 'N/A'
        },
    }
    return requests.put(url=url, json=put_json, headers=headers)


def upload_fed_avg():
    name = SkinLesionDiagnosisFamily.SKIN_LESION_DIAGNOSIS_FED_AVG
    version = 1
    meta_json = {
        "lr": 1e-4,
        "name": "skin_lesion_diagnosis_fed_avg",
        "epochs": 20,
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
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/resnet18.zip'
    data_type = DataType.IMAGE
    task_type = TaskType.MEDICINE
    task_mode = TaskMode.FED_AVG
    post_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
        },
        'data_type': data_type,
        'task_type': task_type,
        'task_mode': task_mode
    }
    return requests.post(url=url, json=post_json, headers=headers)


def update_fed_avg():
    name = SkinLesionDiagnosisFamily.SKIN_LESION_DIAGNOSIS_FED_AVG
    version = 1
    meta_json = {
        "lr": 1e-4,
        "name": "skin_lesion_diagnosis_fed_avg",
        "epochs": 20,
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
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/resnet18.zip'
    put_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
            'display_name': 'Skin Lesion Diagnosis - FedAvg',
            'summary': '皮肤疾病检测-同构数据联邦学习',
            'desc': '待补充 ...',
            'author': 'ssplab',
            'github_link': 'N/A',
            'license': 'Apache Software License 2.0',
            'reference': 'N/A'
        }
    }
    return requests.put(url=url, json=put_json, headers=headers)


if __name__ == '__main__':
    # resp = upload_local()
    # resp = update_local()
    # resp = upload_fed_avg()
    resp = update_fed_avg()
    try:
        print(json.dumps(resp.json(), indent=2))
    except Exception:
        print(resp.content)
