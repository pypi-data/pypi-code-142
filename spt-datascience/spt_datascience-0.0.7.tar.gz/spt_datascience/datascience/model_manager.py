from abc import abstractmethod

import ulid

from spt_datascience.datascience.model_util import ModelUtil, MongoModelUtil
from spt_datascience.datascience.models.base_model import BaseModel, ModelConfig
from functools import lru_cache
from spt_datascience.datascience.singleton import Singleton
from spt_datascience.datascience.models_storage import S3ModelStorage


class ModelManager(metaclass=Singleton):
    __slots__ = 'model_util', 'model_storage'

    def __init__(self, model_util, model_storage):
        self.model_util = model_util
        self.model_storage = model_storage

    @abstractmethod
    def get_model(self, model_id) -> BaseModel:
        """
        Return model object by id
        :param model_id: id of the model
        :return:
        """
        pass

    @abstractmethod
    def save_model(self, model) -> str:
        """
        Save model and return model id
        :param model: model inherit from BaseModel
        :return: model id
        """
        pass

    @abstractmethod
    def get_model_config(self, model_id) -> ModelConfig:
        """
        Return model object by id
        :param model_id: id of the model
        :return:
        """
        pass

    @abstractmethod
    def save_model_config(self, model_config):
        """
        Save model config
        :param model: model inherit from BaseModel
        """
        pass


class SPTModelManager(ModelManager):

    def __init__(self, spt_resource_factory, spt_ds_factory):
        model_util = MongoModelUtil(spt_resource_factory)
        model_storage = S3ModelStorage(spt_resource_factory)
        super().__init__(model_util, model_storage)

    @lru_cache(maxsize=512)
    def get_model(self, model_id) -> BaseModel:
        return self.model_storage.load_model(
            model_id=model_id
        )

    def save_model(self, model: BaseModel) -> str:
        model_name = model.model_name()
        model_version = self.increment_model_version(
            self.model_util.get_model_version(model_name)
        )
        model_id = self.produce_model_id(model_name, model_version)
        model_config = self.model_storage.save_model(model, model_id, model_version)
        self.model_util.save_model_config(model_config)
        return model_id

    def produce_model_id(self, model_name, model_version):
        return f"{model_name}{model_version}#{ulid.new().str}"

    def increment_model_version(self, version):
        return version + 1

    def get_model_config(self, model_id):
        return self.model_storage.load_model_config(model_id)

    def save_model_config(self, model_config):
        model_config = self.model_storage.upload_model_bins(model_config)
        self.model_util.save_model_config(model_config)

    def delete_model(self, model_id):
        self.model_storage.delete_model(model_id)
