from typing import Any, Dict

import torch
from torch.utils.data import Dataset

from bmlt.common.lmdb_storage import JsonLmdb


class LMDBDataset(Dataset):
    """
    LMDB PyTorch Dataset to use for numerical
    tabular data from a JsonLmdb storage.
    """

    def __init__(self, lmdb_file: str) -> None:
        super().__init__()
        self.lmdb_file = lmdb_file
        self.db = JsonLmdb.open(self.lmdb_file, "r")

        self.keys = sorted(self.db.keys())

        some_item = self.db[self.keys[0]]
        self.item_keys_order = sorted(some_item.keys())

    def form_tensor(self, item: Dict[str, Any]) -> torch.FloatTensor:
        """Produce flat tensor for the item.

        Parameters
        ----------
        item : Dict
            item from the storage

        Returns
        -------
        torch.FloatTensor
            1-d tensor with all the features
        """
        res = []
        for key in self.item_keys_order:
            value = item[key]
            if isinstance(value, list):
                res += [float(x) for x in value]
            else:
                res.append(float(value))
        return torch.tensor(res, dtype=torch.float32)

    def __len__(self) -> int:
        return len(self.db)

    def __getitem__(self, idx: int) -> torch.Tensor:
        key = self.keys[idx]
        item = self.db[key]
        return self.form_tensor(item)
