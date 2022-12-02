# utf-8
import requests
import json
from tqdm import tqdm
import itertools
from terminaltables import AsciiTable
import os
import argparse
import time

from lvt_eval.utils import check_json, merge_bbox, get_pic_urls, save_json, load_json, chunks, download_img, max_index, draw_box, get_classes_and_imgs
from lvt_eval.tools import coco_error_analysis, cal_precision_and_recall, cal_map

import logging

logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


class StudioJsonEvaluation:

    def __init__(self):
        pass

    def save_predition(self, category, json_result):
        prediction = []
        names = {}
        for cat in category:
            cat_pred = cat["prediction"]
            cat_id = cat['id']
            names.update({cat_id: cat_pred})
            for i in json_result:
                if i["status"] == False:
                    bbox_list = len(i["bbox_list"])
                    for b in range(bbox_list):
                        if i["bbox_list"][b]["status"] == False:  # bbox的status为false，才会报警，故取该框
                            if isinstance(i["bbox_list"][b]["label"], str):  # bbox的label为str格式
                                label = i["bbox_list"][b]["label"]
                            # bbox的label为list格式
                            elif isinstance(i["bbox_list"][b]["label"], list):
                                label = i["bbox_list"][b]["label"][0]
                            if cat_pred == label:
                                image = int(i["id"])
                                score = 0
                                # bbox的conf为float格式
                                if isinstance(i["bbox_list"][b]["conf"],
                                              float):
                                    score = i["bbox_list"][b]["conf"]
                                # bbox的conf为list格式
                                elif isinstance(i["bbox_list"][b]["conf"],
                                                list):
                                    score = i["bbox_list"][b]["conf"][0]
                                bbox = i["bbox_list"][b]["bbox"]
                                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[
                                    2], bbox[3]
                                box = [x1, y1, x2 - x1, y2 - y1]
                                pred = {
                                    "image_id": image,
                                    "category_id": cat_id,
                                    "bbox": box,  # xywh
                                    "score": score
                                }
                                prediction.append(pred)
                            if isinstance(label, int):
                                image = int(i["id"])
                                bbox, score = i["bbox_list"][b]["bbox"], i[
                                    "bbox_list"][b]["conf"]
                                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[
                                    2], bbox[3]
                                box = [x1, y1, x2 - x1, y2 - y1]
                                pred = {
                                    "image_id": image,
                                    "category_id": cat_id,
                                    "bbox": box,
                                    "score": score[0]
                                }
                                prediction.append(pred)
        logging.info("prediction save done.")
        return prediction, names

    def get_perbox(self,
                   urls,
                   res_id,
                   aiport="http://192.1.2.238:8998/vql/v1/serving/process",
                   includeCoincideRatio_name="person",
                   includeCoincideRatio_ratio=0.95,
                   includeCoincideRatio_threshold="0.1",
                   excludeCoincideRatio=[],
                   classesThreshold=0.1,
                   displayAllBboxes=False,
                   displayScore=True,
                   boxEnlargeSize=3.2,
                   bigModelQueryPositive=[],
                   bigModelQueryNegative=[],
                   bigModelExcludeCoincideRatio=[],
                   bigModelIncludeCoincideRatio=[]):
        logging.info("success start get_perbox")
        src = []
        plaod = {
            "taskId": "123",
            # "schedulingCenter": {"linker_ai_debug_flag": "debug_mode_activate"},  # debug使用的
            "schedulingCenter": {
                "checkServingDto": {
                    "url":
                    "CiSUryUCfpgbUdjrJeKQ61Jc8CcPboONkbF9ctWWsZUalU3FIfi/sY+xzFXwLtyoGVrmu+/JDnA=\n"
                }
            },
            "tasks": [],
            "src": src,
            # 下面的显示报警图片默认注释掉，需要再解除注释
            "dest": [],
            "callback": "123",
            "kwargs": {}
        }

        for id, url in enumerate(tqdm(urls)):
            src_info = {
                "imageId": id + res_id,
                "data": url,
                "selectedRegions": [],
                "videoValidation": "346",
                "abilityCode": "target_detection",
                "eventTime": time.strftime("%Y-%m-%d %H:%M:%S",
                                           time.localtime()),
                "kwargs": {
                    "startTime":
                    "00:00:00",
                    "interval":
                    15,
                    "endTime":
                    "23:59:00",
                    "isStart":
                    False,
                    "isEnd":
                    False,
                    "includeCoincideRatio": [{
                        "name":
                        includeCoincideRatio_name,
                        "ratio":
                        includeCoincideRatio_ratio,
                        "threshold":
                        includeCoincideRatio_threshold
                    }],
                    "excludeCoincideRatio":
                    excludeCoincideRatio,
                    "classesThreshold":
                    classesThreshold,
                    "displayAllBboxes":
                    displayAllBboxes,
                    "displayScore":
                    displayScore,
                    "boxEnlargeSize":
                    boxEnlargeSize,
                    "bigModelQueryPositive":
                    bigModelQueryPositive,
                    "bigModelQueryNegative":
                    bigModelQueryNegative,
                    "bigModelExcludeCoincideRatio":
                    bigModelExcludeCoincideRatio,
                    "bigModelIncludeCoincideRatio":
                    bigModelIncludeCoincideRatio
                },
                "videoId": "1780",
                "srcType": "url"
            }
            src.append(src_info)
        # save_json(plaod, "./prediction_dirs/plaod.json")
        result = requests.post(aiport, json=plaod).text
        json_result = json.loads(result)
        logging.info("success end get_perbox")
        if json_result['code'] == 200:
            return json_result
        else:
            logging.info({
                "错误信息返回": {
                    "status": "fail",
                    "message": "Connection refused"
                }
            })
            return []

    # 从studio_json中提取coco格式的groundtruth
    def get_groundtruth(self, raw_data, label, download_image=True):
        gt = {
            "info": {},
            "licenses": {},
            "images": list,
            "annotations": list,
            "categories": list
        }
        images, annotations, categories = [], [], []
        k = 0
        # ===============================add categories
        for ll in label:
            obj_mapping, at_mapping, lab_id = ll["objectLabel"], ll["attrLabel"], ll["id"]

            if isinstance(obj_mapping, list):  # 若objectLabel包含多个目标
                if at_mapping == [] or at_mapping == [""]:  # attrLabel没有包含任何属性
                    cat = {
                        "supercategory": ",".join(obj_mapping),
                        "id": lab_id,
                        "name": ",".join(obj_mapping),
                    }
                else:  # attrLabel包含多个属性
                    cat = {
                        "supercategory": ",".join(obj_mapping) + '-' + ",".join(at_mapping),
                        "id": lab_id,
                        "name": ",".join(obj_mapping) + '-' + ",".join(at_mapping),
                    }
            categories.append(cat)

        image_id_mapping = {}
        # ============================add images
        for i in tqdm(raw_data):
            if i["marked"] in [0, 1, 2, 3]:
                img = {
                    "license": 0,
                    "file_name": i["url"],
                    "coco_url": i["url"],
                    "height": i["height"],
                    "width": i["width"],
                    "depth": 3,
                    "id": i["id"]
                }
                images.append(img)

                if download_image == True:
                    download_img(i['url'])  # 下载图片

                image_id_mapping[i["id"]] = i['url'].split('/')[-1]

                # ============================add annotations
                for l in label:
                    object_mapping, attr_mapping, label_id = l["objectLabel"], l["attrLabel"], l["id"]
                    for j in i["markData"]:
                        if j["objLabel"][0]["name"] in object_mapping and (
                                attr_mapping != [] and attr_mapping != [""]):
                            if len(j["attrLabel"]) != 0:
                                for a in range(len(j["attrLabel"])):
                                    if j["attrLabel"][a]["name"] in attr_mapping:
                                        x1, y1 = float(j["mouseFrom"]["x"]), float(
                                            j["mouseFrom"]["y"])
                                        x2, y2 = float(j["mouseTo"]["x"]), float(
                                            j["mouseTo"]["y"])

                                        w, h = x2 - x1, y2 - y1
                                        bbox = [x1, y1, w, h]
                                        ann = {
                                            "segmentation": [[]],
                                            "image_id": i["id"],
                                            "bbox": bbox,
                                            "category_id": label_id,
                                            "id": k,
                                            "iscrowd": 0,
                                            "area": w * h
                                        }
                                        annotations.append(ann)
                                        k += 1

                        elif j["objLabel"][0]["name"] in object_mapping and (
                                attr_mapping == [] or attr_mapping == [""]):

                            x1, y1 = float(j["mouseFrom"]["x"]), float(
                                j["mouseFrom"]["y"])
                            x2, y2 = float(j["mouseTo"]["x"]), float(
                                j["mouseTo"]["y"])
                            w, h = x2 - x1, y2 - y1
                            bbox = [x1, y1, w, h]
                            ann = {
                                "segmentation": [[]],
                                "image_id": i["id"],
                                "bbox": bbox,
                                "category_id": label_id,
                                "id": k,
                                "iscrowd": 0,
                                "area": w * h
                            }
                            annotations.append(ann)
                            k += 1

        gt["images"] = images
        gt["annotations"] = annotations
        gt["categories"] = categories

        save_json(image_id_mapping,
                  'mapping_dirs/studio_image_id_mapping.json')
        logging.info("Save groundtruth done.")
        return gt

    def indicator(self,
                  config_path,
                  thresholds=[0.0, 0.1]):
        config = load_json(config_path)

        aiport, data_path, download, drawbox = config.get(
            'aiport'), config.get('rawdata'), config.get(
                'download'), config.get('draw')
        raw_prediction_path, save_gt_path, save_pred_path = config.get(
            'raw_prediction_path'), config.get('save_gt_coco'), config.get(
                'save_pred_path')

        urls, rawdata = get_pic_urls(data_path)
        len_urls = len(urls)
        labels = config.get('label')
        fin_res = []
        bak_id, res_id = 0, 0

        if os.path.exists(raw_prediction_path):
            pred_bak = load_json(raw_prediction_path)
            bak_id = int(pred_bak[-1]["id"])
            fin_res = pred_bak
            res_id = bak_id + 1
        if len_urls != res_id:
            # --------------调用aiport-------start
            logging.info("已经有{}张图片被检测过，从{}开始进行检测".format(bak_id, res_id))
            for imgs in chunks(urls, 100, 100, bak_id):
                if imgs:
                    ress = self.get_perbox(imgs,
                                           res_id,
                                           aiport,
                                           classesThreshold=thresholds[0])
                    if ress != None:
                        res = ress["results"]["1780"]
                        fin_res += res
                        res_id += 100
                        # --------------保存aiport输出的结果
                        save_json(fin_res, raw_prediction_path)
            # --------------调用aiport-------end

        # fin_res = load_json(raw_prediction_path)
        pred_data, pred_name = self.save_predition(labels, fin_res)
        save_json(pred_data, save_pred_path)
        gt_data = self.get_groundtruth(
            rawdata, labels,
            download_image=download)  # 下载图片 download_image=True
        save_json(gt_data, save_gt_path)
        names, classes, _ = get_classes_and_imgs(gt_data)

        metrics = []
        recommend_thres = []
        f1_all = []

        for threshold in thresholds:
            this_metric = {
                "threshold": threshold,
                "metrics": {"labels": []},
            }
            logging.info(
                "+-----------------------------------------------------------------------------------+"
            )
            logging.info('threshold = {}, 开始评估'.format(threshold))

            if gt_data["annotations"] == [] and len(pred_data) == 0:
                logging.info('The model accuracy is 100%, AP = 1.0, AR = 1.0')
                this_metric["metrics"].update({
                    "AP": 1,
                    "AP50": 1,
                    "AP75": 1,
                    "APs": 1,
                    "APm": 1,
                    "APl": 1,
                    "AR_50_95_all_1": 1,
                    "AR_50_95_all_10": 1,
                    "AR_50_95_all_100": 1,
                    "ARs": 1,
                    "ARm": 1,
                    "ARl": 1,
                    "P": 1,
                    "R": 1
                })
                this_metric["metrics"]["labels"] = [
                    {"name": label, "AP": 1, "AR": 1, "P": 1, "R": 1, "AP50": 1, "AR50": 1} for label in classes]

            elif gt_data["annotations"] != [] and len(pred_data) != 0:
                matched_pred_boxes, pred_false_boxes, unmatch_pred_img, _, _ = check_json(
                    pred_data, gt_data, threshold)
                draw_box(gt_data,
                         matched_pred_boxes,
                         data_path.rsplit('/', 2)[-1].split('.')[0],
                         threshold,
                         pred_name,
                         draw=drawbox)  # draw=True 画框

                if matched_pred_boxes == [] and pred_false_boxes == []:
                    this_metric["metrics"].update({
                        "AP": 1,
                        "AP50": 1,
                        "AP75": 1,
                        "APs": 1,
                        "APm": 1,
                        "APl": 1,
                        "AR_50_95_all_1": 1,
                        "AR_50_95_all_10": 1,
                        "AR_50_95_all_100": 1,
                        "ARs": 1,
                        "ARm": 1,
                        "ARl": 1,
                        "P": 1,
                        "R": 1
                    })
                    this_metric["metrics"]["labels"] = [
                        {"name": label, "AP": 1, "AR": 1, "P": 1, "R": 1, "AP50": 1, "AR50": 1} for label in classes]

                elif matched_pred_boxes or (matched_pred_boxes
                                            and pred_false_boxes):

                    results_per_category_iou50 = []
                    a_metrics = cal_map(
                        gt_data, matched_pred_boxes)

                    pr_results = cal_precision_and_recall(
                        gt_data, matched_pred_boxes, names, len(names))

                    # F1用于表示P、R的综合值，找到最大的F1即为推荐置信度
                    f1_all.append(pr_results['all'][-1])

                    this_metric["metrics"].update({
                        "AP": a_metrics["AP"],
                        "AP50": a_metrics["AP50"],
                        "AP75": a_metrics["AP75"],
                        "APs": a_metrics["APs"],
                        "APm": a_metrics["APm"],
                        "APl": a_metrics["APl"],
                        "AR_50_95_all_1": a_metrics["AR_50_95_all_1"],
                        "AR_50_95_all_10": a_metrics["AR_50_95_all_10"],
                        "AR_50_95_all_100": a_metrics["AR_50_95_all_100"],
                        "ARs": a_metrics["ARs"],
                        "ARm": a_metrics["ARm"],
                        "ARl": a_metrics["ARl"],
                        "P": pr_results['all'][2],
                        "R": pr_results['all'][3]
                    })
                    if len(classes) != 1:
                        for label in classes:
                            lab = {
                                "name": label,
                                "AP": a_metrics['AP-' + label],
                                "AR": a_metrics['AR-' + label],
                                "P": pr_results[label][2],
                                "R": pr_results[label][3],
                                "AP50": a_metrics['AP-50-' + label],
                                "AR50": a_metrics['AR-50-' + label]
                            }
                            this_metric["metrics"]["labels"].append(lab)
                            false_50 = 1 - lab["AR50"]
                            res_item = [
                                f'{label}', f'{lab["AP50"]:0.3f}', f'{lab["AR50"]:0.3f}',
                                f'{float(false_50):0.3f}']
                            results_per_category_iou50.append(res_item)

                    else:
                        lab = {
                            "name": classes[0],
                            "AP": a_metrics['AP-' + classes[0]],
                            "AR": a_metrics['AR-' + classes[0]],
                            "P": pr_results['all'][2],
                            "R": pr_results['all'][3],
                            "AP50": a_metrics['AP-50-' + classes[0]],
                            "AR50": a_metrics['AR-50-' + classes[0]]
                        }
                        this_metric["metrics"]["labels"].append(lab)
                        false_50 = 1 - lab["AR50"]
                        res_item = [
                            f'{classes[0]}', f'{lab["AP50"]:0.3f}', f'{lab["AR50"]:0.3f}',
                            f'{float(false_50):0.3f}']
                        results_per_category_iou50.append(res_item)

                    num_columns_50 = min(
                        8, len(results_per_category_iou50) * len(res_item))
                    results_flatten_50 = list(
                        itertools.chain(*results_per_category_iou50))
                    headers_50 = [
                        'category', 'AP', 'AR',
                        'FalseRate'] * (num_columns_50 // len(res_item))
                    results_2d_50 = itertools.zip_longest(*[
                        results_flatten_50[i::num_columns_50]
                        for i in range(num_columns_50)
                    ])

                    table_data_50 = [headers_50]
                    table_data_50 += [result for result in results_2d_50]
                    table_50 = AsciiTable(table_data_50)
                    logging.info("IOU阈值大于0.5的预测结果平均值:")
                    logging.info('\n' + table_50.table)

                    merge_results = merge_bbox(gt_data, matched_pred_boxes)
                    coco_error_analysis(merge_results, save_dir='./insect')

                elif pred_false_boxes and unmatch_pred_img and not matched_pred_boxes:
                    this_metric["metrics"].update({
                        "AP": "NaN",
                        "AP50": "NaN",
                        "AP75": "NaN",
                        "APs": "NaN",
                        "APm": "NaN",
                        "APl": "NaN",
                        "AR_50_95_all_1": "NaN",
                        "AR_50_95_all_10": "NaN",
                        "AR_50_95_all_100": "NaN",
                        "ARs": "NaN",
                        "ARm": "NaN",
                        "ARl": "NaN",
                        "P": "NaN",
                        "R": "NaN"
                    })
                    this_metric["metrics"]["labels"] = [{"name": label, "AP": "NaN", "AR": "NaN",
                                                         "P": "NaN", "R": "NaN", "AP50": "NaN", "AR50": "NaN"} for label in classes]

            else:
                this_metric["metrics"].update({
                    "AP": "NaN",
                    "AP50": "NaN",
                    "AP75": "NaN",
                    "APs": "NaN",
                    "APm": "NaN",
                    "APl": "NaN",
                    "AR_50_95_all_1": "NaN",
                    "AR_50_95_all_10": "NaN",
                    "AR_50_95_all_100": "NaN",
                    "ARs": "NaN",
                    "ARm": "NaN",
                    "ARl": "NaN",
                    "P": "NaN",
                    "R": "NaN"
                })
                this_metric["metrics"]["labels"] = [{"name": label, "AP": "NaN", "AR": "NaN",
                                                     "P": "NaN", "R": "NaN", "AP50": "NaN", "AR50": "NaN"} for label in classes]
            metrics.append(this_metric)
        if f1_all:
            f1_max_index = max_index(f1_all)[-1]
            recommend_thres = metrics[f1_max_index]['threshold']
            p, r = metrics[f1_max_index]['metrics']['P'], metrics[
                f1_max_index]['metrics']['R']
            ap = metrics[f1_max_index]['metrics']['AP50']
            logging.info("==" * 50)
            logging.info(
                '该模型应用推荐的置信度为：{}. 在当前置信度下, P={:.3f}, R={:.3f}, AP={:.3f}'.
                format(recommend_thres, p, r, ap))
            logging.info("==" * 50)
        return metrics


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start evaluation.')
    parser.add_argument('--config',
                        type=str,
                        help='config path',
                        default='config/config_fire.json')
    args = parser.parse_args()

    config_path = args.config
    studio_eval = StudioJsonEvaluation()
    studio_eval.indicator(config_path)
