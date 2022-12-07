from trello import TrelloClient
import datetime
from .system.jsonloader import JsonLoader
from .fparser.daystringutils import DayStringUtils

# Author: Olin Gallet
# Date: 14 Oct 2022                             
#
# The Trellobot performs various tasks for weekly scheduling.  They are:
# 1.  Creating a weekly board.
# 2.  Archiving the lists on the weekly board by moving them to a "Recycling Bin" board.
# 3.  Creating the lists for the weekly board.
# 4.  Uploading a schedule to post on the weekly board.

class TrelloBot:
    def __init__(self, trello_api:str, trello_secret:str, trello_token:str):
        """
        Initializes the TrelloBot.

        :param: trelloapi: the Trello API key
        :type: trelloapi: str
        :param: trellosecret: the Trello secret key
        :type: trellosecret: str
        :param: trellotoken: the Trello token
        :type: trellotoken: str
        """
        self._trello_client = TrelloClient(trello_api, trello_secret, trello_token)
        self._WEEKLY_BOARD = 'Weekly Schedule'
        self._RECYCLE_BIN_BOARD = 'Recycle Bin'

    def _get_board_by_name(self, name:str):
        #Gets the weekly board.
        response = None
        target = [board for board in self._trello_client.list_boards() if board.name == name]
        if len(target) > 0:
            response = target[0]
        return response

    def build_boards(self):
        """Creates the weekly board and recycle bin board.  
        """
        self._trello_client.add_board(self._WEEKLY_BOARD)
        self._trello_client.add_board(self._RECYCLE_BIN_BOARD)
        self.archive_all_lists()                              

    def create_weekly_lists(self):
        """Creates seven lists representing today and the next six days of the week.
        """
        day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(0, 7):
            day = datetime.date.today() + datetime.timedelta(days=i)
            self._get_board_by_name(self._WEEKLY_BOARD).add_list(name = day_name[day.weekday()] + '::' + str(day))

    def upload_schedule(self, filename:str):
        """Uploads the given schedule to the weekly list.
        
        :param: schedule a json schedule file representing the schedule to add
        :type: str
        """
        for task in JsonLoader.load(filename)['tasks']:
            taskdays = DayStringUtils.getDayNames(task['day'])
            if len(taskdays) == 0:
                taskdays = [DayStringUtils.getDayInCurrentMonth(task['day'])]
            for list in self._get_board_by_name(self._WEEKLY_BOARD).all_lists():
                for day in taskdays:                        
                    if day == list.name.split("::")[0] or day == list.name.split("::")[1]:
                        list.add_card(task['name'], task['description'])

    def archive_all_lists(self):
        """Archives all lists in the weekly board.
        """
        for list in self._get_board_by_name(self._WEEKLY_BOARD).all_lists():
            list.move_to_board( self._get_board_by_name(self._RECYCLE_BIN_BOARD))