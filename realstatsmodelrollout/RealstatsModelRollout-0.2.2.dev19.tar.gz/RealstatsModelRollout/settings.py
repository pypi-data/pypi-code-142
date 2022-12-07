import os
from .global_functions import globalFunctions as GF


class Settings:
    def __init__(self):
        self._base_path = ""
        self._premade_main_code_data = ""
        self._premade_ms_init_code = ""
        self._premade_function_code_data = ""
        self._premade_train_code = ""
        self._premade_requirements_data = ""
        self._premade_documentation_data = ""
        self._enviroment_name = ""
        self._enviroment_version = ""
        self._package_version = ""
        self._base_url = ""
        self._username = ""
        self._token = ""
        self._platform_version = ""
        self._gitaccesstoken = ""
        self._validation_data_path = ""
        self._validation_control_data_path = ""

    # Base path that will be used by the system to work with the system and work from #
    @property
    def Base_path(self):
        """
        :type: string
        """
        return self._base_path

    @Base_path.setter
    def Base_path(self, value):
        """
        :type: string
        """
        self._base_path = GF.Path_is_dir(value)

    # Premade code that can be used when not using custom code #
    @property
    def Premade_main_code_data(self):
        """
        :type: string
        """
        return self._premade_main_code_data

    @Premade_main_code_data.setter
    def Premade_main_code_data(self, value):
        """
        :type: string
        """
        self._premade_main_code_data = GF.Check_instance(check=value, instance_type="string")

    # Premade function code that can be used when not using custom code #
    @property
    def Premade_ms_function_code_data(self):
        """
        :type: string
        """
        return self._premade_function_code_data

    @Premade_ms_function_code_data.setter
    def Premade_ms_function_code_data(self, value):
        """
        :type: string
        """
        self._premade_function_code_data = GF.Check_instance(check=value, instance_type="string")

    # Premade function code that can be used when not using custom code #
    @property
    def Premade_ms_init_code(self):
        """
        :type: string
        """
        return self._premade_ms_init_code

    @Premade_ms_init_code.setter
    def Premade_ms_init_code(self, value):
        """
        :type: string
        """
        self._premade_ms_init_code = GF.Check_instance(check=value, instance_type="string")

    # Premade train code that can be used when not using custom code #
    @property
    def Premade_ms_train_code(self):
        """
        :type: string
        """
        return self._premade_train_code

    @Premade_ms_train_code.setter
    def Premade_ms_train_code(self, value):
        """
        :type: string
        """
        self._premade_train_code = GF.Check_instance(check=value, instance_type="string")

    # Premade requirements list that can be used when not using custom code #
    @property
    def Premade_requirements_data(self):
        """
        :type: string
        """
        return self._premade_requirements_data

    @Premade_requirements_data.setter
    def Premade_requirements_data(self, value):
        """
        :type: string
        """
        self._premade_requirements_data = GF.Check_instance(check=value, instance_type="string")

    # Premade documentation that can be used when not using custom code #
    @property
    def Premade_documentation_data(self):
        """
        :type: string
        """
        return self._premade_documentation_data

    @Premade_documentation_data.setter
    def Premade_documentation_data(self, value):
        """
        :type: string
        """
        self._premade_documentation_data = GF.Check_instance(check=value, instance_type="string")

    @property
    def Enviroment_name(self):
        """
        :type: string
        """
        return self._enviroment_name

    @Enviroment_name.setter
    def Enviroment_name(self, value):
        """
        :type: string
        """
        self._enviroment_name = GF.Check_instance(check=value, instance_type="string")

    @property
    def Enviroment_version(self):
        """
        :type: string
        """
        return self._enviroment_version

    @Enviroment_version.setter
    def Enviroment_version(self, value):
        """
        :type: string
        """
        self._enviroment_version = GF.Check_instance(check=value, instance_type="string")

    @property
    def Package_version(self):
        """
        :type: string
        """
        return self._package_version

    @Package_version.setter
    def Package_version(self, value):
        """
        :type: string
        """
        self._package_version = GF.Check_instance(check=value, instance_type="string")

    @property
    def Base_url(self):
        """
        :type: string
        """
        return self._base_url

    @Base_url.setter
    def Base_url(self, value):
        """
        :type: string
        """
        self._base_url = GF.Check_instance(check=value, instance_type="string")

    @property
    def Username(self):
        """
        :type: string
        """
        return self._username

    @Username.setter
    def Username(self, value):
        """
        :type: string
        """
        self._username = GF.Check_instance(check=value, instance_type="string")

    @property
    def Token(self):
        """
        :type: string
        """
        return self._token

    @Token.setter
    def Token(self, value):
        """
        :type: string
        """
        self._token = GF.Check_instance(check=value, instance_type="string")

    @property
    def Platform_version(self):
        """
        :type: string
        """
        return self._platform_version

    @Platform_version.setter
    def Platform_version(self, value):
        """
        :type: string
        """
        self._platform_version = value[0:4]

    @property
    def Gitaccesstoken(self):
        """
        :type: string
        """
        return self._gitaccesstoken

    @Gitaccesstoken.setter
    def Gitaccesstoken(self, value):
        """
        :type: string
        """
        self._gitaccesstoken = GF.Check_instance(check=value, instance_type="string")
