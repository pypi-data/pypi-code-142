import pandas as pd
import datatest as dt
from datetime import datetime

def strftime_format(format):
    def func(value):
        try:
            datetime.strptime(value, format)
        except ValueError:
            return False
        return True
    func.__doc__ = f'should use date format {format}'
    return func

class df_data_validator:
    def __init__(self,dataframe):
        self.dataframe=dataframe

    def checkDatatype(self,field,requirement):
        try:
            dt.validate(self.dataframe[field], requirement)
        except Exception as e:
            return "{0} is not a valid datatype for {1} field".format(requirement,field), e
        else:
            return "{0} is a valid datatype for {1} field ".format(requirement,field),dt.validate(self.dataframe[field], requirement)

    def checkDuplicatesAllCol(self):
        lst=list(self.dataframe.columns)
        dup=self.dataframe[self.dataframe.duplicated(lst)]
        if len(dup.index)==0:
            return "No Duplicates"
        return "Duplicates rows present",self.dataframe[self.dataframe.duplicated(lst)]

    def checkDuplicates(self,columnList):
        dup=self.dataframe[self.dataframe.duplicated(columnList)]
        if len(dup.index)==0:
            return "No Duplicates"
        return "Duplicates present",self.dataframe[self.dataframe.duplicated(columnList)]
   

    def checkDateStrings(self, column):
        try:
            dt.validate(self.dataframe[column], strftime_format('%Y-%m-%d'))
        except Exception as e:
            return "Invalid date string for {0} column".format(column), e
        else:
            return "Valid date string for {0} column ".format(column)

    def checkDateTimeStrings(self,column):
        try:
            dt.validate(self.dataframe[column], strftime_format('%Y-%m-%d %H:%M:%S.%f'))
        except Exception as e:
            return "Invalid date string for {0} column".format(column), e
        else:
            return "Valid date string for {0} column ".format(column)

    def checkIfNulls(self):
        if True in list(self.dataframe.isnull().all()):
            dict={}
            for col in self.dataframe.columns:
                dict[col]=self.dataframe[self.dataframe[col].isnull()].index.tolist()
            return dict
        return "No NULL are presents"

    def checkNegative(self,column):
        if True in list(self.dataframe[self.dataframe[column]<0].all()):
            return self.dataframe[self.dataframe[column]<0].index.tolist()
        return "No Negative"

    def checkRange(self,column,lowerLimit, upperLimit):
        if False in list(self.dataframe[column].between(lowerLimit,upperLimit,inclusive=True)):
            a=self.dataframe[column].between(lowerLimit,upperLimit,inclusive=True)
            b=[not elem for elem in a]
            return self.dataframe[b].index.tolist()
        return "All row values lies within the range."


