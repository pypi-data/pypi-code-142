__author__ = 'Qi'
# Created by on 11/25/22.
import torch
import torch.nn as nn

class ABLoss(nn.Module):
    '''
    This is the attention biased loss for handling data imbalance problem.
    When combining with SGD optimizer, its the absgd.
    When combining with Adam optimizer, its the ABAdam.
    We implement the multi stage lambda that: applying the ABSGD after learning a representation at certain epoch.
    '''
    def __init__(self,  mylambda, milestone = 0, criterion = nn.CrossEntropyLoss(reduction='none'), abgamma = 0.9, abalpha =1):
        '''
        :param mylambda: regularizers that we want to set
        :param milestone (default 0): decayed epoch
        :param criterion (default multi-class cross entropy): loss criterion
        :param abgamma (default 0.9) : moving average parameter
        :param abalpha (default 1) : control the stability of moving average parameter, (0, 1]
        '''
        super(ABLoss, self).__init__()
        self.u = 0
        self.abgamma = abgamma
        self.abalpha = abalpha
        self.criterion = criterion
        self.milestone = milestone
        self.ablambda = None
        self.mylambda = mylambda
        self.step = 0

    def forward(self, output, target):
        loss = self.criterion(output, target)
        if self.ablambda is None:
            # reduces to CE
            p = 1/len(loss)
        else:
            # exponential loss
            expLoss = torch.exp(loss / self.ablambda)
            # record moving average history
            self.u = (1 - self.abgamma) * self.u + self.abgamma * (self.abalpha * torch.mean(expLoss))
            # robust weights
            drop = expLoss/(self.u * len(loss))
            drop.detach_()
            p = drop

        abloss = torch.sum(p * loss)
        return abloss

    def updateLambda(self):
        if self.step >= self.milestone - 1:
            self.ablambda = self.mylambda
        self.step += 1




