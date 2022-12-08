"""
Base Classes
------------
This module contains the base classes of AILCA for machine learning.
It provides abstracted frames to implement the prediction models.
"""


from __future__ import annotations
import joblib
import torch
from abc import ABC, abstractmethod
from typing import Union
from copy import deepcopy
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from gplearn.genetic import SymbolicRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from xgboost import XGBRegressor
from torch.utils.data import DataLoader
from ailca.core.env import *
from ailca.core.sys import is_gpu_runnable
from ailca.data.base import Dataset
from ailca.data.multimodal import MultimodalDataset


class Model(ABC):
    """
    A base class of the machine learning models.
    All machine learning models in AILCA must inherit this base class to utilize the implemented modules.
    """

    @abstractmethod
    def __init__(self,
                 alg_id: str = None,
                 alg_src: str = None):
        self.__alg_id = alg_id
        self.__alg_name = ALG_NAMES[self.__alg_id]
        self.__alg_src = alg_src
        self._model_info = dict()

    def __str__(self):
        return '<Algorithm: {}, Source library: {}>'.format(self.alg_name, self.alg_src)

    @property
    def alg_id(self):
        return self.__alg_id

    @property
    def alg_name(self):
        return self.__alg_name

    @property
    def alg_src(self):
        return self.__alg_src

    @property
    def model_info(self):
        return self._model_info

    @abstractmethod
    def predict(self,
                data: object):
        """
        Calculate the output of the model for a given dataset or data.

        :param data: (*object*) Input data of the machine learning model.
        :return: (*object*) Predicted values for the given ``data``.
        """

        pass

    @abstractmethod
    def save(self,
             path_model_file: str):
        """
        Save the model as a mode file in ``path_model_file``.

        :param path_model_file: (*str*) Path of the model file.
        """

        pass

    @abstractmethod
    def load(self,
             path_model_file: str):
        """
        Load the model parameters from the model file in ``path_model_file``.

        :param path_model_file: (*str*) Path of the model file.
        """

        pass


class SKLearnModel(Model):
    """
    A base class of the machine learning models in Scikit-learn and its variance libraries.
    """

    def __init__(self,
                 alg_id: str = None,
                 **kwargs):
        super(SKLearnModel, self).__init__(alg_id, SRC_SKLEARN)
        self.__model = None
        self.__hparams = deepcopy(kwargs)
        self._model_info = {
            'alg_id': self.alg_id,
            'alg_name': self.alg_name,
            'alg_src': self.alg_src,
            'hparams': self.hparams
        }

        self.__init_model(**kwargs)

    def __init_model(self,
                     **kwargs):
        """
        Build a Scikit-learn model for given hyper-parameters.
        """

        if self.alg_id == ALG_LR:
            self.__model = LinearRegression()
        elif self.alg_id == ALG_LASSO:
            alpha = kwargs['alpha'] if 'alpha' in kwargs.keys() else 0.1
            max_iter = kwargs['max_iter'] if 'max_iter' in kwargs.keys() else 1000
            self.__model = Lasso(alpha=alpha, max_iter=max_iter)
        elif self.alg_id == ALG_DCTR:
            self.__model = DecisionTreeRegressor()
        elif self.alg_id == ALG_SYMR:
            population_size = kwargs['population_size'] if 'population_size' in kwargs.keys() else 1000
            generations = kwargs['generations'] if 'generations' in kwargs.keys() else 100
            p_subtree_mutation = kwargs['p_subtree_mutation'] if 'p_subtree_mutation' in kwargs.keys() else 0.01
            p_hoist_mutation = kwargs['p_hoist_mutation'] if 'p_hoist_mutation' in kwargs.keys() else 0.01
            p_point_mutation = kwargs['p_point_mutation'] if 'p_point_mutation' in kwargs.keys() else 0.01
            verbose = kwargs['verbose'] if 'verbose' in kwargs.keys() else 0
            self.__model = SymbolicRegressor(population_size=population_size, generations=generations,
                                             p_subtree_mutation=p_subtree_mutation, p_hoist_mutation=p_hoist_mutation,
                                             p_point_mutation=p_point_mutation, verbose=verbose)
        elif self.alg_id == ALG_KRR:
            alpha = kwargs['alpha'] if 'alpha' in kwargs.keys() else 1.0
            degree = kwargs['degree'] if 'degree' in kwargs.keys() else 3
            self.__model = KernelRidge(alpha=alpha, kernel='poly', degree=degree)
        elif self.alg_id == ALG_KNNR:
            n_neighbors = kwargs['n_neighbors'] if 'n_neighbors' in kwargs.keys() else 5
            p = kwargs['p'] if 'p' in kwargs.keys() else 2
            self.__model = KNeighborsRegressor(n_neighbors=n_neighbors, p=p)
        elif self.alg_id == ALG_GPR:
            kernel = DotProduct() + WhiteKernel()
            self.__model = GaussianProcessRegressor(kernel=kernel, alpha=1e-8)
        elif self.alg_id == ALG_SVR:
            c = kwargs['c'] if 'c' in kwargs.keys() else 1.0
            epsilon = kwargs['epsilon'] if 'epsilon' in kwargs.keys() else 0.1
            self.__model = SVR(C=c, epsilon=epsilon)
        elif self.alg_id == ALG_GBTR:
            max_depth = kwargs['max_depth'] if 'max_depth' in kwargs.keys() else 7
            n_estimators = kwargs['n_estimators'] if 'n_estimators' in kwargs.keys() else 300
            self.__model = XGBRegressor(max_depth=max_depth, n_estimators=n_estimators)
        else:
            raise AssertionError('Unknown Scikit-learn model \'{}\' was given.'.format(self.alg_id))

    @property
    def model(self):
        return self.__model

    @property
    def hparams(self):
        return self.__hparams

    def fit(self,
            dataset: Union[Dataset, MultimodalDataset]) -> SKLearnModel:
        """
        Fit model parameters of the prediction model to approximate the relationships between ``x`` and ``y``.

        :param dataset: (*Union[Dataset, MultimodalDataset]*) A training dataset to fit the model parameters.
        """

        if isinstance(dataset, Dataset):
            x = dataset.x.numpy()
        elif isinstance(dataset, MultimodalDataset):
            x = torch.hstack([d.x for d in dataset.datasets]).numpy()
        else:
            raise TypeError('A dataset of unsupported data type {} was given.'.format(dataset.__class__))

        if dataset.y is None:
            self.__model.fit(x)
        else:
            self.__model.fit(x, dataset.y.numpy().flatten())

        return self

    def predict(self,
                x: Union[torch.tensor, Dataset]) -> torch.Tensor:
        """
        Predict target values for the input data in ``dataset`` using the prediction model.
        If ``selected_dtypes`` is not ``None``, the prediction process is performed only for the selected data types.

        :param x: (*Union[torch.tensor, Dataset]*) A single input or dataset object containing multiple inputs.
        :return: (*torch.Tensor*) Predicted values for the input dataset.
        """

        if isinstance(x, torch.Tensor):
            _x = x.numpy().reshape(1, -1)
        else:
            _x = x.x

        return torch.tensor(self.__model.predict(_x).reshape(-1, 1))

    def save(self,
             path_model_file: str):
        """
        Save the model as a model file using the `Joblib package <https://joblib.readthedocs.io/en/latest/>`_.

        :param path_model_file: (*str*) Path of the model file.
        """

        joblib.dump(self.__model, path_model_file)

    def load(self,
             path_model_file: str):
        """
        Load the model parameters using the `Joblib package <https://joblib.readthedocs.io/en/latest/>`_.

        :param path_model_file: (*str*) Path of the model file.
        """

        self.__model = joblib.load(path_model_file)


