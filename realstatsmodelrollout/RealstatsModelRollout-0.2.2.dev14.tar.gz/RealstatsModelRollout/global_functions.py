import os
from six import string_types


class globalFunctions:
    def __init__(self):
        self._id = "Optional"

    # get index location of char in string #
    def Find(s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def Path_is_dir(localpath=""):
        local_envpath = ""
        # Get directory #
        print("Looking for directory")
        if localpath[-1] == '/':
            local_envpath = localpath
        else:
            local_envpath = localpath + "/"

        isDirectory = os.path.isdir(local_envpath)
        if isDirectory is True:
            return local_envpath
        else:
            raise Exception("Given localpath: " + local_envpath + " is not a directory")

    def Check_instance(check, instance_type):
        if instance_type == "string":
            if isinstance(check, string_types):
                return check
            else:
                return Exception("Type is not string")
        elif instance_type == "float":
            if isinstance(check, float):
                return check
            else:
                return Exception("Type is not float")
        elif instance_type == "int":
            if isinstance(check, int):
                return check
            else:
                return Exception("Type is not int")
        elif instance_type == "list":
            if isinstance(check, list):
                return check
            else:
                return Exception("Type is not list")
