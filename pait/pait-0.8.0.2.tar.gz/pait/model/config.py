from json import JSONEncoder
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Set, Tuple, Type

from pydantic import BaseConfig

from pait.model.response import PaitBaseResponseModel
from pait.model.status import PaitStatus
from pait.util import CustomJSONEncoder, I18nTypedDict, change_local
from pait.util import i18n_config_dict as pait_i18n_config_dict
from pait.util import i18n_local as pait_i18n_local
from pait.util import json_type_default_value_dict as pait_json_type_default_value_dict
from pait.util import python_type_default_value_dict as pait_python_type_default_value_dict

if TYPE_CHECKING:
    from pait.model.core import PaitCoreModel

APPLY_FN = Callable[["PaitCoreModel"], None]


__all__ = ["Config", "APPLY_FN"]


class Config(object):
    """
    Provide pait parameter configuration, the init_config method is valid only before the application service is started
    """

    __initialized: bool = False

    def __init__(self) -> None:
        self.author: Tuple[str, ...] = ("",)
        self.status: PaitStatus = PaitStatus.undefined
        self.block_http_method_set: Set[str] = set()
        self.default_response_model_list: List[Type[PaitBaseResponseModel]] = []
        self.json_encoder: Type[JSONEncoder] = CustomJSONEncoder
        self.default_pydantic_model_config: Type[BaseConfig] = BaseConfig
        self.tag_dict: Dict[str, str] = {}
        self.i18n_local: str = pait_i18n_local
        self.apply_func_list: List[APPLY_FN] = []

    def __setattr__(self, key: Any, value: Any) -> None:
        if not self.__initialized:
            super().__setattr__(key, value)
        else:
            raise RuntimeError("Can not set new value in runtime")

    def init_config(
        self,
        author: Optional[Tuple[str, ...]] = None,
        status: Optional[PaitStatus] = None,
        json_type_default_value_dict: Optional[Dict[str, Any]] = None,
        python_type_default_value_dict: Optional[Dict[type, Any]] = None,
        json_encoder: Optional[Type[JSONEncoder]] = None,
        i18n_local: str = pait_i18n_local,
        i18n_config_dict: Optional[Dict[str, I18nTypedDict]] = None,
        apply_func_list: Optional[List[APPLY_FN]] = None,
    ) -> None:
        """
        :param author:  Only @pait(author=None) will be called to change the configuration
        :param status:  Only @pait(status=None) will be called to change the configuration
        :param json_type_default_value_dict: Configure default values for each json type
        :param python_type_default_value_dict: Configure default values for each python type
        :param json_encoder: Define certain types of serialization rules
        :param i18n_local: Select the default i18 language
        :param i18n_config_dict: Update i18n-related configuration
        :param apply_func_list: List of functions for application configuration
        :return:
        """
        if self.__initialized:
            raise RuntimeError("Can not set new value in runtime")
        if author:
            self.author = author
        if status:
            self.status = status

        if json_type_default_value_dict:
            pait_json_type_default_value_dict.update(json_type_default_value_dict)
        if python_type_default_value_dict:
            pait_python_type_default_value_dict.update(python_type_default_value_dict)
        if json_encoder:
            self.json_encoder = json_encoder
        if i18n_local:
            change_local(i18n_local)
        if i18n_config_dict:
            pait_i18n_config_dict.update(i18n_config_dict)
        if apply_func_list:
            self.apply_func_list = apply_func_list
        self.__initialized = True

    @property
    def initialized(self) -> bool:
        """Judge whether it has been initialized, it can only be initialized once per run"""
        return self.__initialized
