import os
from collections import namedtuple
import pathlib

fields_cor = "folder file path ext"
classname_cor = "files"

FilePathInfos = namedtuple(classname_cor, fields_cor)


def get_folder_file_complete_path(folders):
    if isinstance(folders,str):
        folders=[folders]
    listOfFiles2 = ()
    for dirName in folders:
        for (dirpath, dirnames, filenames) in os.walk(dirName):
            listOfFiles2 += tuple(
                FilePathInfos(
                    dirpath,
                    file,
                    os.path.normpath(os.path.join(dirpath, file)),
                    pathlib.Path(file).suffix,
                )
                for file in filenames
            )
    return listOfFiles2

