"""utilities"""
from os.path import exists, expanduser
from os import mkdir
import yaml

class HiddenPassword(object):
    def __init__(self, password=''):
        self.password = password
    def __str__(self):
        return '*' * len(self.password)

def return_yaml() -> dict:
    """Returns yaml configurations

    Returns:
        _type_: _description_
    """
    home = expanduser('~')
    base_dir = f"{home}/.config"
    if not exists(f"{home}/.config"):
        mkdir(base_dir)
    filename = f"{base_dir}/.sase_push"
    with open(filename, 'r') as yam:
        yaml_config = yaml.safe_load(yam)
    return yaml_config

if __name__ == '__main__':
    config = return_yaml()
    print(config)