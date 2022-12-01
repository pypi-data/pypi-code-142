import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class MultiAction_Perform(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.MultiAction_Perform")

    def execute(self):
        requestObj = []

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "MultiAction_Perform was successful", "MultiAction_Perform failed")
