import abc

from sklearn.base import TransformerMixin


class Transformer(TransformerMixin):
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.constructor_kwargs = kwargs

    @abc.abstractmethod
    def fit(self, X, y=None):
        pass

    @abc.abstractmethod
    def transform(self, X):
        pass

    def clone(self):
        return self.__class__(**self.constructor_kwargs)

    @abc.abstractmethod
    def load(self, path):
        pass

    @abc.abstractmethod
    def save(self, path):
        pass
