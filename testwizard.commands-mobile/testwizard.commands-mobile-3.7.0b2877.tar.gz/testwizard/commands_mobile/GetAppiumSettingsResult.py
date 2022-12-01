import json
import sys

from testwizard.commands_core.ResultBase import ResultBase

class GetAppiumSettingsResult(ResultBase):
    def __init__(self, result, successMessage, failMessage):
        ResultBase.__init__(self, result["ok"] is True, successMessage, failMessage + ": " + result["errorMessage"])

        self.settings = json.loads(result["settings"])