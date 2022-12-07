from tracking_data.datarow.annotation import Annotation
from tracking_data.datarow.datarow_error import DatarowError
import cv2
import os

class Datarow:
    supported_video_formats = set({'avi', 'mp4'})
    supported_frame_formats = set({'jpg', 'jpeg', 'png'})

    @staticmethod
    def datarow_path_validate(path):
        if os.path.isdir(path):
            return True
        else:
            return False

    @staticmethod
    def validate_datarow(path):
        if not Datarow.datarow_path_validate(path):
            return DatarowError.WRONG_PATH
        try:
            dir_list = sorted(os.listdir(path), key=lambda x: int(os.path.splitext(x)[0]))
        except:
            return False, DatarowError.WRONG_FILES_ORDER
        for file in dir_list:
            format = file.split('.')[-1]
            if format not in Datarow.supported_frame_formats:
                return False, DatarowError.WRONG_FILES_TYPE
        return True, DatarowError.NONE

    @staticmethod
    def get_datarow_information(path):
        dir_list = os.listdir(path)
        frame = cv2.imread(os.path.join(path, dir_list[0]))
        height, width, _ = frame.shape
        frames_amount = len(os.listdir(path))
        return {"width": width, "height": height, "frames_amount": frames_amount}

    def __init__(self, name, path, annotation, width, height, frames_amount):
        self.name = name
        self.path = path
        self.annotation = annotation
        self.width = width
        self.height = height
        self.nframes = frames_amount

    def __str__(self):
        return f'Video datarow \"{self.name}\" with {str(self.nframes)} frames of shape {str(self.width)}x{str(self.height)}'

    @staticmethod
    def create(name, path, annotation_path):
        ok, err = Datarow.validate_datarow(path)
        if not ok:
            return err
        info = Datarow.get_datarow_information(path)
        annotation = Annotation.create(annotation_path)
        if annotation is None:
            return DatarowError.WRONG_ANNOTATION_FORMAT

        return Datarow(name, path, annotation, info['width'], info['height'], info['frames_amount'])

    def get_full_info(self):
        return {"name": self.name, "path": self.path, "gt": self.annotation, "width": self.width, "height": self.height,
                "#frames": self.nframes}

#a = Datarow.create("igor1", "/Users/rodion/Documents/trackers/python/sova_data/dataset/igor1", "/Users/rodion/Documents/trackers/python/sova_data/dataset/igor1.json")
#print(a.get_full_info())
