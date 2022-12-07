# Author: Olin Gallet
# Date: 22 Oct 2022
#
# The EnvironmentVarsNotSetException represents when the necessary environment
# variables are not set for the Trellobot.

class EnvironmentVarsNotSetException(Exception):

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return 'The environment variables necessary for operation are not set.  Make sure your ~/.bashrc has TRELLO_API_KEY, TRELLO_API_SECRET, and TRELLO_TOKEN are set.'
