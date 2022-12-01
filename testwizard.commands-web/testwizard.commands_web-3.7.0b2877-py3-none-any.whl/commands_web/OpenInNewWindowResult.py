from testwizard.commands_core.ResultBase import ResultBase


class OpenInNewWindowResult(ResultBase):
    def __init__(self, result, successMessage, failMessage):
        ResultBase.__init__(self, result["ok"] is True and result["errorCode"] == 0, successMessage, failMessage)

        self.handle = result["handle"]

        if self.success is True:
            return

        self.message = self.getMessageForErrorCode(self.message, result["errorCode"])
