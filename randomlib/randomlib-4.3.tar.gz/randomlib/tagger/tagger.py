from randomlib.modelRepo.mahaNER import NERModel

class EntityRecognizer(NERModel):

    def __init__(self):
        self.modelName = 'marathi-ner'
        super().__init__(self.modelName)

    def getTokenLabels(self, text, details: str = "minimum", as_dict: bool = False):
        return super().getTokenLabels(text, details, as_dict)

    def getTokens(self, text):
        return super().getTokens(text)

    def listModels(self):
        return super().listModels()