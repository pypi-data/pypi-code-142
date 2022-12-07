import os
import datetime
import csv
from enum import Enum

class GET(Enum):
    ALL = 0
    NAME = 1
    DESCRIPTION = 2
    START_TIME = 3
    END_TIME = 4

class TSV_Read():
    def __init__(self, file:str):
        extension = os.path.splitext(file)[-1]
        if(extension!=".tsv"):
            raise NameError("File has to be .tsv")
        self.file = file

    def _get_info(self, value:GET, line:str):
        match value:
            case GET.ALL:
                return(line)
            case GET.NAME:
                return(line[1])
            case GET.DESCRIPTION:
                return(line[2])
            case GET.START_TIME:
                return datetime.timedelta(hours=int(line[3][0:2]), minutes=int(line[3][2:4]))
            case GET.END_TIME:
                return datetime.timedelta(hours=int(line[4][0:2]), minutes=int(line[4][2:4]))

    def all(self, value:GET=GET.ALL):
        tsv_file = csv.reader(open(self.file), delimiter="\t")
        info_return = []
        for line in tsv_file:
            info_return.append(self._get_info(value, line))
        return info_return
    def today(self, value:GET=GET.ALL):
        tsv_file = csv.reader(open(self.file), delimiter="\t")
        info_return = []
        for line in tsv_file:
            if(datetime.datetime.now().weekday()==int(line[0])):
                info_return.append(self._get_info(value, line))
        return info_return
    def next(self, value:GET=GET.ALL):
        tsv_file = csv.reader(open(self.file), delimiter="\t")
        for line in tsv_file:
            if(datetime.datetime.now().weekday()==int(line[0])):
                currenttime = datetime.datetime.now().strftime("%H%M")
                if(currenttime < line[3]):
                    return self._get_info(value, line)
        return("No next Event!")
    def current(self, value:GET=GET.ALL):
        if isinstance(value, GET):
            tsv_file = csv.reader(open(self.file), delimiter="\t")
            for line in tsv_file:
                if(datetime.datetime.now().weekday()==int(line[0])):
                    currenttime = datetime.datetime.now().strftime("%H%M")
                    if(line[3] < currenttime and currenttime < line[4]):
                        return self._get_info(value, line)
            return("No current Event!")
        else:
            raise TypeError("Argument must be of Type tsv_calendar.GET")
