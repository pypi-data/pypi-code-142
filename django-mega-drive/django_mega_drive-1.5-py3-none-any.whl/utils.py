from typing import List, Union

from django.db.models.fields.files import FieldFile, ImageFieldFile

FileFields = List[Union[FieldFile, ImageFieldFile]]


def delete_drive_files(fields: FileFields, empty_trash: bool = False) -> None:

    for file in fields:
        file.storage.delete(file.name)
    if empty_trash:
        file[0].storage.empty_trash()
