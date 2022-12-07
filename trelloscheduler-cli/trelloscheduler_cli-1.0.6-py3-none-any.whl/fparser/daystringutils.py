# Author: Olin Gallet
# Date: 24 Oct 2022
#
# DayStringUtils provides different utilities for parsing a day string.
from datetime import date

class DayStringUtils:
    def __init__():
        pass

    @staticmethod
    def getDayNames(query:str):
        """Parses a string of abbreviated days into an array of full days

        :param: query the query of abbreviated day names
        :type: str

        :return: an array of full day names represented
        :rtype: str[]
        """
        days = []
        if 'Su' in query:
            days.append('Sunday')
        if 'Mo' in query:
            days.append('Monday')
        if 'Tu' in query:
            days.append('Tuesday')
        if 'We' in query:
            days.append('Wednesday')
        if 'Th' in query:
            days.append('Thursday')
        if 'Fr' in query:
            days.append('Friday')
        if 'Sa' in query:
            days.append('Saturday')
        return days

    @staticmethod
    def getDayInCurrentMonth(day:str):
        """Puts the given numerical day into the current month and year

        :param: day the numerical day
        :type: str

        :return: the day in yyyy-mm-dd format
        :rtype: str
        """
        return str(date.today().year) + '-' + str(date.today().month) + '-' + day 
