from cycler import cycler
import matplotlib.pyplot as plt


COLORS = (
    'black',
    'red',
    'green',
    'blue',
    'cyan',
    'magenta',
    'purple',
    'orange',
    'olive',
    'yellow',
    'brown',
    'pink',
    'gray',
    'lime',
    'slateblue',
    'crimson',
    'darkviolet',
    'sienna',
    'coral',
    'navy',
    'crimson',
    'goldenrod',
    'darkcyan',
    'dodgerblue',
    'saddlebrown',
)


class StyleSetter:
    """Description of Plot object"""

    def update(self):
        """Setting of rcParams"""
        self._update_figure()
        self._update_axes()
        self._update_lines()
        self._update_legend()
        self._update_font(family='Arial', size=14)
        self._update_ticks()

    @staticmethod
    def _update_figure() -> None:
        plt.rcParams.update({
            'figure.dpi': 300,
            'figure.figsize': [i / 2.54 for i in (10, 10)],
        })

    @staticmethod
    def _update_axes() -> None:
        plt.rcParams.update({
            'axes.labelpad': 0,
            'axes.prop_cycle': cycler(color=COLORS),
            'axes.linewidth': 2,
            'lines.linewidth': 2,
            'lines.markersize': 7,
            "legend.frameon": False,
        })

    @staticmethod
    def _update_lines() -> None:
        plt.rcParams.update({
            'lines.linewidth': 2,
            'lines.markersize': 7,
            "legend.frameon": False,
        })

    @staticmethod
    def _update_legend() -> None:
        plt.rcParams.update({
            "legend.frameon": False,
        })

    @staticmethod
    def _update_font(family: str, size: int) -> None:
        plt.rcParams.update({
            # 'mathtext.fontset': 'stix',
            'font.family': family,
            'mathtext.it': family,
            'xtick.labelsize': size,
            'ytick.labelsize': size,
            'legend.fontsize': size,
            'axes.titlesize': size,
            'axes.labelsize': size,
            'font.size': size,
        })

    @staticmethod
    def _update_ticks() -> None:
        plt.rcParams.update({
            "xtick.minor.bottom": True,
            "xtick.minor.top": True,
            "xtick.top": True,
            "ytick.minor.left": True,
            "ytick.minor.right": True,
            "ytick.right": True,
        })
        tick_parameters = {
            'direction': 'in',
            'major.pad': 3,
            'major.size': 6,
            'major.width': 2,
            'minor.size': 3,
            'minor.width': 2,
        }
        for tick in ('xtick', 'ytick'):
            for _key, _value in tick_parameters.items():
                plt.rcParams[f'{tick}.{_key}'] = _value
