from __future__ import annotations
from bfscan.utils import sequence_to_kmer
from bloom_filter2 import BloomFilter
from collections.abc import Iterable
import numpy as np 
import pickle
import copy

class BFScanModel:

    def __init__(self, base_estimator, filter):
    
        self.base_estimator = base_estimator
        self.filter = filter
        self.classes = self.filter.classes + ['other']

    def transform(self, X, n_jobs=1):
        return self.filter.predict_proba(X, n_jobs=n_jobs)
        
    def fit(self, X, y):

        X_ = self.transform(X)
        self.base_estimator.fit(X_, y)

    def predict(self, X, n_jobs=1):
        y_pred_proba   = self.predict_proba(X, n_jobs=n_jobs)
        y_pred_classes = np.argmax(y_pred_proba, axis=1)        
        y_pred = [self.classes[class_id] for class_id in y_pred_classes]
        
        return y_pred

    def predict_proba(self, X, n_jobs=1):

        X_ = self.transform(X, n_jobs=n_jobs)
        y_pred_proba = self.base_estimator.predict_proba(X_)
                  
        return y_pred_proba

    def save(self, filename):
        with open(filename, 'wb') as writer:
            writer.write(pickle.dumps(self))

    @staticmethod
    def load(filename) -> BFScanModel:
        with open(filename, 'rb') as reader:
            return pickle.loads(reader.read())   
