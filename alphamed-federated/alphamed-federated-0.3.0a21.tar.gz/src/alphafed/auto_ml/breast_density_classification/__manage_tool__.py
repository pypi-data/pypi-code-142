import json
import os
import sys

import requests

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_PATH = os.path.join(CURRENT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.insert(0, PYTHON_PATH)

if True:
    from alphafed.auto_ml.auto_model import DataType, TaskMode, TaskType
    from alphafed.auto_ml.breast_density_classification.auto import \
        BreastDensityClassificationFamily


# url = 'http://localhost:8000/alphamed-modelzoo/manage/pretrained'  # dev
# url = 'https://service.sspedu.cn/alphamed-modelzoo/manage/pretrained'  # test
url = 'https://service-prod.sspedu.cn/alphamed-modelzoo/manage/pretrained'  # prod
headers = {
    'content-type': 'application/json',
    'x-token': 'FxvCl1ihqb2VPQf393yinmjRV4aPYudN'
}


def upload_local():
    name = BreastDensityClassificationFamily.BREAST_DENSITY_CLASSIFICATION
    version = 1
    meta_json = {
        "lr": 0.001,
        "name": name,
        "epochs": 50,
        "version": version,
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
        "param_file": "inception3.pth",
        "model_class": "Inception3"
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/breast_density_classification.zip'
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
    name = BreastDensityClassificationFamily.BREAST_DENSITY_CLASSIFICATION
    version = 1
    meta_json = {
        "lr": 0.001,
        "name": name,
        "epochs": 50,
        "version": version,
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
        "param_file": "inception3.pth",
        "model_class": "Inception3"
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/breast_density_classification.zip'
    put_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
            'display_name': 'Breast Density Classification',
            'summary': '乳腺密度分类',
            'desc': '待补充 ...',
            'author': 'NVIDIA',
            'github_link': 'https://github.com/Project-MONAI/model-zoo/tree/dev/models/breast_density_classification',
            'license': 'Apache Software License 2.0',
            'reference': 'https://arxiv.org/abs/2202.08238'
        },
    }
    return requests.put(url=url, json=put_json, headers=headers)


def upload_fed_avg():
    name = BreastDensityClassificationFamily.BREAST_DENSITY_CLASSIFICATION_FED_AVG
    version = 1
    meta_json = {
        "lr": 0.001,
        "name": name,
        "epochs": 50,
        "version": version,
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
        "param_file": "inception3.pth",
        "model_class": "Inception3"
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/breast_density_classification.zip'
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
    name = BreastDensityClassificationFamily.BREAST_DENSITY_CLASSIFICATION_FED_AVG
    version = 1
    meta_json = {
        "lr": 0.001,
        "name": name,
        "epochs": 50,
        "version": version,
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
        "param_file": "inception3.pth",
        "model_class": "Inception3"
    }
    pkg = 'https://dev-sapce-1309103037.cos.ap-nanjing.myqcloud.com/tmp/breast_density_classification.zip'
    put_json = {
        'pretrained': {
            'name': name,
            'version': version,
            'meta': meta_json,
            'pkg': pkg,
            'display_name': 'Breast Density Classification - FedAvg',
            'summary': '乳腺密度分类-同构数据联邦学习',
            'desc': '待补充 ...',
            'author': 'NVIDIA',
            'github_link': 'https://github.com/Project-MONAI/model-zoo/tree/dev/models/breast_density_classification',
            'license': 'Apache Software License 2.0',
            'reference': 'https://arxiv.org/abs/2202.08238'
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
