"""Define base AutoModel interfaces."""

import os
from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique
from typing import Any, Dict, Optional, Tuple, Type
from zipfile import ZipFile

import torch
from torch import nn, optim
from torch.utils.data import DataLoader

from .. import logger, task_logger
from ..contractor import AutoTaskContractor
from ..fed_avg import FedAvgScheduler
from ..fed_avg.contractor import AutoFedAvgContractor
from .exceptions import AutoModelError


@unique
class DataType(int, Enum):

    IMAGE = 1
    TEXT = 2
    AUDIO = 3
    VIDEO = 4


@unique
class TaskType(int, Enum):

    MEDICINE = 1  # 医学


@unique
class TaskMode(int, Enum):

    LOCAL = 1
    FED_AVG = 2
    HETERO_NN_HOST = 3
    HETERO_NN_COLLABORATOR = 4


@unique
class DatasetMode(int, Enum):

    TRAINING = 1
    VALIDATION = 2
    TESTING = 3
    PREDICTING = 4


@dataclass
class Meta(ABC):
    ...


@dataclass
class AutoMeta(Meta, metaclass=ABCMeta):
    """Manage meta data of a auto model."""

    name: str


class AutoModel(ABC):
    """An model which supports alphamed AutoML process."""

    def __init__(self,
                 meta_data: dict,
                 resource_dir: str,
                 **kwargs) -> None:
        super().__init__()
        self.meta_data = meta_data
        self.resource_dir = resource_dir

    @abstractmethod
    def train(self):
        """Go into `train` mode as of torch.nn.Module."""

    @abstractmethod
    def eval(self):
        """Go into `eval` mode as of torch.nn.Module."""

    @abstractmethod
    def forward(self, *args, **kwargs):
        """Do a forward propagation as of torch.nn.Module."""

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.forward(*args, **kwargs)

    @abstractmethod
    def init_dataset(self, dataset_dir: str) -> Tuple[bool, str]:
        """Init local dataset and report the result.

        Args:
            dataset_dir:
                The root dir of the dataset staff.

        Return:
            Tuple[is_verification_successful, the_cause_if_it_is_failed]
        """

    @abstractmethod
    def fine_tune(self,
                  id: str,
                  task_id: str,
                  dataset_dir: str,
                  is_initiator: bool = False,
                  **kwargs):
        """Begin to fine-tune on dataset.

        Args:
            id:
                The ID of current node.
            task_id:
                The ID of current task.
            dataset_dir:
                The root dir of the dataset staff.
            is_initiator:
                Is current node the initiator of the task.
            kwargs:
                Other keywords for specific models.
        """

    def push_log(self, message: str):
        """Push a running log message to the task manager."""
        assert message and isinstance(message, str), f'invalid log message: {message}'
        if hasattr(self, 'task_id') and self.task_id:
            task_logger.info(message, extra={"task_id": self.task_id})
        else:
            logger.warn('Failed to push a message because context is not initialized.')


class AutoModelFamily(ABC):
    """A serious auto models with the same core architecture."""

    @classmethod
    @abstractmethod
    def get_auto_model(cls, name: str) -> Optional[Type[AutoModel]]:
        """Get the auto model class corresponding to the given name if exists."""


