from abc import ABC

import joblib

from mlc.models.model import Model


class SkModel(Model, ABC):
    def load(self, path):
        self.model = joblib.load(path)

    def save(self, path):
        joblib.dump(self.model, path)
