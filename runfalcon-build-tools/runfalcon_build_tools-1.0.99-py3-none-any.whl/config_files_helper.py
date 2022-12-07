import json
from typing import Dict
from runfalconbuildtools.file_utils import copy_dir, delete_directory, get_runfalcon_tmp_dir
from runfalconbuildtools.properties import Properties
from runfalconbuildtools.repository_helper import RepositoryHelper, Repository
from runfalconbuildtools.string_util import get_random_string

class ConfigFileHelper:

    __configuration_files_repository_ssh_url__ = 'ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/runfalcon-configuration'
    __configuration_files_repository_https_url__ = 'https://{git_user}:{git_key}@git-codecommit.us-east-1.amazonaws.com/v1/repos/runfalcon-configuration'

    def __set_value_in_json(self, json_object, key, value):
        index = key.find('.')
        if index < 0:
            if isinstance(value, bool):
                json_object[key] = bool(value)
            elif value.isnumeric():
                json_object[key] = int(value)
            else:
                json_object[key] = value
        else:
            base_key = key[0:index]
            new_key = key[index + 1:len(key)]
            self.__set_value_in_json(json_object[base_key], new_key, value)

    def __set_values_in_json_file(self, json_config_file_path:str, value_mapping:Dict, output_file_path:str = None):
        file = open(json_config_file_path, 'r')
        json_object = json.load(file)
        file.close()

        for item in value_mapping:
            for key in item:
                self.__set_value_in_json(json_object, key, item[key])

        return json_object

    def set_values_in_json_file(self, json_config_file_path:str, value_mapping:Dict, output_file_path:str = None) -> json:
        json_object:json = self.__set_values_in_json_file(json_config_file_path, value_mapping)
        if output_file_path != None:
            file = open(output_file_path, 'w')
            json.dump(json_object, file)
            file.close()
            return None
        return json_object

    def set_values_in_properties_file(self, properties_config_file_path:str, value_mapping:Dict, output_file_path:str = None) -> Properties:
        properties:Properties = Properties()

        properties.load(properties_config_file_path)
        
        for item in value_mapping:
            for key in item:
                properties.put(key, item[key])
        
        if output_file_path != None:
            properties.dump(output_file_path)
            return None
            
        return properties

    def __get_repository__(self, environment:str, git_user:str = None, git_key:str = None) -> Repository:
        url:str = None
        if git_user and git_key:
            url = self.__configuration_files_repository_https_url__.format(git_user = git_user, git_key = git_key)
        else:
            url = self.__configuration_files_repository_ssh_url__
        return Repository(url, environment)

    def get_config_files_from_repo(self, application:str, environment:str, outdir:str, git_user:str = None, git_key:str = None):
        repository:Repository = self.__get_repository__(environment, git_user, git_key)
        repository_helper:RepositoryHelper = RepositoryHelper(repository)
        out_dir:str = get_runfalcon_tmp_dir() + '/' + 'rf-' + get_random_string(10)
        repository_helper.get_source_artifacts(out_dir)
        copy_dir(out_dir + '/' + application, outdir)
        delete_directory(out_dir)
