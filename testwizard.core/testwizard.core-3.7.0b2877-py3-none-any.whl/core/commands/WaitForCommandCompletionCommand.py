import sys
import json

from testwizard.commands_core import SessionCommandBase
from testwizard.commands_core import OkErrorCodeAndMessageResult

class WaitForCommandCompletionCommand(SessionCommandBase):
    def __init__(self, session):
        SessionCommandBase.__init__(self, session, "WaitForCommandCompletion")

    def execute(self, timeout=None):
        requestObj = [timeout]

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "WaitForCommandCompletion was successful", "WaitForCommandCompletion failed")