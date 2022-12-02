import os
import logging

class ConfigManager():
    """
    This class is a helper to load and store configuration values from envvars
    For each parameter found in the list config_params, the method load_params gets
        config_params=[
                    {"name": "LOGLEVEL", "default": "INFO"},
                    {"name": "MQTT_HOST"},
                    {"name": "MQTT_PORT", "default": 1883},
                    {"name": "TOPIC_BASE_TIME_SERIE"},
                    {"name": "TOPIC_BASE_STATE"},
                    {"name": "TOPIC_NOTIFICATION"},
                    {"name": "TOPIC_AGENT"},
                    {"name": "DATABASE_NAME"},
                    {"name": "MYSQL_PV_HOST"},
                    {"name": "MYSQL_PV_USER"},
                    {"name": "MYSQL_PV_PASSWORD", "hide": True},
                    {"name": "DAILY_REPORT_TIME"},
                    {"name": "DAILY_REPORT_TIME", "default": "22:00"}
                   ]
        if a param has a default value, this value is stored if the envvar is not set
        if a param has no default value, and is not found from environment, the value is set as None and self.status is set as False
        if a param has hide = True, its value will be displayed as *****

    """
    def __init__(self, config_params, logger=None):
        """
        Instantiates a ConfigManager instance, and load values from environment for every param from config_params
        A  list of dicts loaded_config is created, for each param its name, default_value eventually and the read value
        :param config_params: a list of dicts, each dict represents a parameter: the key name is mandatory,
        the key "default" is not mandatory
        :param logger: if a logger instance is passed, use it, else creates a private logging instance
        """
        self.config_params = config_params
        self.loaded_config = []
        self.status = True
        if logger:
            self.logger = logger
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s')
            self.logger = logging.getLogger(__name__)
        self.load_params()

    def load_params(self):
        """
        loops over the elements of the self.config_params list
        For each one, get the envvar corresponding to the var name (param["name"])
        The params with their values are appended in self.loaded_config
        If something went wrong (ie a param could not be loaded) self.status is set to False
        :return:
        """
        all_ok = True
        status = {"name": "status", "value": True}
        for param in self.config_params:
            param_value = os.getenv(param["name"])
            hide_value= ("hide" in param and param["hide"])
            if param_value:
                param["value"] = param_value
                self.loaded_config.append(param)
                if hide_value:
                    self.logger.info(f"[ENVVAR OK]: {param['name']} = ********")
                else:
                    self.logger.info(f"[ENVVAR OK]: {param['name']} = {param_value}")
            elif not param_value and "default" in param:
                self.logger.info(f"{param['name']} env var not found, using default value {param['default']}")
                param_value  = param["default"]
                param["value"] = param_value
                self.loaded_config.append(param)
                if hide_value:
                    self.logger.info(f"[ENVVAR OK]: {param['name']} = ********")
                else:
                    self.logger.info(f"[ENVVAR OK]: {param['name']} = {param_value}")
            elif not param_value and "default" not in param:
                param["value"] = None
                self.logger.info(f"[ENVVAR KO]: {param['name']} = {param_value}")
                self.loaded_config.append(param)
                self.status = False

    def get_param(self, param_name):
        """
        return the value loaded for the given param name
        :param param_name:
        :return: the related value
        """
        param_value = None
        for param in self.loaded_config:
            if param['name'] == param_name:
                param_value =  param["value"]
                break
        if not param_value:
            self.logger.error(f"Value not found for param {param_name}")
        return param_value
