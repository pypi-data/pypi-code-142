import json
from tracking_data.datarow.datarow_error import DatarowError

class Annotation:
    @staticmethod
    def return_value(error_code=DatarowError.NONE):
        status = None
        if error_code == DatarowError.NONE:
            status = True
        else:
            status = False
        return (status, error_code)

    @staticmethod
    def create(path):
        format = path.split('.')[-1]
        if format != 'json':
            return None
        gt = json.load(open(path, 'r'))
        try:
            images = gt['images']
            annotations = gt['annotations']
        except:
            return None
        return Annotation(gt)

    def __init__(self, gt):
        self.__gt = gt
        self.__images = self.__gt['images']
        self.__annotations = self.__gt['annotations']

    def get(self, image_name):
        id_list = [i['id'] for i in self.__images if i['file_name'] == image_name]
        if id_list == []:
            return None
        image_id = id_list[0]
        #print(image_id)

        info = self.__annotations[image_id]
        return info['bbox']
