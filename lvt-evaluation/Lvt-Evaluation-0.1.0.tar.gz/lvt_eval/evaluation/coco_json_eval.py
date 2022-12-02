# coding: utf-8
import argparse
from lvt_eval.utils import check_json, get_classes_and_imgs, merge_bbox, load_json, sorted_image_id
from lvt_eval.tools import coco_error_analysis, cal_precision_and_recall, cal_map

import logging

logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


class CocoJsonEvaluation:

    def __init__(self, gt_json, pred_json):
        self.gt_json = gt_json
        self.pred_json = pred_json

    def indicator(self, thresholds=[0.1]):
        pred_data = sorted_image_id(load_json(self.pred_json)) if type(self.pred_json) == str else self.pred_json
        gt_data = load_json(self.gt_json) if type(self.gt_json) == str else self.gt_json

        names, classes, _ = get_classes_and_imgs(self.gt_json)
        metrics = []
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

                    a_metrics = cal_map(gt_data, matched_pred_boxes)

                    pr_results = cal_precision_and_recall(
                        gt_data, matched_pred_boxes, names, len(names))

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
                                              "P": "NaN", "R": "NaN", "AP50": "NaN", "AR50":"NaN"} for label in classes]

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
                                          "P": "NaN", "R": "NaN", "AP50": "NaN", "AR50":"NaN"} for label in classes]


            metrics.append(this_metric)
        return metrics

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start evaluation.')
    parser.add_argument('--gt_json',
                        type=str,
                        help='groundtruth absolute path',
                        default='')
    parser.add_argument('--pred_json',
                        type=str,
                        help='prediction absolute path',
                        default='')
    args = parser.parse_args()

    groundtruth_json = args.gt_json
    prediction_json = args.pred_json

    eval = CocoJsonEvaluation(groundtruth_json, prediction_json)
    eval.indicator()
