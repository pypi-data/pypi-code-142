from lvt_eval.tools.customcoco import CustomCOCO as _COCO
from lvt_eval.tools.customcocoeval import CustomCOCOeval as _COCOeval
import numpy as np


def cal_map(gt_data, pred_data):

    anno = _COCO(gt_data)
    pred = anno.loadRes(pred_data)
    eval = _COCOeval(anno, pred, 'bbox')

    eval.evaluate()
    eval.accumulate()
    eval.summarize()
    metrics = [
        "AP", "AP50", "AP75", "APs", "APm", "APl", "AR_50_95_all_1",
        "AR_50_95_all_10", "AR_50_95_all_100", "ARs", "ARm", "ARl"
    ]
    results = {
        metric: float(eval.stats[idx] if eval.stats[idx] >= 0 else "NaN")
        for idx, metric in enumerate(metrics)
    }
    precisions = eval.eval["precision"]
    recalls = eval.eval["recall"]
    results_per_category_ap = []
    results_per_category_ar = []
    cats = list(eval.cocoGt.cats.values())
    class_names = [c["name"] for c in sorted(cats, key=lambda x: x["id"])]
    for idx, name in enumerate(class_names):
        # area range index 0: all area ranges
        # max dets index -1: typically 100 per image

        # AP per category
        precision = precisions[:, :, idx, 0, -1]
        precision = precision[precision > -1]
        precision_50 = precisions[0, :, idx, 0, -1]
        precision_75 = precisions[5, :, idx, 0, -1]
        ap = np.mean(precision) if precision.size else "NaN"
        ap50 = np.mean(precision_50) if precision.size else "NaN"
        ap75 = np.mean(precision_75) if precision.size else "NaN"

        results_per_category_ap.append(("{}".format(name), ap))
        results_per_category_ap.append(("{}".format('50-' + name), ap50))
        results_per_category_ap.append(("{}".format('75-' + name), ap75))

        # AR per category
        recall = recalls[:, idx, 0, -1]
        recall = recall[recall > -1]
        recall_50 = recalls[0, idx, 0, -1]
        ar = np.mean(recall) if recall.size else "NaN"
        ar50 = np.mean(recall_50) if recall.size else "NaN"
        results_per_category_ar.append(("{}".format(name), ar))
        results_per_category_ar.append(("{}".format('50-' + name), ar50))

    # for idx, name in enumerate(class_names):
    #     # area range index 0: all area ranges
    #     # max dets index -1: typically 100 per image
    #     recall = recalls[:, idx, 0, -1]
    #     recall = recall[recall > -1]
    #     ar = np.mean(recall) if recall.size else float("nan")
    #     results_per_category.append(("{}".format(name), float(ar * 100)))
    results.update(
        {"AP-" + name: ap
            for name, ap in results_per_category_ap})
    results.update(
        {"AR-" + name: ar
            for name, ar in results_per_category_ar})
    return results
