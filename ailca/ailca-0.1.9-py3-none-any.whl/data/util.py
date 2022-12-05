"""
Data Utilities
--------------
This module contains useful functions to process the dataset objects for machine learning.
"""


import torch.utils.data
import torch_geometric
from typing import Any
from torch_geometric.data import Batch
from ailca.data.base import *
from ailca.data.multimodal import MultimodalDataset


def get_data_loader(dataset: Dataset,
                    batch_size: int,
                    shuffle: bool) -> Union[torch.utils.data.DataLoader, torch_geometric.loader.DataLoader]:
    """
    Get ``DataLoader`` object to fit the model parameters of the ``PyTorchModel``.

    :param dataset: (*Dataset*) A datasets object to generate the mini-batches.
    :param batch_size: (*int*) The size of the mini-batch.
    :param shuffle: (*bool*) A flag variable to generate shuffled mini-batches at every epoch.
    :return: (*Union[torch.utils.data.DataLoader, torch_geometric.loader.DataLoader]*) A data loader object.
    """

    if isinstance(dataset, MultimodalDataset):
        # For multimodal dataset.
        return torch.utils.data.DataLoader(dataset,
                                           batch_size=batch_size,
                                           shuffle=shuffle,
                                           collate_fn=_collate_multimodal)
    else:
        if isinstance(dataset.data[0].x, torch.Tensor):
            # For feature vector and chemical formula dataset.
            return torch.utils.data.DataLoader(dataset,
                                               batch_size=batch_size,
                                               shuffle=shuffle,
                                               collate_fn=_collate)
        else:
            # For graph dataset.
            return torch_geometric.loader.DataLoader(dataset,
                                                     batch_size=batch_size,
                                                     shuffle=shuffle,
                                                     collate_fn=_collate)


def _collate(batch: list) -> Any:
    """
    Generate a mini-batch from the data list.
    It returns a tuple of the mini-batches of the input and target data.
    If the target data is not available, a tuple of the input mini-batch and ``None`` is returned.

    :param batch: (*list*) A list of the batched data.
    :return: (*Any*) Mini-batch of the input and target data.
    """

    if isinstance(batch[0][1], torch.Tensor):
        # For a dataset containing the target values.
        x = list()
        y = list()

        for b in batch:
            x.append(b[0])
            y.append(b[1])

        if isinstance(x[0], torch.Tensor):
            return torch.stack(x, dim=0), torch.vstack(y)
        else:
            return Batch.from_data_list(x), torch.vstack(y)
    else:
        # For a dataset without the target values.
        x = [b[0] for b in batch]

        if isinstance(x[0], torch.Tensor):
            return torch.stack(x, dim=0), None
        else:
            return Batch.from_data_list(x), None


def _collate_multimodal(batch: list) -> Union[Tuple[list, torch.Tensor], Tuple[list, None]]:
    """
    Generate a mini-batch from the data list for multimodal learning.
    It returns a tuple of the mini-batches of the input and target data.
    If the target data is not available, a tuple of the input mini-batch and ``None`` is returned.

    :param batch: (*list*) A list of the batched data.
    :return: (*Union[Tuple[list, torch.Tensor], Tuple[list, None]]*) Mini-batch of the input and target data.
    """

    n_hd = len(batch[0][0])
    _x = [list() for i in range(0, n_hd)]

    if isinstance(batch[0][1], torch.Tensor):
        # For a dataset containing the target values.
        y = list()

        for i in range(0, len(batch)):
            for j in range(0, n_hd):
                _x[j].append(batch[i][0][j])
            y.append(batch[i][1])

        return _aggregate_batch(_x), torch.vstack(y)
    else:
        # For a dataset without the target values.
        for i in range(0, len(batch)):
            for j in range(0, n_hd):
                _x[j].append(batch[i][0][j])

        return _aggregate_batch(_x), None


def _aggregate_batch(list_batches: list) -> list:
    """
    Generate mini-batches from a 2-dimensional list of the data.

    :param list_batches: (*list*) A 2-dimensional list of the data.
    :return: (*list*) A list of the mini-batches.
    """

    n_hd = len(list_batches)
    x = list()

    for i in range(0, n_hd):
        if isinstance(list_batches[i][0], torch.Tensor):
            x.append(torch.stack(list_batches[i], dim=0))
        else:
            x.append(Batch.from_data_list(list_batches[i]))

    return x
