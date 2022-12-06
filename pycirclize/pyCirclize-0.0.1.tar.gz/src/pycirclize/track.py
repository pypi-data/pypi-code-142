from __future__ import annotations

import math
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Callable

import numpy as np
from Bio.SeqFeature import SeqFeature
from matplotlib.colors import Normalize
from matplotlib.patches import Patch
from matplotlib.projections.polar import PolarAxes

from pycirclize import config, utils
from pycirclize.patches import ArcArrow, ArcLine, ArcRectangle

if TYPE_CHECKING:
    # Avoid Sector <-> Track circular import error at runtime
    from pycirclize.sector import Sector


class Track:
    """Circos Track Class"""

    def __init__(
        self,
        name: str,
        r_lim: tuple[float, float],
        r_pad_ratio: float,
        parent_sector: Sector,
    ):
        """
        Parameters
        ----------
        name : str
            Track name
        r_lim : tuple[float, float]
            Track radius limit region
        r_pad_ratio : float
            Track padding ratio for plot data
        parent_sector : Sector
            Parent sector of track
        """
        # Track params
        self._name = name
        self._r_lim = r_lim
        self._r_pad_ratio = r_pad_ratio
        # Inherited from parent sector
        self._parent_sector = parent_sector
        self._rad_lim = parent_sector.rad_lim
        self._start = parent_sector.start
        self._end = parent_sector.end

        # Plot data and functions
        self._patches: list[Patch] = []
        self._plot_funcs: list[Callable[[PolarAxes], None]] = []

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Track name"""
        return self._name

    @property
    def size(self) -> float:
        """Track size (x coordinate)"""
        return self.end - self.start

    @property
    def start(self) -> float:
        """Track start position (x coordinate)"""
        return self._start

    @property
    def end(self) -> float:
        """Track end position (x coordinate)"""
        return self._end

    @property
    def r_size(self) -> float:
        """Track radius size"""
        return max(self.r_lim) - min(self.r_lim)

    @property
    def r_lim(self) -> tuple[float, float]:
        """Track radius limit"""
        return self._r_lim

    @property
    def r_plot_size(self) -> float:
        """Track radius size for plot data (`r_size` with padding)"""
        return max(self.r_plot_lim) - min(self.r_plot_lim)

    @property
    def r_plot_lim(self) -> tuple[float, float]:
        """Track radius limit for plot data (`r_lim` with padding)"""
        edge_pad_size = (self.r_size * self._r_pad_ratio) / 2
        min_plot_r = min(self.r_lim) + edge_pad_size
        max_plot_r = max(self.r_lim) - edge_pad_size
        return (min_plot_r, max_plot_r)

    @property
    def rad_size(self) -> float:
        """Radian size"""
        return max(self.rad_lim) - min(self.rad_lim)

    @property
    def rad_lim(self) -> tuple[float, float]:
        """Radian limit"""
        return self._rad_lim

    @property
    def deg_size(self) -> float:
        """Degree size"""
        return max(self.deg_lim) - min(self.deg_lim)

    @property
    def deg_lim(self) -> tuple[float, float]:
        """Degree limit"""
        return (math.degrees(min(self.rad_lim)), math.degrees(max(self.rad_lim)))

    @property
    def parent_sector(self) -> Sector:
        """Parent sector"""
        return self._parent_sector

    @property
    def patches(self) -> list[Patch]:
        """Plot patches"""
        return self._patches

    @property
    def plot_funcs(self) -> list[Callable[[PolarAxes], None]]:
        """Plot functions"""
        return self._plot_funcs

    ############################################################
    # Public Method
    ############################################################

    def x_to_rad(self, x: float) -> float:
        """Convert x coordinate to radian in track start-end range

        Parameters
        ----------
        x : float
            X coordinate

        Returns
        -------
        rad : float
            Radian coordinate
        """
        return self.parent_sector.x_to_rad(x)

    def text(
        self,
        text: str,
        x: float | None = None,
        r: float | None = None,
        adjust_rotation: bool = True,
        orientation: str = "horizontal",
        **kwargs,
    ) -> None:
        """Plot text

        Parameters
        ----------
        text : str
            Text content
        x : float | None
            X position. If None, track center x position is set.
        r : float | None
            Radius position. If None, track center radius position is set.
        adjust_rotation : bool, optional
            If True, text rotation is auto set based on `x` and `orientation` params.
        orientation : str, optional
            Text orientation (`horizontal` or `vertical`)
            If adjust_rotation=True, orientation is used for rotation calculation.
        **kwargs
            Text properties (e.g. `size=12, color="red", va="center", ...`)
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
        """
        # If value is None, center position is set.
        x = (self.start + self.end) / 2 if x is None else x
        r = sum(self.r_lim) / 2 if r is None else r

        if adjust_rotation:
            rad = self.x_to_rad(x)
            params = utils.get_label_params_by_rad(rad, orientation, only_rotation=True)
            kwargs.update(params)

        if "ha" not in kwargs and "horizontalalignment" not in kwargs:
            kwargs.update(dict(ha="center"))
        if "va" not in kwargs and "verticalalignment" not in kwargs:
            kwargs.update(dict(va="center"))

        def plot_func(ax: PolarAxes) -> None:
            ax.text(self.x_to_rad(x), r, text, **kwargs)

        self._plot_funcs.append(plot_func)

    def line(
        self,
        x: list[float] | np.ndarray,
        y: list[float] | np.ndarray,
        vmin: float = 0,
        vmax: float | None = None,
        **kwargs,
    ) -> None:
        """Plot line

        Parameters
        ----------
        x : list[float] | np.ndarray
            X coordinates
        y : list[float] | np.ndarray
            Y coordinates
        vmin : float, optional
            Y min value. If `min(y)` is less than `vmin`, `min(y)` is set.
        vmax : float | None, optional
            Y max value. If None, `max(y)` is set.
            If `max(y)` is more than `vmax`, `max(y)` is set.
        """
        # Convert (x, y) to (rad, r)
        rad = list(map(self.x_to_rad, x))
        vmin = min(list(y) + [vmin])
        vmax = max(y) if vmax is None else max(list(y) + [vmax])
        r = [self._y_to_r(v, vmin, vmax) for v in y]
        # Convert normal line to arc line (rad, r) points
        arc_rad, arc_r = self._to_arc_radr(rad, r)

        def plot_line(ax: PolarAxes) -> None:
            ax.plot(arc_rad, arc_r, **kwargs)

        self._plot_funcs.append(plot_line)

    def bar(
        self,
        x: list[float] | np.ndarray,
        height: list[float] | np.ndarray,
        width: float,
        bottom: float = 0,
        align: str = "center",
        **kwargs,
    ) -> None:
        """Plot bar

        For plot speed reasons, don't use matplotlib's `Axes.bar` method internally.
        Self-implemented bar method with equivalent functionality of `Axes.bar` is used.

        Parameters
        ----------
        x : list[float] | np.ndarray
            Bar X coordinates
        height : list[float] | np.ndarray
            Bar heights
        width : float
            Bar width ratio (0 - 1.0)
        bottom : float, optional
            Height bottom value
        align : str, optional
            Bar alignment type (`center` or `edge`)
        """
        if len(x) != len(height):
            err_msg = "'x', 'height' list length is not match "
            err_msg += f"(List length: x={len(x)}, height={len(height)})."
            raise ValueError(err_msg)

        # Convert (x, y) to (rad, r)
        x = list(map(self.x_to_rad, x))
        height = [self._y_to_r(v, bottom, max(height)) for v in height]
        height = np.array(height) - self.r_plot_lim[0]
        width = self.rad_size * (width / self.size)

        # Don't use matplotlib's `Axes.bar` method
        #
        # def plot_bar(ax: PolarAxes) -> None:
        #     ax.bar(x, height, width, self.r_plot_lim[0], **kwargs)
        # self._plot_funcs.append(plot_bar)

        for rad, h in zip(x, height):
            if align == "center":
                radr = (rad - (width / 2), min(self.r_plot_lim))
            elif align == "edge":
                radr = (rad, min(self.r_plot_lim))
            else:
                raise ValueError(f"align='{align}' is invalid ('center' or 'edge').")
            bar_arc_rect = ArcRectangle(radr, width, h, **kwargs)
            self._patches.append(bar_arc_rect)

    def scatter(
        self,
        x: list[float] | np.ndarray,
        y: list[float] | np.ndarray,
        vmin: float = 0,
        vmax: float | None = None,
        **kwargs,
    ) -> None:
        """Plot scatter

        In this method, `x` & `y` are converted to polar coordinates and
        passed to matplotlib's `Axes.scatter` method.

        Parameters
        ----------
        x : list[float] | np.ndarray
            X position list
        y : list[float] | np.ndarray
            Y position list
        vmin : float, optional
            Y min value. If `min(y)` is less than `vmin`, `min(y)` is set.
        vmax : float | None, optional
            Y max value. If None, `max(y)` is set.
            If `max(y)` is more than `vmax`, `max(y)` is set.
        **kwargs
            Scatter property (e.g. `ec="black", lw=1.0, ...`)
            https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
        """
        # Convert (x, y) to (rad, r)
        rad = list(map(self.x_to_rad, x))
        vmin = min(list(y) + [vmin])
        vmax = max(y) if vmax is None else max(list(y) + [vmax])
        r = [self._y_to_r(v, vmin, vmax) for v in y]

        def plot_scatter(ax: PolarAxes) -> None:
            ax.scatter(rad, r, **kwargs)

        self._plot_funcs.append(plot_scatter)

    def fill_between(
        self,
        x: list[float] | np.ndarray,
        y1: list[float] | np.ndarray,
        y2: float | list[float] | np.ndarray = 0,
        vmin: float | None = 0,
        vmax: float | None = None,
        **kwargs,
    ) -> None:
        """Fill the area between two horizontal(y1, y2) curves

        In this method, `x` & `y1` & `y2` are converted to polar coordinates and
        passed to matplotlib's `Axes.fill_between` method.

        Parameters
        ----------
        x : list[float] | np.ndarray
            X coordinates
        y1 : list[float] | np.ndarray
            Y coordinates (first curve definition)
        y2 : float | list[float] | np.ndarray, optional
            Y coordinate[s] (second curve difinition)
        vmin : float | None, optional
            Y min value.
        vmax : float | None, optional
            Y max value.
        **kwargs
            Axes.fill_between properties (e.g. `fc="red", ec="black", lw=0.1, ...`)
        """
        rad = list(map(self.x_to_rad, x))
        # TODO: Refactor code (_to_arc_radr, _to_arc_rad) move to utils?
        if isinstance(y2, Iterable):
            y_all = list(y1) + list(y2)
            vmin = min(y_all) if vmin is None else min(y_all + [vmin])
            vmax = max(y_all) if vmax is None else max(y_all + [vmax])
            r2 = [self._y_to_r(v, vmin, vmax) for v in y2]
            arc_rad, arc_r2 = self._to_arc_radr(rad, r2)
            r = [self._y_to_r(v, vmin, vmax) for v in y1]
            _, arc_r = self._to_arc_radr(rad, r)
        else:
            y_all = list(y1) + [y2]
            vmin = min(y_all) if vmin is None else min(y_all + [vmin])
            vmax = max(y_all) if vmax is None else max(y_all + [vmax])
            r2 = self._y_to_r(y2, vmin, vmax)
            arc_rad = self._to_arc_rad(rad)
            arc_r2 = [r2] * len(arc_rad)
            r = [self._y_to_r(v, vmin, vmax) for v in y1]
            _, arc_r = self._to_arc_radr(rad, r)

        def plot_fill(ax: PolarAxes) -> None:
            ax.fill_between(arc_rad, arc_r, arc_r2, **kwargs)  # type: ignore

        self._plot_funcs.append(plot_fill)

    def heatmap(self) -> None:
        """Plot heatmap"""
        pass

    def hist(self) -> None:
        """Plot histogram"""
        pass

    def xticks(
        self,
        x: list[float],
        labels: list[str] | None = None,
        tick_length: float = 2,
        outer: bool = True,
        show_bottom_line: bool = False,
        label_size: float = 8,
        label_margin: float = 0.5,
        label_orientation: str = "horizontal",
        line_kws: dict[str, Any] = {},
        text_kws: dict[str, Any] = {},
    ) -> None:
        """Plot xticks & labels on user-specified position

        If you want to plot xticks and their position labels at regular intervals,
        it is recommended to use high-level API function `track.xticks_by_interval()`.

        Parameters
        ----------
        x : list[float]
            X coordinates
        labels : list[str] | None, optional
            Labels on xticks. If None, only plot ticks line.
        tick_length : float, optional
            Tick length
        outer : bool, optional
            If True, show ticks on outer. Else, show ticks on inner.
        show_bottom_line : bool, optional
            If True, show bottom line.
        label_size : float, optional
            Label size
        label_margin : float, optional
            Label margin size
        label_orientation : str, optional
            Label orientation (`horizontal` or `vertical`)
        line_kws : dict[str, Any], optional
            Patch properties (e.g. `dict(ec="red", lw=1, ...)`)
        text_kws : dict[str, Any], optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
        """
        # Check list length of x & labels
        if labels is not None and len(x) != len(labels):
            err_msg = "'x', 'labels' list length is not match "
            err_msg += f"(List length: x={len(x)}, labels={len(labels)})"
            raise ValueError(err_msg)

        # Plot xticks & labels
        r = max(self.r_lim) if outer else min(self.r_lim)
        tick_r_lim = (r, r + tick_length) if outer else (r - tick_length, r)
        labels = [""] * len(x) if labels is None else labels
        for x_pos, label in zip(x, labels):
            # Plot xticks
            if tick_length > 0:
                self._simpleline((x_pos, x_pos), tick_r_lim, **line_kws)
            # Plot labels
            if label != "":
                rad = self.x_to_rad(x_pos)
                if outer:
                    adj_r = max(tick_r_lim) + label_margin
                else:
                    adj_r = min(tick_r_lim) - label_margin
                params = utils.get_label_params_by_rad(rad, label_orientation, outer)
                text_kws.update({**params, **dict(size=label_size)})
                self.text(label, x_pos, adj_r, adjust_rotation=False, **text_kws)

        # Plot bottom line
        if show_bottom_line:
            self._simpleline((self.start, self.end), (r, r), **line_kws)

    def xticks_by_interval(
        self,
        interval: float,
        tick_length: float = 2,
        outer: bool = True,
        show_bottom_line: bool = False,
        show_label: bool = True,
        label_size: float = 8,
        label_margin: float = 0.5,
        label_orientation: str = "horizontal",
        label_formatter: Callable[[float], str] | None = None,
        line_kws: dict[str, Any] = {},
        text_kws: dict[str, Any] = {},
    ) -> None:
        """Plot xticks & position labels by user-specified interval

        `track.xticks_by_interval()` is high-level API function of `track.xticks()`.
        If you want to plot xticks and their labels in any position you like,
        use low-level API function `track.xticks()` instead.

        Parameters
        ----------
        interval : float
            Xticks interval
        tick_length : float, optional
            Tick length
        outer : bool, optional
            If True, show ticks on outer. Else, show ticks on inner.
        show_bottom_line : bool, optional
            If True, show bottom line.
        show_label : bool, optional
            If True, show label of xticks interval position.
        label_size : float, optional
            Label size
        label_margin : float, optional
            Label margin size
        label_orientation : str, optional
            Label orientation (`horizontal` or `vertical`)
        label_formatter : Callable[[float], str] | None, optional
            User-defined function for label format. (e.g. `1000 -> '1.0 Kb'`)
        line_kws : dict[str, Any], optional
            Patch properties (e.g. `dict(ec="red", lw=1, ...)`)
        text_kws : dict[str, Any], optional
            Text properties (e.g. `dict(color="red", alpha=0.5, ...)`)
        """
        # Setup xtick positions
        x_list = []
        start_pos, end_pos = self.start - (self.start % interval), self.end + interval
        for x in np.arange(start_pos, end_pos, interval):
            if self.start <= x <= self.end:
                x_list.append(x)

        # Setup xticks labels
        labels = None
        if show_label:
            if label_formatter is None:
                labels = [str(x) for x in x_list]
            else:
                labels = [label_formatter(x) for x in x_list]

        # Plot xticks by user-specified interval
        self.xticks(
            x=x_list,
            labels=labels,
            tick_length=tick_length,
            outer=outer,
            show_bottom_line=show_bottom_line,
            label_size=label_size,
            label_margin=label_margin,
            label_orientation=label_orientation,
            line_kws=line_kws,
            text_kws=text_kws,
        )

    def axis(self, **kwargs) -> None:
        """Plot track axis (track border)

        By default, simple black axis params(`fc="none", ec="black", lw=0.5`) are set.

        Parameters
        ----------
        **kwargs
            Patch properties (e.g. `fc="tomato", ec="blue", hatch="//"`)
        """
        # Set default params
        kwargs = utils.set_axis_default_kwargs(**kwargs)

        # Spines facecolor placed behind other patches (zorder=0.99)
        fc_behind_kwargs = {**kwargs, **config.AXIS_FACE_PARAM}
        self.rect(self.start, self.end, ignore_pad=True, **fc_behind_kwargs)

        # Spines edgecolor placed in front of other patches (zorder=1.01)
        ec_front_kwargs = {**kwargs, **config.AXIS_EDGE_PARAM}
        self.rect(self.start, self.end, ignore_pad=True, **ec_front_kwargs)

    def arrow(
        self,
        start: float,
        end: float,
        # TODO: Add r_lim param
        head_length: float = 2,
        shaft_ratio: float = 0.5,
        **kwargs,
    ) -> None:
        """Plot arrow

        Parameters
        ----------
        start : float
            Start position (x coordinate)
        end : float
            End position (x coordinate)
        head_length : float, optional
            Arrow head lenth (Degree unit)
        shaft_ratio : float, optional
            Arrow shaft ratio (0 - 1.0)
        **kwargs
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
        """
        rad_arrow_start = self.x_to_rad(start)
        rad_arrow_end = self.x_to_rad(end)
        arc_arrow = ArcArrow(
            rad=rad_arrow_start,
            r=self.r_plot_lim[0],
            drad=rad_arrow_end - rad_arrow_start,
            dr=self.r_plot_size,
            head_length=math.radians(head_length),
            shaft_ratio=shaft_ratio,
            **kwargs,
        )
        self._patches.append(arc_arrow)

    def rect(
        self,
        start: float,
        end: float,
        r_lim: tuple[float, float] | None = None,
        ignore_pad: bool = False,
        **kwargs,
    ) -> None:
        """Plot rectangle on track

        Parameters
        ----------
        start : float
            Start position (x coordinate)
        end : float
            End position (x coordinate)
        r_lim : tuple[float, float]
            Radius limit range. If None, track's r_lim is set.
        ignore_pad : bool, optional
            If True, ignore track padding setting.
            If r_lim param is set by user, this option not works.
        **kwargs
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
        """
        rad_rect_start = self.x_to_rad(start)
        rad_rect_end = self.x_to_rad(end)
        rad = rad_rect_start if start < end else rad_rect_end
        width = abs(rad_rect_end - rad_rect_start)
        if r_lim is not None:
            if not min(self.r_lim) <= min(r_lim) < max(r_lim) <= max(self.r_lim):
                raise ValueError(f"r_lim={r_lim} is invalid track range.\n{self}")
            radr, height = (rad, min(r_lim)), max(r_lim) - min(r_lim)
        elif ignore_pad:
            radr, height = (rad, min(self.r_lim)), self.r_size
        else:
            radr, height = (rad, min(self.r_plot_lim)), self.r_plot_size
        arc_rect = ArcRectangle(radr, width, height, **kwargs)
        self._patches.append(arc_rect)

    def genomic_features(
        self,
        features: list[SeqFeature],
        plotstyle: str = "box",
        facecolor_handle_func: Callable[[SeqFeature], str] | None = None,
        **kwargs,
    ) -> None:
        """Plot genomic features

        Parameters
        ----------
        features : list[SeqFeature]
            Biopython's SeqFeature list
        plotstyle : str, optional
            Plot style (`box` or `arrow`)
        facecolor_handle_func : Callable[[SeqFeature], str] | None, optional
            User-defined function to handle facecolor
        """
        for feature in features:
            # Set qualifier tag facecolor if exists
            tag_color = feature.qualifiers.get("facecolor", [None])[0]
            if tag_color is not None:
                kwargs.update(dict(fc=tag_color, facecolor=tag_color))
            # Set facecolor by user-defined function
            if facecolor_handle_func is not None:
                color = facecolor_handle_func(feature)
                kwargs.update(dict(fc=color, facecolor=color))
            # Plot feature
            try:
                start = int(str(feature.location.parts[0].start))
                end = int(str(feature.location.parts[-1].end))
            except ValueError:
                print(f"Failed to parse feature's start-end position.\n{feature}")
                continue
            if feature.strand == -1:
                start, end = end, start
            if plotstyle == "box":
                self.rect(start, end, **kwargs)
            elif plotstyle == "arrow":
                self.arrow(start, end, **kwargs)
            else:
                raise ValueError(f"Invalid plotstyle='f{plotstyle}'.")

    ############################################################
    # Private Method
    ############################################################

    def _y_to_r(self, y: float, vmin: float, vmax: float) -> float:
        """Convert y coordinate to radius in track radius limit"""
        norm = Normalize(vmin, vmax)
        r = self.r_plot_lim[0] + (self.r_plot_size * norm(y))
        return r

    def _to_arc_radr(
        self, rad: list[float] | np.ndarray, r: list[float] | np.ndarray
    ) -> tuple[list[float], list[float]]:
        all_arc_rad, all_arc_r = [], []
        for i in range(len(rad) - 1):
            rad1, rad2, r1, r2 = rad[i], rad[i + 1], r[i], r[i + 1]
            step = config.ARC_RADIAN_STEP
            arc_rad = list(np.arange(rad1, rad2, step)) + [rad2]
            all_arc_rad.extend(arc_rad)
            arc_r = np.linspace(r1, r2, len(arc_rad), endpoint=True)
            all_arc_r.extend(arc_r)
        return all_arc_rad, all_arc_r

    def _to_arc_rad(self, rad: list[float] | np.ndarray) -> list[float]:
        all_arc_rad = []
        for i in range(len(rad) - 1):
            rad1, rad2 = rad[i], rad[i + 1]
            step = config.ARC_RADIAN_STEP
            arc_rad = list(np.arange(rad1, rad2, step)) + [rad2]
            all_arc_rad.extend(arc_rad)
        return all_arc_rad

    def _simpleline(
        self,
        x_lim: tuple[float, float],
        r_lim: tuple[float, float],
        **kwargs,
    ) -> None:
        """Plot simple patch line between two points (x1, r1), (x2, r2)

        Used to plot simple lines such as ticks internally

        Parameters
        ----------
        x_lim : tuple[float, float]
            X start-end limit region
        r_lim : tuple[float, float]
            Radius start-end limit region
        **kwargs
            Patch properties (e.g. `ec="red", lw=1.0, ...`)
        """
        rad_lim = (self.x_to_rad(x_lim[0]), self.x_to_rad(x_lim[1]))
        self._patches.append(ArcLine(rad_lim, r_lim, **kwargs))

    def __str__(self):
        return (
            f"# Track = '{self.name}' (Parent Sector = '{self.parent_sector.name}')\n"
            f"# Size = {self.size} ({self.start} - {self.end})\n"
            f"# Radius size = {self.r_size:.2f} "
            f"({min(self.r_lim):.2f} - {max(self.r_lim):.2f})\n"
            f"# Degree size = {self.deg_size:.2f} "
            f"({min(self.deg_lim):.2f} - {max(self.deg_lim):.2f})\n"
        )
