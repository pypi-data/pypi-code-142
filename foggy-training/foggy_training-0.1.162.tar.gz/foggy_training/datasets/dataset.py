from typing import Union

import numpy as np
import pandas as pd
import torchvision
from attr import define
from matplotlib import pyplot as plt
from sklearn.pipeline import Pipeline, FeatureUnion
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import ToPILImage
from tqdm import tqdm
import multiprocessing


class FTDataset(Dataset):
    def __init__(self, items,
                 transforms: Union[callable, Pipeline, FeatureUnion]):
        self.items = items
        self.transforms = transforms
        self._cache = dict()

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):

        if self._cache:
            return self._cache[idx]

        if isinstance(self.items, pd.DataFrame):
            item = self.items.iloc[idx]
        else:
            item = self.items[idx]

        return self.transforms(item)

    def cache(self, batch_size: int = 16, num_workers: int = 'all', **kwargs):
        num_workers = multiprocessing.cpu_count() if num_workers == 'all' else num_workers
        dl = DataLoader(self, batch_size=batch_size, num_workers=num_workers, shuffle=False,
                        collate_fn=lambda d: d,
                        **kwargs)
        idx = 0
        for batch in tqdm(dl):
            for item in batch:
                self._cache[idx] = item
                idx += 1

    def show_item(self, idx):
        def show(imgs):
            if not isinstance(imgs, list):
                imgs = [imgs]
            fig, axs = plt.subplots(ncols=len(imgs), squeeze=False, figsize=(24, 24))
            for i, img in enumerate(imgs):
                img = img.detach()
                img = ToPILImage()(img)
                axs[0, i].imshow(np.asarray(img))
                axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

        show(torchvision.utils.make_grid(self[idx]['x'], normalize=True, nrow=4))


@define
class DatasetBlueprint:
    transforms: Union[callable, Pipeline, FeatureUnion]

    def __call__(self, items):
        return FTDataset(items, self.transforms)
