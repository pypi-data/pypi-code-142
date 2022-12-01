import sys
import json

from testwizard.commands_core import SessionCommandBase
from testwizard.commands_core import OkErrorCodeAndMessageResult

class CancelCommandsCommand(SessionCommandBase):
    def __init__(self, session):
        SessionCommandBase.__init__(self, session, "CancelCommands")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "CancelCommands was successful", "CancelCommands failed")