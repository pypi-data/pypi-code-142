__author__ = 'Qi'
# Created by on 11/25/22.
import torch

def ABSGD(model_param, lr, weight_decay = 0.0):
    return torch.optim.SGD(model_param, lr = lr,  momentum=0.9, weight_decay=weight_decay)


def ABAdam(model_param, lr, weight_decay= 0.0):
    return torch.optim.Adam(model_param, lr = lr, weight_decay=weight_decay)
