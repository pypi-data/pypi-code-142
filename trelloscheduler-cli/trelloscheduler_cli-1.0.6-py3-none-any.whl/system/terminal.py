# Author: Olin Gallet
# Date: 22 Oct 2022
#
# The Terminal contains various ways to display commands on the terminal.
from plumbum import colors

class Terminal:
    def __init__(self):
        pass

    @staticmethod
    def display_usage_help():
        """Displays usage help message and possible parameters for the Trellobot.
        """
        print(colors.orchid | '[Usage]')
        print(colors.blue | '  python3 trellobot [command : startweek OR buildweek OR endweek OR loadweek] [schedule file IF loadweek]')
        print(colors.yellow | '  Trello bot is used to automate tasks related to creating a weekly schedule in Trello.')
        print(colors.yellow | '  All you need is a valid Trello account to access the various commands.')

    @staticmethod
    def display_buildweek_help():
        """Displays help message for the buildweek command.
        """
        print(colors.blue | '  buildweek')
        print(colors.yellow | '  EX: python3 trellobotrunner.py buildweek')
        print()
        print(colors.yellow | '  Create a new weekly schedule board and recycle bin board.  They will show up as "Weekly Schedule"')
        print(colors.yellow | ' and "Recycle Bin" in Trello.')
        print(colors.yellow | '  Does not need to be executed more than once.')

    @staticmethod
    def display_startweek_help():
        """Displays help message for the startweek command.
        """
        print(colors.blue| '  startweek')
        print(colors.yellow | '  EX: python3 trellobotrunner.py startweek')
        print()
        print(colors.yellow | '  Starts a week by adding empty lists to the "Weekly Schedule" board.')

    @staticmethod
    def display_endweek_help():
        """Displays help message for the endweek command.
        """
        print(colors.blue | '  endweek')
        print(colors.yellow | '  EX: python3 trellobotrunner.py endweek')
        print()
        print(colors.yellow | '  Archives all of the lists in the "Weekly Schedule" board.')

    @staticmethod
    def display_loadweek_help():
        """Displays help message for the loadweek command.
        """
        print(colors.blue | '  loadweek')
        print(colors.yellow | '  EX: python3 trellobotrunner.py loadweek "filename"')
        print()
        print(colors.yellow | '  Loads a schedule file in JSON format into the "Weekly Schedule" board.')
        print(colors.yellow | '  Currently supports named days and numerical days.')  

    @staticmethod    
    def display_full_help():
        """Displays the full help message for all commands.
        """
        Terminal.display_usage_help()
        print(colors.orchid | '[Commands]')
        Terminal.display_buildweek_help()
        print()
        Terminal.display_startweek_help()
        print()
        Terminal.display_endweek_help()
        print()
        Terminal.display_loadweek_help()
        print()
        print(colors.green| '<<Shell script originally made by Olin Gallet October 2022>>')

    @staticmethod
    def display_buildweek_completion():
        """Displays the build week message for completion.
        """
        print(colors.orchid | '[Success] >> Build week board command successful.')

    @staticmethod
    def display_startweek_completion():
        """Displays the build week message for completion.
        """
        print(colors.orchid | '[Success] >> Create weekly lists command successful.')

    @staticmethod
    def display_endweek_completion():
        """Displays the build week message for completion.
        """
        print(colors.orchid | '[Success] >> Archive all lists command successful.')

    @staticmethod
    def display_loadweek_completion():
        """Displays the load week message for completion.
        """
        print(colors.orchid | '[Success] >> All lists loaded from file successfully.')

