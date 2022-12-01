import sys
import json

from testwizard.commands_core import CommandBase
from .StartWebDriverResult import StartWebDriverResult


class StartWebDriver(CommandBase):
    def __init__(self, testObject):
        CommandBase.__init__(self, testObject, "Selenium.StartWebDriver")

    def execute(self, browser, serverUrl):
        requestObj = []
        if browser is not None:
            requestObj = [browser]
            if serverUrl is not None:
                requestObj = [browser, serverUrl]

        result = self.executeCommand(requestObj)

        return StartWebDriverResult(result, "StartWebDriver was successful", "StartWebDriver failed")
