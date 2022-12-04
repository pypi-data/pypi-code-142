"""

The config bundles the configuration for dataset, model and training.
```python
from foggy_training import config

print(config)
# config was set to cpu because no gpu was detected.
# Config(trainer=TrainerConfig(max_epochs=3, ...), data=DataConfig(batch_size=32, num_workers=0))
```

replace values:

```python
config.trainer.max_epochs = 15
```

get trainer:

```python
from pytorch_lightning import Trainer
trainer = Trainer(**config.trainer.as_dict)

```


"""



from typing import Union, List

import torch
from attr import field, asdict, define
from datasets import Dataset
from pytorch_lightning import Callback
from torch.utils.data import DataLoader


@define
class DataConfig:
    """

    DataConfig holds values that are specific for dataset creation:

    batch size (defaults to 32)
    num_workers (defaults to 6 on GPU and 0 on CPU)

    """
    batch_size: int = 32
    num_workers: int = 6

    def cpu(self):
        self.num_workers = 0
        self.batch_size = 32

    def gpu(self):
        self.num_workers = 6
        self.batch_size = 32

    @property
    def as_dict(self):
        return asdict(self)  # noqa

    def get_dataloader(self, dataset: Dataset, shuffle: bool) -> DataLoader:
        """
        The config may create DataLoaders based on the config values

        Args:
            dataset: torch compatible dataset
            shuffle: if True, shuffle values.

        Returns: DataLoader

        """
        return DataLoader(dataset, shuffle=shuffle, **self.as_dict)


@define
class TrainerConfig:

    """

    TrainerConfig holds values that are specific for trainer creation:

    max_epochs (defaults to 20)
    ... tbc

    """

    max_epochs: int = 20
    auto_scale_batch_size: Union[str, bool] = False
    callbacks: List[Callback] = field(factory=lambda: [])
    accelerator: str = 'gpu'
    precision: Union[int, str] = 16
    logger: bool = True
    gradient_clip_val: Union[int, float] = None
    enable_progress_bar: bool = True
    overfit_batches: Union[int, float] = 0.0
    track_grad_norm: Union[int, float, str] = -1
    fast_dev_run: Union[int, bool] = False
    log_every_n_steps: int = 50
    enable_model_summary: bool = True
    num_sanity_val_steps: int = 2

    def cpu(self):
        self.accelerator = 'cpu'
        self.precision = 32
        self.logger = False
        self.max_epochs = 3

    def gpu(self):
        self.accelerator = 'gpu'
        self.precision = 16
        self.logger = True
        self.overfit_batches = 0.0

    @property
    def as_dict(self):
        return asdict(self)  # noqa


@define
class Config:
    """

    Config holds the values for trainer and data config.

    You can change default values by calling config.cpu() or config.gpu().

    """
    trainer: TrainerConfig = TrainerConfig()
    data: DataConfig = DataConfig()

    def __attrs_post_init__(self):
        if not torch.cuda.is_available():
            self.cpu()
            print('config was set to cpu because no gpu was detected.')

    def cpu(self):
        self.trainer.cpu()
        self.data.cpu()

    def gpu(self):
        self.trainer.gpu()
        self.data.gpu()