class AutoFedAvgModel(AutoModel):
    """Define interfaces for AutoModels work with FedAvgScheduler."""

    @property
    @abstractmethod
    def training_loader(self) -> DataLoader:
        """Return the dataloader object used in training."""

    @property
    @abstractmethod
    def validation_loader(self) -> DataLoader:
        """Return the dataloader object used in validation."""

    @property
    @abstractmethod
    def testing_loader(self) -> DataLoader:
        """Return the dataloader object used in testing."""

    @property
    @abstractmethod
    def model(self) -> nn.Module:
        """Return the model object used in training and predicting."""

    @property
    @abstractmethod
    def optimizer(self) -> optim.Optimizer:
        """Return the optimizer object used in training."""

    @property
    @abstractmethod
    def param_file(self) -> str:
        """Return the value of `meta.param_file`."""

    @property
    @abstractmethod
    def init_args_for_fine_tuned(self) -> Optional[str]:
        """Return necessary arguments for initialize a fine-tuned model.

        Return:
            The necessary information for initialize a fine-tuned model object
            after training, i.e. the labels list. It must be a jsonable string.
            It will be persistent in a `fine_tuned.meta` file and be uploaded with
            the training result files. So that you can download it later and feed
            it back into the model.
        """

    @abstractmethod
    def state_dict(self) -> Dict[str, torch.Tensor]:
        """Get the params that need to train and update.

        Only the params returned by this function will be updated and saved during aggregation.

        Return:
            List[torch.Tensor], The list of model params.
        """

    @abstractmethod
    def load_state_dict(self, state_dict: Dict[str, torch.Tensor]):
        """Load the params that trained and updated.

        Only the params returned by state_dict() should be loaded by this function.
        """

    @abstractmethod
    def train_an_epoch(self) -> Any:
        """Define the training steps in an epoch."""

    @abstractmethod
    def run_test(self) -> Any:
        """Run a round of test."""

    @abstractmethod
    def run_validation(self) -> Any:
        """Run a round of validation."""

    def _fine_tune_impl(self,
                        id: str,
                        task_id: str,
                        dataset_dir: str,
                        scheduler_impl: Type['AutoFedAvgScheduler'],
                        is_initiator: bool = False,
                        min_clients: int = 0,
                        max_clients: int = 0,
                        max_rounds: int = 0,
                        merge_epochs: int = 1,
                        calculation_timeout: int = 300,
                        schedule_timeout: int = 30,
                        log_rounds: int = 0,
                        **kwargs):

        is_dataset_ready, cause_of_failure = self.init_dataset(dataset_dir)
        if not is_dataset_ready:
            raise AutoModelError(f'Failed to initialize dataset. {cause_of_failure}')

        if is_initiator and not self.testing_loader:
            raise AutoModelError('The initiator must provide testing dataset.')
        if not is_initiator and not self.training_loader:
            raise AutoModelError('The collaborator must provide training dataset.')

        task_contractor = AutoTaskContractor(task_id=task_id)
        self.clients = task_contractor.query_nodes()
        involve_aggregator = bool(self.validation_loader
                                  and len(self.validation_loader) > 0)
        if involve_aggregator:
            min_clients = min_clients or len(self.clients)
            max_clients = max_clients or len(self.clients)
        else:
            min_clients = min_clients or len(self.clients) - 1
            max_clients = max_clients or len(self.clients) - 1

        self.scheduler = scheduler_impl(auto_proxy=self,
                                        min_clients=min_clients,
                                        max_clients=max_clients,
                                        max_rounds=max_rounds,
                                        merge_epochs=merge_epochs,
                                        calculation_timeout=calculation_timeout,
                                        schedule_timeout=schedule_timeout,
                                        log_rounds=log_rounds,
                                        involve_aggregator=involve_aggregator,
                                        **kwargs)
        self.scheduler._setup_context(id=id,
                                      task_id=task_id,
                                      is_initiator=is_initiator)
        self.scheduler._launch_process()

    def push_log(self, message: str):
        return self.scheduler.push_log(message)


