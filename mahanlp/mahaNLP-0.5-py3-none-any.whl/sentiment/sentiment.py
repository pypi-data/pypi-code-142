from mahaNLP.modelRepo.mahaSentiment import SentimentModel

class SentimentAnalyzer(SentimentModel):
    def __init__(self):
        self.modelName = 'MarathiSentiment'
        super().__init__(self.modelName)

    def getPolarityScore(self, text):
        return super().getPolarityScore(text)

    def listSupportedLabels(self):
        return super().listSupportedLabels()
        
    def listModels(self):
        return super().listModels()
