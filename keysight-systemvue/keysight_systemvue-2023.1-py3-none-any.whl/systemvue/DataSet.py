from .Variable import Variable

class DataSet:
    def __init__(self, dataset) -> None:
        self.dataset = dataset

    def create_variable(self, name: str) -> Variable:
        return Variable(self.dataset.create_variable(name))

    def delete_variable(self, name: str):
        self.dataset.delete_variable(name)

    def import_data(self, fileSpecification: str, format: str, options):
        self.dataset.import_data(fileSpecification, format, options)

    def export_data(self, fileSpecification: str, format: str, options):
        self.dataset.export_data(fileSpecification, format, options)
    
    @property
    def name(self) -> str:
        return self.dataset.name
    
    @property
    def variables(self) -> dict[str, Variable]:
        return {k:Variable(x) for (k,x) in self.dataset.variables.items()}