class AutoFedAvgScheduler(FedAvgScheduler):

    def __init__(self,
                 auto_proxy: AutoFedAvgModel,
                 min_clients: int,
                 max_clients: int,
                 max_rounds: int = 0,
                 merge_epochs: int = 1,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 log_rounds: int = 0,
                 involve_aggregator: bool = False,
                 **kwargs):
        super().__init__(min_clients=min_clients,
                         max_clients=max_clients,
                         max_rounds=max_rounds,
                         merge_epochs=merge_epochs,
                         calculation_timeout=calculation_timeout,
                         schedule_timeout=schedule_timeout,
                         log_rounds=log_rounds,
                         involve_aggregator=involve_aggregator)
        self.auto_proxy = auto_proxy

    def build_model(self) -> nn.Module:
        return self.auto_proxy.model

    def build_optimizer(self, model: nn.Module) -> optim.Optimizer:
        return self.auto_proxy.optimizer

    def build_train_dataloader(self) -> DataLoader:
        return self.auto_proxy.training_loader

    def build_validation_dataloader(self) -> DataLoader:
        return self.auto_proxy.validation_loader

    def build_test_dataloader(self) -> DataLoader:
        return self.auto_proxy.testing_loader

    def state_dict(self) -> Dict[str, torch.Tensor]:
        return self.auto_proxy.state_dict()

    def load_state_dict(self, state_dict: Dict[str, torch.Tensor]):
        return self.auto_proxy.load_state_dict(state_dict)

    @property
    @abstractmethod
    def best_state_dict(self) -> Dict[str, torch.Tensor]:
        """Return the best state of the model by now."""

    def _setup_context(self, id: str, task_id: str, is_initiator: bool = False):
        """DO NOT OVERRIDE unless you know exactly what you are doing."""
        super()._setup_context(id=id, task_id=task_id, is_initiator=is_initiator)
        self.contractor = AutoFedAvgContractor(task_id=task_id)
        self.data_channel.contractor = self.contractor

    def _run_a_round(self):
        super()._run_a_round()
        self._report_progress()

    def _report_progress(self) -> bool:
        max_rounds = (self.max_rounds
                      if not self.validation_loader or len(self.validation_loader) == 0
                      else max(int(self.max_rounds * 0.8), 20))
        percent = self._round * 100 // max_rounds
        percent = min(percent, 99)
        self.contractor.report_progress(percent=percent)

    def _save_model(self):
        """Save the best or final state of fine tuning."""
        os.makedirs(self._checkpoint_dir, exist_ok=True)
        with open(os.path.join(self._checkpoint_dir, 'model_ckpt.pt'), 'wb') as f:
            torch.save(self.best_state_dict, f)
        self.push_log('Saved latest parameters locally.')

    def _prepare_task_output(self) -> Tuple[str, str]:
        """Generate final output files of the task.

        Return:
            Local paths of the report file and model file.
        """
        self.push_log('Uploading task achievement and closing task ...')

        os.makedirs(self._result_dir, exist_ok=True)

        metrics_files = []
        for _name, _metrics in self._metrics_bucket.items():
            _file = f'{os.path.join(self._result_dir, _name)}.csv'
            _metrics.to_csv(_file)
            metrics_files.append(_file)
        report_file = os.path.join(self._result_dir, "report.zip")
        with ZipFile(report_file, 'w') as report_zip:
            for _file in metrics_files:
                report_zip.write(_file, os.path.basename(_file))
        report_file_path = os.path.abspath(report_file)

        # torch.jit doesn't work with a TemporaryFile
        resource_dir = self.auto_proxy.resource_dir
        resource_zip_file = os.path.join(self._result_dir, 'model.zip')
        with ZipFile(resource_zip_file, 'w') as resource_zip:
            for path, _, filenames in os.walk(resource_dir):
                for _file in filenames:
                    if os.path.join(path, _file) == self.auto_proxy.param_file:
                        continue  # don't save the original params
                    inner_path = path[len(resource_dir):]
                    resource_zip.write(os.path.join(path, _file),
                                       os.path.join(inner_path, _file))

            rel_param_file = self.auto_proxy.param_file[len(self.auto_proxy.resource_dir) + 1:]
            resource_zip.write(os.path.join(self._checkpoint_dir, 'model_ckpt.pt'),
                               rel_param_file)
            if self.auto_proxy.init_args_for_fine_tuned:
                with open(os.path.join(resource_dir, 'fine_tuned.meta'), 'w') as f:
                    f.write(self.auto_proxy.init_args_for_fine_tuned)
                resource_zip.write(os.path.join(resource_dir, 'fine_tuned.meta'),
                                   'fine_tuned.meta')
        resource_file_path = os.path.abspath(resource_zip_file)

        self.push_log('Task achievement files are ready.')
        return report_file_path, resource_file_path
