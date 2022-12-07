import json

# Author: Olin Gallet
# Date: 14 Oct 2022
#
# The JsonLoader loads up a json file as is.

class JsonLoader:
    def __init__():
        pass

    @staticmethod
    def load(filename: str):
        """Loads the provided filename as a json array.

        :return: a json array of the file
        :rtype: Array
        """
        tasks_data = []
        with open(filename, 'r') as tasks_file:
            tasks_data = json.load(tasks_file)
        return tasks_data
    