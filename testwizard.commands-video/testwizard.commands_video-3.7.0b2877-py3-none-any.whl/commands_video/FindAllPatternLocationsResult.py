import json
import sys

from testwizard.commands_core.ResultBase import ResultBase


class FindAllPatternLocationsResult(ResultBase):
    def __init__(self, result, successMessage, failMessage):
        ResultBase.__init__(
            self, result["errorCode"] == 0, successMessage, failMessage)

        self.matches = result["matches"]
        self.numberOfMatches = result["numberOfMatches"]

        if self.success is True:
            return

        self.message = self.getMessageForErrorCode(self.message, result["errorCode"])
