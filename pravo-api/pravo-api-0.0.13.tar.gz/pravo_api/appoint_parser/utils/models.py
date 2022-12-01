from pathlib import Path
from typing import List, Union
from pydantic import BaseModel, validator


class Person(BaseModel):
    raw_name: str = ''
    lemm_name: str = ''
    gender:str = ''
    fio: dict = {}

    @validator('raw_name', pre=True)
    def pre_prep(cls, v):
        return ' '.join(v.split())

class AppoitmentLine(BaseModel):
    raw_line: Union[str,None] = ''
    appointees: List[Person] = [] # список людей, которых назначили 
    resignees: List[Person] = []
    position: Union[str, None] = ''


class FileData(BaseModel):
    doc_id:str=None
    file_name : str = None
    file_path : Union[str, Path] = None
    date : str = None
    text_raw : Union[str, None] = None
    splitted_text:List[str]=None
    url : str = None
    appointment_lines: List[AppoitmentLine] = [] # events
    author:str = None # кто подписал
    naznach_line:str = None
    region:str = None
    

