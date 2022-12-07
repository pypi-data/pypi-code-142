import json
from tracking_data.datarow.datarow import Datarow
from tracking_data.dataset_error import DatasetError

class Dataset:
    def __init__(self, storage):
        self.storage = storage

    def __str__(self):
        return f'Video dataset with {self.size()} datarows.'

    @staticmethod
    def load(path):
        try:
            json_file = json.load(open(path, 'r'))
        except:
            return DatasetError.FILE_NOT_FOUND

        storage = {}
        for video_name in json_file:
            storage[video_name] = Datarow.create(video_name, json_file[video_name]['dir'], json_file[video_name]['GT'])
        return Dataset(storage)

    def get(self, name):
        if name in self.storage:
            return self.storage[name]
        else:
            return None

    def video_names(self):
        return self.storage.keys()

    def size(self):
        return len(self.storage.keys())

#dataset = Dataset.load('../videos.json')
#print(dataset.video_names())
#print(dataset.get('igor1_1'))
#print(dataset)
#print(type(dataset.get['igor1_1']))
#datarow.Datarow()
#a = Datarow.create("igor1", "/Users/rodion/Documents/trackers/python/sova_data/dataset/igor1", "/Users/rodion/Documents/trackers/python/sova_data/dataset/igor1.json")
