from randomlib.modelRepo.mahaHate import HateModel

class HateAnalyzer(HateModel):
    def __init__(self):
        self.modelName = 'mahahate-bert'
        super().__init__(self.modelName)

    def getHateScore(self, text):
        return super().getHateScore(text)

    def listSupportedLabels(self):
        return super().listSupportedLabels()
        
    def listModels(self):
        return super().listModels()
