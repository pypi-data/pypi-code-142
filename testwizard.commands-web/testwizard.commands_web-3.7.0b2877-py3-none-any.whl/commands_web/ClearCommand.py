import sys
import json

from testwizard.commands_core import CommandBase
from testwizard.commands_core.OkErrorCodeAndMessageResult import OkErrorCodeAndMessageResult


class Clear(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.Clear")

    def execute(self, selector):
        if selector is None:
            raise Exception("selector is required")

        requestObj = [selector]

        result = self.executeCommand(requestObj)

        return OkErrorCodeAndMessageResult(result, "Clear was successful", "Clear failed")
