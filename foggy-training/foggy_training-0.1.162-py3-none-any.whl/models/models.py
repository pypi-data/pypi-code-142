"""

`foggy_training.models` provides some default implementations for common models. They inherit from LightningExtended
and are trainable with PytorchLightning.

## Example

Say you have your regression module ready:
```python
model = nn.Sequential(...modules)
```
now you want to train it. Use it as follows:
```python
model = ModuleFromModel(model, 'mse_loss', metrics=['R2Score'])
```
and fit:

```python
trainer = Trainer(**config.trainer.as_dict)
trainer.fit(model, ...your data)
```


"""

from functools import singledispatch
from typing import List, Union

import torch
from datasets import Dataset, DatasetDict
from torch import nn
from torch.nn.functional import cross_entropy
from transformers import AutoConfig, AutoModel, AutoTokenizer

from foggy_training.base import LightningExtended, ForwardResult


@singledispatch
def prepare_inputs(dataset: Dataset, x_cols: List[str], y_col: str):
    assert all([f in dataset.features for f in x_cols]), 'x_cols provided that are not in dataset'
    assert y_col in dataset.features, 'y_col provided that is not in dataset'
    remove = [c for c in dataset.features if c not in x_cols + [y_col]]
    dataset = dataset.remove_columns(remove)
    dataset.set_format('pt')
    return dataset


@prepare_inputs.register
def _(dataset: DatasetDict, x_cols: List[str], y_col: str):
    new_data = dict()
    for d in dataset:
        new_data[d] = prepare_inputs(dataset[d], x_cols, y_col)
    return DatasetDict(new_data)


class SoftmaxClassifier(LightningExtended):
    def __init__(self, n_inputs: int, n_classes: int, metrics=None, hidden_dim: int = 50):
        super().__init__(loss_fun=cross_entropy, metrics=metrics)

        self.model = nn.Sequential(
            nn.Linear(n_inputs, hidden_dim), nn.LeakyReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.LeakyReLU(),
            nn.Linear(hidden_dim, n_classes)
        )

    def forward(self, batch: dict) -> ForwardResult:
        pred = self.model(batch['x'])
        return ForwardResult(pred=pred, true=batch['y'])


class ModuleFromModel(LightningExtended):
    def __init__(self, model, loss_fun: Union[str, callable], lr: float = None, metrics=None, x: str = 'x', y: str = 'y'):
        """
        ModuleFromModel turns an existing model into a LightningExtended Module. This way, it is trainable using
        PytorchLightning.

        Example:
        ```python
        from foggy_training.models import ModuleFromModel
        from foggy_training import config

        model = nn.Sequential(nn.Linear(10, 15), nn.ReLU(), nn.Linear(15, 15), nn.ReLU(), nn.Linear(15, 1))
        model = ModuleFromModel(model, 'mse_loss', metrics=['R2Score'])

        trainer = Trainer(**config.trainer.as_dict)
        trainer.fit(model, ...your data)

        ```

        Args:
            model: nn.Module
            loss_fun: str or callable, loss to use for training
            metrics: str or torchmetrics, metrics to collect during training. defaults to None.
            x: the data is expected to be in a dictionary. x specifies the entry for x values
            y: y specifies the entry for targets
        """
        super().__init__(loss_fun, lr=lr, metrics=metrics)
        self.model = model
        self.x = x
        self.y = y

    def forward(self, batch) -> ForwardResult:
        x, y = batch[self.x], batch.get(self.y, None)
        pred = self.model(x)
        return ForwardResult(pred, y)


class TransformerModel(LightningExtended):
    def __init__(self, backbone_name: str, head_fn: callable, loss_fun: callable, metrics=None):
        super().__init__(loss_fun=loss_fun, metrics=metrics)
        config = AutoConfig.from_pretrained(backbone_name)
        self.backbone_name = backbone_name
        self.backbone = AutoModel.from_pretrained(backbone_name, config=config)
        self.head = head_fn()

    def forward(self, batch: dict) -> ForwardResult:
        batch = self.backbone(input_ids=batch["input_ids"], attention_mask=batch.get("attention_mask", None))
        batch = batch['last_hidden_state']
        batch = self.head(batch)
        return ForwardResult(pred=batch)

    def tokenize(self, dataset, columns, padding='max_length', truncation=True):
        tokenizer = AutoTokenizer.from_pretrained(self.backbone_name)
        dataset = dataset.map(
            lambda examples: tokenizer(examples[columns],
                                       padding=padding, truncation=truncation, return_tensors="np"),
            batched=True, desc='tokenizing'
        )
        return dataset

    def summary(self, depth: int = 3,
                col_names=('output_size', 'num_params', 'trainable'),
                row_settings=('var_names', ), **kwargs):
        """
        Prints summary of the model with chosen depth of child modules. **kwargs are forwarded to torchsummary.
        """
        input_shape = (3, self.backbone.config.max_position_embeddings)
        input_data = dict(input_ids=torch.ones(input_shape).int())

        super(TransformerModel, self).summary(
            depth=depth, input_data=[input_data],
            col_names=col_names, row_settings=row_settings, **kwargs)
