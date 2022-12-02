# conding: utf-8
import numpy as np


def box_iou_numpy(box1, box2):
    # https://github.com/pytorch/vision/blob/master/torchvision/ops/boxes.py
    """
    Return intersection-over-union (Jaccard index) of boxes.
    Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
    Arguments:
        box1 (numpy[N, 4])
        box2 (numpy[M, 4])
    Returns:
        iou (numpy[N, M]): the NxM matrix containing the pairwise
            IoU values for every element in boxes1 and boxes2
    """
    def box_area(box):
        return (box[:, 2] - box[:, 0]) * (box[:, 3] - box[:, 1])

    area1 = box_area(box1)
    area2 = box_area(box2)
    inter = (np.minimum(box1[:, None, 2:], box2[:, 2:]) -
             np.maximum(box1[:, None, :2], box2[:, :2])).clip(0).prod(2)
    return inter / (area1[:, None] + area2 - inter)


def merge_bbox(gt, pre_bbox):
    merge_results = dict()

    merge_results['gt'] = gt
    merge_results['bbox'] = pre_bbox

    return merge_results
