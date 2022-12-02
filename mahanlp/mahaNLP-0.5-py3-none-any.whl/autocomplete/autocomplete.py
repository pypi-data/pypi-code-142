from mahaNLP.modelRepo.mahaGPT import GPTModel

class TextGenerator(GPTModel):
    def __init__(self):
        self.modelName = 'marathi-gpt'
        super().__init__(self.modelName)

    def nextWord(self, text, numOfPredictions = 1):
        return super().nextWord(text, numOfPredictions)

    def completeSentence(self, text, numOfWords = 25, numOfPredictions = 1):
        return super().completeSentence(text, numOfWords, numOfPredictions )

    def listModels(self):
        return super().listModels()