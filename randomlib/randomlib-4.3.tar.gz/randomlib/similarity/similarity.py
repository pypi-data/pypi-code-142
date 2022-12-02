from randomlib.modelRepo.mahaSimilarity import SimilarityModel

class SimilarityAnalyzer(SimilarityModel):
    def __init__(self):
        self.modelName =  'marathi-sentence-similarity-sbert'
        super().__init__(self.modelName)

    def embedSentences(self, sentences):
        return super().embedSentences(sentences)
    
    def getSimilarityScore(self, sourceSentence, sentences, as_dict: bool = False):
        return super().getSimilarityScore(sourceSentence, sentences, as_dict)

    def listModels(self):
        return super().listModels()