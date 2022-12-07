class GraphSeries:
    def __init__(self, graph_series) -> None:
        self.graph_series = graph_series

    def set_context(self, context: str):
        self.graph_series.set_context(context)
    
    @property
    def name(self) -> str:
        return self.graph_series.name