class PyTorchModel(torch.nn.Module, Model):
    """
    An abstract class of the machine learning models based on PyTorch.
    All user-defined models from PyTorch must inherit this class.
    """

    @abstractmethod
    def __init__(self,
                 alg_id: str = None):
        torch.nn.Module.__init__(self)
        Model.__init__(self, alg_id, SRC_PYTORCH)

        # Model parameters.
        self.__params = self.parameters()

        # Layers of the neural network.
        self._layers = None

        # Output dimensionality of the model.
        self._dim_out = None

    def __str__(self) -> str:
        return torch.nn.Module.__str__(self)

    @property
    def params(self):
        return self.__params

    @property
    def layers(self):
        return self._layers

    @property
    def dim_out(self):
        return self._dim_out

    @abstractmethod
    def forward(self,
                x: object) -> torch.Tensor:
        """
        Execute the forward process of the prediction model.

        :param x: (*object*) Input data of the model.
        :return: (*torch.Tensor*) Output of the model for the input data.
        """

        pass

    @abstractmethod
    def fit(self,
            data_loader: DataLoader,
            optimizer: torch.optim.Optimizer,
            loss_func: torch.nn.Module):
        """
        Optimize the model parameters of the prediction model to minimize the given ``loss_func``.

        :param data_loader: (*DataLoader*) A data loader object for generating mini-batches from the training dataset.
        :param optimizer: (*torch.optim.Optimizer*) An optimization algorithm to fit the model parameters.
        :param loss_func: (*torch.nn.Module*) A loss function to fit the model parameters.
        """

        pass

    @abstractmethod
    def predict(self,
                dataset: Dataset) -> torch.Tensor:
        """
        Predict the target values for the input data ``x``.

        :param dataset: (*Dataset*) A dataset containing the input data.
        :return: (*torch.Tensor*) Predicted values for the input dataset.
        """

        pass

    def save(self,
             path_model_file: str):
        """
        Save the model as a model file using the `PyTorch package <https://pytorch.org/>`_.

        :param path_model_file: (*str*) Path of the model file.
        """

        torch.save(self.state_dict(), path_model_file)

    def load(self,
             path_model_file: str):
        """
        Load the model parameters using the `PyTorch package <https://pytorch.org/>`_.

        :param path_model_file: (*str*) Path of the model file.
        """

        if is_gpu_runnable():
            self.load_state_dict(torch.load(path_model_file))
        else:
            self.load_state_dict(torch.load(path_model_file, map_location=torch.device('cpu')))

    def init(self):
        """
        Initialize the prediction model.
        """

        if is_gpu_runnable():
            return self.cuda()
        else:
            return self
