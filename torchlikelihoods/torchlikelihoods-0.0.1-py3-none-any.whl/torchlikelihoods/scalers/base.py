from abc import ABC, abstractmethod


class BaseScaler(ABC):

    @abstractmethod
    def fit(self, x, dims=None):
        pass

    @abstractmethod
    def fit_with_loader(self, loader, dims=None):
        pass
    @abstractmethod
    def fit_manual(self):
        pass
    @abstractmethod
    def transform(self, x):
        pass

    @abstractmethod
    def inverse_transform(self, x_norm):
        pass

