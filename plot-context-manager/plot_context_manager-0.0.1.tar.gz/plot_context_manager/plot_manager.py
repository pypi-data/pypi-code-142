import matplotlib.pyplot as plt
from pretty_repr import RepresentableObject

from plot_context_manager.style_setter import StyleSetter


class PlotManager(RepresentableObject):

    def __init__(
            self,
            figure_size: tuple[float, float] = None,
            dpi: int = 300,
    ):
        self.fig, self.ax = None, None
        self.dpi = dpi
        self.figure_size = figure_size

    @property
    def excluded_attributes_for_repr(self) -> set[str]:
        return {'fig', 'ax'}

    def __enter__(self):
        """Method for entrance to context manager"""
        StyleSetter().update()
        self.fig, self.ax = plt.subplots(
            figsize=self.figure_size,
            dpi=self.dpi,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Method for exit from context manager"""
        if self.fig and self.ax:
            self.show()
            plt.close('all')

    @staticmethod
    def show() -> None:
        plt.show()
