from enum import Enum

class DatarowError(Enum):
    NONE = 0,
    WRONG_PATH = 1,
    WRONG_FILES_ORDER = 2,
    WRONG_FILES_TYPE = 3,
    WRONG_ANNOTATION_FORMAT = 4
