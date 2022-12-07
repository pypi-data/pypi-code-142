from bfscan.utils import sequence_to_kmer
from bloom_filter2 import BloomFilter
from collections.abc import Iterable
from joblib import Parallel, delayed
import numpy as np 
import pickle

class BFScanFilter:

    def __init__(self, k_size, max_elements, error, threshold=0.5):
        
        self.k_size = k_size
        self.max_elements = max_elements
        self.error = error
        self.threshold = threshold
        self._init_filters()
    
    def _init_filters(self):

        self.filters = {}
        self.classes = []

    def fit(self, X, y=None, class_name=None):

        if class_name is None and y is None:
            raise Exception('Either class_name or y must be provided')

        self._init_filters()
        self.partial_fit(X, y=y, class_name=class_name)

    def partial_fit(self, X, y=None, class_name=None):

        if class_name is None and y is None:
            raise Exception('Either class_name or y must be provided')

        for i, X_i in enumerate(X):
            print(i)
            if y:
                class_name = y[i]
            if class_name not in self.filters:
                self.filters[class_name] = BloomFilter(self.max_elements, self.error)
                self.classes.append(class_name)

            kmers = sequence_to_kmer(X_i, self.k_size)
            
            for k, kmer in enumerate(kmers):
                self.filters[class_name].add(kmer)

    def predict(self, X, n_jobs=1):

        y_pred_proba   = self.predict_proba(X, n_jobs=n_jobs)
        y_pred_classes = np.argmax(y_pred_proba, axis=1)        
        y_pred = [self.classes[class_id] for class_id in y_pred_classes]
        
        return y_pred

    def predict_proba(self, X, n_jobs=1):
        y_pred = [self.predict_proba_X_i(X_i) for X_i in X]
        return y_pred

    def predict_proba_X_i(self, X_i):
        y_i = []
        kmers = set(sequence_to_kmer(X_i, self.k_size))
        for class_name in self.classes:
            hit_rate = sum(
                [1 if kmer in self.filters[class_name] else 0 for kmer in kmers]
            )/len(kmers)
            y_i.append(hit_rate)
        return y_i
                  
    def save(self, filename):
        with open(filename, 'wb') as writer:
            writer.write(pickle.dumps(self))

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as reader:
            return pickle.loads(reader.read())       
