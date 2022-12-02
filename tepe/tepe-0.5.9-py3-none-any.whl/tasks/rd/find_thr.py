import numpy as np
import torch
from scipy.ndimage import gaussian_filter
from torch.nn import functional as F
from tqdm import tqdm

'''
找个阈值
encoder, bn, decoder:三个模型
good_loader, bad_loader:训练样本的loader, 训练样本贴图后的loader

thr计算方式: (mean(正常样本的分数)+mean(异常样本分数))/2

return: thr <float>
'''


def find(model, good_loader, bad_loader, device):

    model.eval()
    gt_list_sp = []
    pr_list_sp = []
    #
    most = 40
    i = 0

    with torch.no_grad():
        for img, _, _ in tqdm(good_loader):
            i = i + 1
            if i > most:
                break
            img = img.to(device)
            anomaly_map = model(img)
            anomaly_map = anomaly_map.cpu().detach().numpy()
            anomaly_map = gaussian_filter(anomaly_map, sigma=4)  # [256,256]

            gt_list_sp.append(0)  # 一个值
            pr_list_sp.append(np.max(anomaly_map))
        i = 0
        for img, _, _ in tqdm(bad_loader):
            i = i + 1
            if i > most:
                break
            img = img.to(device)
            anomaly_map = model(img)
            anomaly_map = anomaly_map.cpu().detach().numpy()
            anomaly_map = gaussian_filter(anomaly_map, sigma=4)  # [256,256]

            gt_list_sp.append(1)  # 一个值
            pr_list_sp.append(np.max(anomaly_map))

        gt_list_sp = np.array(gt_list_sp)
        pr_list_sp = np.array(pr_list_sp)

        # thr=compare(gt_list_sp=gt_list_sp, pr_list_sp=pr_list_sp)
        thr = (np.mean(pr_list_sp[np.where(gt_list_sp == 0)]) + np.mean(pr_list_sp[np.where(gt_list_sp == 1)])) / 2
    return thr