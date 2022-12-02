"""
Encoder
"""
from typing import Dict


class UniqueFieldError(Exception):
    """UniqueFieldError"""


class Encoder:
    """
    Encoder
    """
    form_dict: Dict

    def __init__(self, form_dict: Dict):
        self.form_dict = form_dict

    @staticmethod
    def parse_params(params: str) -> Dict:
        """
        :param params:
        :type params:
        :return:
        :rtype:
        """
        fields = {}
        param_list = params[1:]
        param_list = param_list.split("&")
        for p in param_list:
            try:
                name, value = p.split("=")
            except ValueError:
                # string contains no form params
                return {}
            # ensure field names should be unique RFC7578 1.3
            if name in fields:
                raise UniqueFieldError("field names must be unique")
            fields[name] = {"name": name, "value": value}
        return fields
