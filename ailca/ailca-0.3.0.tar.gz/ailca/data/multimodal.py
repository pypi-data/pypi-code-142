from __future__ import annotations
import numpy
import torch
import torch.utils.data
from typing import Union, Tuple
from copy import deepcopy
from ailca.core.operation import sublist, merge_lists, flatten_lists


class MultimodalDataset(torch.utils.data.Dataset):
    """
    A dataset class to store heterogeneous datasets for multimodal learning.
    """

    def __init__(self,
                 datasets: list):
        self.datasets = datasets
        self.y = datasets[0].y
        self.data = list()

        for i in range(0, len(self.datasets[0])):
            self.data.append([dataset.data[i] for dataset in self.datasets])

        self.metadata = dict()
        self.metadata['names_feats'] = flatten_lists([d.metadata['names_feats'] for d in self.datasets])
        self.metadata['types_feats'] = flatten_lists([d.metadata['types_feats'] for d in self.datasets])
        self.metadata['name_target'] = self.datasets[0].metadata['name_target']
        self.metadata['datasets'] = [d.metadata for d in self.datasets]

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self,
                    idx: int) -> Union[Tuple[list, None], Tuple[list, torch.Tensor]]:
        if self.y is None:
            return [d.x for d in self.data[idx]], None
        else:
            return [d.x for d in self.data[idx]], self.y[idx]

    @property
    def idx_data(self):
        return self.datasets[0].idx_data

    @property
    def tooltips(self):
        return self.datasets[0].tooltips

    def clone(self,
              datasets: list = None) -> MultimodalDataset:
        """
        Generate a clone of the dataset.
        If ``datasets`` is given, a new dataset containing ``datasets`` is generated with copied metadata.

        :param datasets: (*list, optional*) A list of new datasets (*default* = ``None``).
        :return: (*MultimodalDataset*) A copied dataset.
        """

        if datasets is None:
            return deepcopy(self)
        else:
            dataset = MultimodalDataset(datasets)
            dataset.metadata = self.metadata

            return dataset

    def split(self,
              ratio_train: float,
              random_seed: int = None) -> Tuple[MultimodalDataset, MultimodalDataset]:
        """
        Split the dataset into two sub-datasets.

        :param ratio_train: (*float*) A ratio of the number of data in the training dataset.
        :param random_seed: (*int, optional*) A random seed to split the dataset (*default* = ``None``).
        :return: (*Union[Tuple[MultimodalDataset, MultimodalDataset],
        Tuple[MultimodalDataset, MultimodalDataset, MultimodalDataset]]*) Two sub-datasets of the original dataset.
        """

        if random_seed is not None:
            numpy.random.seed(random_seed)

        idx_rand = numpy.random.permutation(len(self))
        n_data_train = int(ratio_train * len(self))
        datasets_train = [d.clone(x=sublist(d.data, idx_rand[:n_data_train])) for d in self.datasets]
        datasets_test = [d.clone(x=sublist(d.data, idx_rand[n_data_train:])) for d in self.datasets]
        dataset_train = self.clone(datasets_train)
        dataset_test = self.clone(datasets_test)

        return dataset_train, dataset_test

    def save(self,
             path: str):
        """
        Save the dataset in a given ``path``.

        :param path: (*str*) Path of the saved dataset.
        """

        torch.save(self, path)

    @staticmethod
    def load(path: str) -> MultimodalDataset:
        """
        Load the dataset from a given ``path``.

        :param path: (*str*) Path of the dataset.
        :return: (*MultimodalDataset*) A dataset object.
        """

        return torch.load(path)

    def get_k_folds(self,
                    k: int,
                    random_seed: int = None) -> list:
        """
        Generate ``k`` subsets of the dataset for k-fold cross-validation.

        :param k: (*int*) The number of subsets for k-fold cross-validation.
        :param random_seed: (*int, optional*) An integer index of the random seed (*default* = ``None``).
        :return: (*list*) A list of the k-folds.
        """

        if random_seed is not None:
            numpy.random.seed(random_seed)

        # Split the dataset into k subsets.
        idx_rand = numpy.array_split(numpy.random.permutation(len(self.data)), k)
        k_folds = list()

        # Generate k tuples of the training and test datasets from the k subsets.
        for i in range(0, k):
            idx_train = merge_lists(idx_rand[:i], idx_rand[i+1:])
            idx_test = idx_rand[i]
            dataset_train = self.clone([d.clone(x=sublist(d.data, idx_train)) for d in self.datasets])
            dataset_test = self.clone([d.clone(x=sublist(d.data, idx_test)) for d in self.datasets])
            k_folds.append([dataset_train, dataset_test])

        return k_folds
