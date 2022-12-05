import logging
from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
from plot_context_manager.plot_manager import PlotManager


logging.basicConfig(format='%(asctime)s: %(message)s', level='INFO')


class Plot(PlotManager):

    def plot(self, *args, **kwargs):
        self.ax.plot(*args, **kwargs)

    def scatter(self, *args, **kwargs):
        self.ax.scatter(*args, **kwargs)

    def get_legend(self):
        self.ax.legend()

    def set_limits(
            self,
            left: float = None,
            right: float = None,
            bottom: float = None,
            top: float = None,
    ):
        self.ax.set_xlim(left=left, right=right)
        self.ax.set_ylim(bottom=bottom, top=top)

    def set_title(self, title: str):
        self.ax.set_title(title)

    def set_labels(
            self,
            x_label: str = None,
            y_label: str = None,
    ):
        if x_label:
            self.ax.set_xlabel(x_label)
        if y_label:
            self.ax.set_ylabel(y_label)

    def set_major_locators(
            self,
            x_step: float = None,
            y_step: float = None,
    ):
        if x_step:
            self.ax.xaxis.set_major_locator(plt.MultipleLocator(x_step))
        if y_step:
            self.ax.yaxis.set_major_locator(plt.MultipleLocator(y_step))

    def set_minor_locators(
            self,
            x_step: float = None,
            y_step: float = None,
    ):
        if x_step:
            self.ax.xaxis.set_minor_locator(plt.MultipleLocator(x_step))
        if y_step:
            self.ax.yaxis.set_minor_locator(plt.MultipleLocator(y_step))

    @staticmethod
    def save(path: Union[str, Path]):
        _path = path if isinstance(path, Path) else Path(path).resolve()
        prefix = _path.parent / _path.stem
        for fmt in ('png', 'eps', 'svg'):
            filename = str(prefix.with_suffix(f'.{fmt}'))
            plt.savefig(
                filename,
                format=fmt,
                bbox_inches='tight',
                pad_inches=0,
                transparent=True,
            )
            logging.info(f'Figure {filename} is saved.')


if __name__ == '__main__':
    with Plot() as plot:
        plot.plot([0, 5], [0, 5], label='line')
        plot.scatter([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25], label='square')
        plot.get_legend()
        plot.set_title('test')
        plot.set_labels('x', 'y')
        plot.set_limits(left=-1, right=6, top=7)
        plot.set_major_locators(x_step=1, y_step=1)
        plot.set_minor_locators(x_step=0.2, y_step=0.2)
        plot.save('test.png')
