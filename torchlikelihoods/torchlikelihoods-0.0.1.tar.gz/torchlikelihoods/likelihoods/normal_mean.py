import torch.distributions as td
from torch.utils.data import DataLoader

from .base import BaseLikelihood
from ..scalers import StandardScaler


class NormalMeanLikelihood(BaseLikelihood):
    std = None

    def __init__(self, domain_size):
        super().__init__(domain_size)

        self.std = NormalMeanLikelihood.std

    # a class method to create a Person object by birth year.
    @classmethod
    def create(cls, std):
        cls.std = std
        return cls

    def _params_size(self):
        return self._domain_size

    def forward(self, logits, return_mean=False):
        # mu = torch.sigmoid(logits)
        mu = logits
        p = td.Normal(mu, self.std)
        if return_mean:
            return p.mean, p
        else:
            return p

    def _get_scaler(self):
        return StandardScaler()