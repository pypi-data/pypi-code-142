import numpy as np
import os
import glob

import torch
from tepe.data.voc_xml import PascalVocReader


def read_xml(xml_path):
    reader = PascalVocReader(xml_path)
    anno_bboxes = reader.get_bbox()
    bboxes = []
    for anno in anno_bboxes:
        label, box = anno.get('name'), anno.get('bndbox')
        bboxes.append(box)

    return torch.tensor(bboxes)


def box_iou(box1, box2):
    """
    Return intersection-over-union (Jaccard index) of boxes.
    Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
    Arguments:
        box1 (Tensor[N, 4])
        box2 (Tensor[M, 4])
    Returns:
        iou (Tensor[N, M]): the NxM matrix containing the pairwise
            IoU values for every element in boxes1 and boxes2
    """

    def box_area(box):
        # box = 4xn
        return (box[2] - box[0]) * (box[3] - box[1])

    area1 = box_area(box1.T)
    area2 = box_area(box2.T)

    # inter(N,M) = (rb(N,M,2) - lt(N,M,2)).clamp(0).prod(2)
    inter = (torch.min(box1[:, None, 2:], box2[:, 2:]) - torch.max(box1[:, None, :2], box2[:, :2])).clamp(0).prod(2)
    return inter / (area1[:, None] + area2 - inter)  # iou = inter / (area1 + area2 - inter)


def cal_true_positive(gt, pred, iou_thr=0.001):
    num_pred = len(pred)
    num_gt = len(gt)
    tp = 0
    if num_gt > 0 and num_pred > 0:
        iou = box_iou(gt, pred)
        x = torch.where((iou >= iou_thr))

        if len(x) > 0:
            x = x[1].numpy()
            tp = len(np.unique(x))

    tp = num_gt if tp > num_gt else tp
    return tp


if __name__ == '__main__':
    pred_dir = '/home/zepei/workspace/tepe/outputs/rd_bguo_221024/bguo/predict'
    label_idr = '/home/zepei/DATA/lenovo_anomaly/bguo/ground_truth/yiwu3'

    total_pred, total_gt, total_tp = 0, 0, 0
    for pred_xml_path in glob.glob(os.path.join(pred_dir, '*.xml')):
        xml_name = os.path.basename(pred_xml_path)
        label_xml_path = os.path.join(label_idr, xml_name)

        pred = read_xml(pred_xml_path)
        gt = read_xml(label_xml_path)

        num_pred = len(pred)
        num_gt = len(gt)
        tp = cal_true_positive(gt, pred)

        total_pred += num_pred
        total_gt += num_gt
        total_tp += tp

    precision = total_tp / total_pred
    recall = total_tp / total_gt

    print('精度， 召回：', precision, recall)