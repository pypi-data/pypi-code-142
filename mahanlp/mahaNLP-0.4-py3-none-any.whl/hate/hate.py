from mahaNLP.modelRepo.mahaHate import HateModel

class HateAnalyzer(HateModel):
    def __init__(self):
        self.modelName = 'mahahate-bert'
        super().__init__(self.modelName)

    def getPolarityScore(self, text):
        return super().getPolarityScore(text)

    def listModels(self):
        return super().listModels()
