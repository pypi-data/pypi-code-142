from lvt_eval.tools.ap_per_class import ap_per_class
from lvt_eval.utils.boxes import box_iou_numpy
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s [%(pathname)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def cal_precision_and_recall(target_data, prediction_data, names, nc):
    target_info = target_data
    prediction_info = prediction_data
    iouv = np.linspace(0.5, 0.95, 10)  # iou vector for mAP@0.5:0.95
    target_list, prediction_list, ap_class = [], [], []
    mp, mr, map50, map, seen, f1_mean = 0.0, 0.0, 0.0, 0.0, 0, 0.0
    stats = []
    pr_results = {}

    """
    prediction_tensor (Array[N, 7]), image_id, x1, y1, x2, y2, conf, class  预测结果
    target_tensor (Array[M, 6]), image_id, class, x1, y1, x2, y2  标注的真实结果
    """

    # target
    for i in range(len(target_info['annotations'])):
        tx1, ty1 = target_info['annotations'][i]["bbox"][0], target_info['annotations'][i]["bbox"][1]
        tx2, ty2 = target_info['annotations'][i]["bbox"][0] + \
            target_info['annotations'][i]["bbox"][2], target_info['annotations'][i]["bbox"][1] + \
            target_info['annotations'][i]["bbox"][3]
        timage_id, tcat = float(target_info['annotations'][i]["image_id"]), float(
            target_info['annotations'][i]["category_id"])
        target_list.append([timage_id, tcat, tx1, ty1, tx2, ty2])
   
    target_tensor = np.array(target_list)

    # 　prediction
    for j in range(len(prediction_info)):
        px1, py1 = prediction_info[j]["bbox"][0], prediction_info[j]["bbox"][1]
        px2, py2 = prediction_info[j]["bbox"][0] + \
            prediction_info[j]["bbox"][2], prediction_info[j]["bbox"][1] + \
            prediction_info[j]["bbox"][3]
        pimage_id, pcat, score = float(prediction_info[j]["image_id"]), float(
            prediction_info[j]["category_id"]), prediction_info[j]["score"]
        prediction_list.append([pimage_id, px1, py1, px2, py2, score, pcat])
    
    prediction_tensor = np.array(prediction_list)

    for si in range(int(prediction_tensor[:, 0][-1] + 1)):
        if si not in target_tensor[:, 0]:
            continue
        labels = target_tensor[target_tensor[:, 0] == si, 1:]  # 真实框信息
        nl = labels.shape[0]

        tcls = labels[:, 0].tolist() if nl else []  # target class
        predn = prediction_tensor[prediction_tensor[:, 0] == si, 1:]  # 预测框信息

        seen += 1
        # ---------------------------------------------------------------
        npr = prediction_tensor.shape[0]  # 总的框数
        if npr == 0:
            if nl:
                stats.append((correct, *np.zeros((2, 0)), labels[:, 0]))
            continue
        # Evaluate
        if nl:
            tbox = labels[:, 1:5]  # target boxes ======= xyxy
            # native-space labels (class, x1, y1, x2, y2)
            labelsn = np.concatenate((labels[:, 0:1], tbox), 1)
            correct = process_batch_numpy(predn, labelsn, iouv)
        # (correct, conf, pcls, tcls)
        stats.append((correct, predn[:, 4], predn[:, 5], labels[:, 0]))

        # ---------------------------------------------------------------
    # Compute statistics
    stats = [np.concatenate(x, 0) for x in zip(*stats)]  # to numpy
    if len(stats) and stats[0].any():

        tp, fp, p, r, f1, ap, ap_class = ap_per_class(*stats, names=names)
        ap50, ap = ap[:, 0], ap.mean(1)  # AP@0.5, AP@0.5:0.95
        f1_mean = f1.mean()  # F1
        mp, mr, map50, map = p.mean(), r.mean(), ap50.mean(), ap.mean()

    # number of targets per class
    nt = np.bincount(stats[3].astype(int), minlength=nc)

    # Print results
    s = ('%10s' + '%12s' * 2 + '%8s' * 2 + '%13s' * 3) % ('Class',
                                                          'Images', 'Labels', 'P', 'R', 'mAP@.5', 'mAP@.5:.95', 'F1 score')
    logging.info(s)
    pf = '%10s' + '%11i' * 2 + '%11.3g' * 5  # print format
    logging.info(pf % ('all', seen, nt.sum(), mp, mr, map50, map, f1_mean))
    pr_results['all'] = [seen, nt.sum(), mp, mr, map50, map, f1_mean]

    # Print results per class
    if nc > 1 and len(stats):
        for i, c in enumerate(ap_class):

            logging.info(pf % (names[c], seen, nt[c],
                         p[i], r[i], ap50[i], ap[i], f1[i]))
            pr_results[names[c]] = [seen, nt[c],
                                    p[i], r[i], ap50[i], ap[i], f1[i]]
    return pr_results


def process_batch_numpy(detections, labels, iouv):
    """
    Return correct predictions matrix. Both sets of boxes are in (x1, y1, x2, y2) format.
    Arguments:
        detections (Array[N, 6]), x1, y1, x2, y2, conf, class  预测结果
        labels (Array[M, 5]), class, x1, y1, x2, y2  标注的真实结果
    Returns:
        correct (Array[N, 10]), for 10 IoU levels
    """
    correct = np.zeros((detections.shape[0], iouv.shape[0])).astype(bool)
    iou = box_iou_numpy(labels[:, 1:], detections[:, :4])
    # ---------------------------------------------------------------
    correct_class = labels[:, 0:1] == detections[:, 5]
    for i in range(len(iouv)):
        # IoU > threshold and classes match
        x = np.where((iou >= iouv[i]) & correct_class)
        if x[0].shape[0]:
            # .cpu().numpy()  # [label, detection, iou]
            matches = np.column_stack(
                (np.stack(x, 1), iou[x[0], x[1]][:, None]))
            if x[0].shape[0] > 1:
                matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(
                    matches[:, 1], return_index=True)[1]]
                # matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(
                    matches[:, 0], return_index=True)[1]]
            correct[matches[:, 1].astype(int), i] = True
    # ---------------------------------------------------------------

    # x = np.where((iou >= iouv[0]) & (labels[:, 0:1] == detections[:, 5]))  # IoU above threshold and classes match
    # if x[0].shape[0]:
    #     matches = np.column_stack((np.stack(x, 1), iou[x[0], x[1]][:, None]))#.cpu().numpy()  # [label, detection, iou]
    #     if x[0].shape[0] > 1:
    #         matches = matches[matches[:, 2].argsort()[::-1]]
    #         matches = matches[np.unique(matches[:, 1], return_index=True)[1]]
    #         # matches = matches[matches[:, 2].argsort()[::-1]]
    #         matches = matches[np.unique(matches[:, 0], return_index=True)[1]]
    #     # matches = torch.Tensor(matches).to(iouv.device)
    #     correct[matches[:, 1].astype(int)] = matches[:, 2:3] >= iouv
    return correct


if __name__ == '__main__':
    detections = np.array([
        [168.0732, 399.3882, 194.4995, 419.9093,   0.9304,   0.0000],
        [134.6291, 521.1181, 163.5203, 545.9926,   0.7533,   0.0000]])
    labels = np.array([[0.0000, 167.4550, 397.9094, 198.7564, 418.9667],
                       [0.0000, 137.3941, 521.1845, 161.7689, 546.5866],
                       [0.0000, 137.0474, 500.2992, 163.5090, 518.9866],
                       [0.0000, 167.9946, 379.5518, 195.5183, 395.2098],
                       [0.0000, 112.2710, 278.8515, 122.8941, 296.7064]])
    iouv = np.array([0.5000, 0.5500, 0.6000, 0.6500, 0.7000, 0.7500, 0.8000, 0.8500, 0.9000,
                     0.9500])
    print(process_batch_numpy(detections, labels, iouv))

    '''
    [[ True  True  True  True  True False False False False False]
 [ True  True  True  True  True  True False False False False]
 [ True  True  True  True  True  True  True False False False]]'''
