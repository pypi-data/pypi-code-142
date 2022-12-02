from randomlib.modelRepo.mahaFill import MaskFillModel

class MaskPredictor(MaskFillModel):
    def __init__(self):
        self.modelName = 'marathi-bert-v2'
        super().__init__(self.modelName)

    def predictMask(self, text, details: str = "minimum", as_dict: bool = False):
        return super().predictMask(text, details, as_dict)

    def listModels(self):
        return super().listModels()