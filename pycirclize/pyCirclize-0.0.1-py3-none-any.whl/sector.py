from __future__ import annotations

import math
from typing import Callable

from matplotlib.patches import Patch
from matplotlib.projections.polar import PolarAxes

from pycirclize import config, utils
from pycirclize.patches import ArcRectangle
from pycirclize.track import Track


class Sector:
    """Circos Sector Class"""

    def __init__(
        self,
        name: str,
        size: float,
        rad_lim: tuple[float, float],
        start_pos: float = 0,
    ):
        self._name = name
        self._size = size
        self._rad_lim = rad_lim
        self._start_pos = start_pos
        self._tracks: list[Track] = []

        # Plot data and functions
        self._patches: list[Patch] = []
        self._plot_funcs: list[Callable[[PolarAxes], None]] = []

    ############################################################
    # Property
    ############################################################

    @property
    def name(self) -> str:
        """Name"""
        return self._name

    @property
    def size(self) -> float:
        """Size"""
        return self._size

    @property
    def start(self) -> float:
        """Start position"""
        return self._start_pos

    @property
    def end(self) -> float:
        """End position"""
        return self._start_pos + self._size

    @property
    def rad_size(self) -> float:
        """Radian size"""
        return self.rad_lim[1] - self.rad_lim[0]

    @property
    def rad_lim(self) -> tuple[float, float]:
        """Radian limit"""
        return self._rad_lim

    @property
    def deg_size(self) -> float:
        """Degree size"""
        return self.deg_lim[1] - self.deg_lim[0]

    @property
    def deg_lim(self) -> tuple[float, float]:
        """Degree limit"""
        return (math.degrees(self.rad_lim[0]), math.degrees(self.rad_lim[1]))

    @property
    def tracks(self) -> list[Track]:
        """Tracks"""
        return self._tracks

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

    def add_track(
        self,
        r_lim: tuple[float, float],
        r_pad_ratio: float = 0,
        name: str | None = None,
    ) -> Track:
        """Add track to specified radius limit region of sector

        Parameters
        ----------
        r_lim : tuple[float, float]
            Radius limit region (0 <= r <= 100)
        r_pad_ratio : float
            Radius padding ratio for plot (0 <= r_pad_ratio <= 1.0)
        name : str | None, optional
            Track name. If None, `Track{track_num}` is set.

        Returns
        -------
        track : Track
            Track
        """
        name = f"Track{len(self.tracks) + 1:02d}" if name is None else name
        if name in [t.name for t in self.tracks]:
            raise ValueError(f"TrackName='{name}' is already exists.")
        track = Track(name, r_lim, r_pad_ratio, self)
        self._tracks.append(track)
        return track

    def get_track(self, name: str) -> Track:
        """Get track by name

        Parameters
        ----------
        name : str
            Track name

        Returns
        -------
        track : Track
            Target name track
        """
        name2track = {t.name: t for t in self.tracks}
        if name not in name2track:
            raise ValueError(f"TrackName='{name}' not exists.")
        return name2track[name]

    def get_lowest_r(self) -> float:
        """Get lowest r position of sector from tracks data

        Returns
        -------
        lowest_r : float
            Lowest r position. If no tracks found, `lowest_r=100`.
        """
        if len(self.tracks) == 0:
            return config.MAX_R
        return min([min(t.r_lim) for t in self.tracks])

    def x_to_rad(self, x: float) -> float:
        """Convert x coordinate to radian in sector start-end range

        Parameters
        ----------
        x : float
            X coordinate

        Returns
        -------
        rad : float
            Radian coordinate
        """
        if not self.start <= x <= self.end:
            err_msg = f"x={x} is invalid range of '{self.name}' sector.\n{self}"
            raise ValueError(err_msg)
        size_ratio = self.rad_size / self.size
        x_from_start = x - self.start
        rad_from_start = x_from_start * size_ratio
        rad = min(self.rad_lim) + rad_from_start
        return rad

    def text(
        self,
        text: str,
        x: float | None = None,
        r: float = 110,
        orientation: str = "horizontal",
        **kwargs,
    ) -> None:
        """Plot text

        By default, plot text outside of sector

        Parameters
        ----------
        text : str
            Text content
        x: float, optional
            X position. If None, sector center x is set.
        r : float, optional
            Radius position. By default, outside position r=110 is set.
        orientation : str, optional
            Text orientation (`horizontal` or `vertical`)
        """
        if x is None:
            # Get sector center radian position
            center_x = (self.start + self.end) / 2
            rad = self.x_to_rad(center_x)
        else:
            rad = self.x_to_rad(x)

        # Set label proper alignment, rotation parameters by radian
        params = utils.get_label_params_by_rad(rad, orientation, outer=True)
        kwargs.update(params)

        def plot_text(ax: PolarAxes) -> None:
            ax.text(rad, r, text, **kwargs)

        self._plot_funcs.append(plot_text)

    def axis(self, **kwargs) -> None:
        """Plot sector axis (=sector border)

        Parameters
        ----------
        **kwargs
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
        """
        # Set default params
        kwargs = utils.set_axis_default_kwargs(**kwargs)

        # Spines facecolor placed behind other patches (zorder=0.99)
        fc_behind_kwargs = {**kwargs, **config.AXIS_FACE_PARAM}
        self.rect(self.start, self.end, config.R_LIM, **fc_behind_kwargs)

        # Spines edgecolor placed in front of other patches (zorder=1.01)
        ec_front_kwargs = {**kwargs, **config.AXIS_EDGE_PARAM}
        self.rect(self.start, self.end, config.R_LIM, **ec_front_kwargs)

    def rect(
        self,
        start: float,
        end: float,
        r_lim: tuple[float, float] | None = None,
        **kwargs,
    ) -> None:
        """Plot rectangle in sector

        Parameters
        ----------
        start : float
            Start position (x coordinate)
        end : float
            End position (x coordinate)
        r_lim : tuple[float, float] | None
            Radius limit region. If None, (0, 100) is set.
        **kwargs
            Patch properties (e.g. `fc="red", ec="blue", lw=1.0, ...`)
        """
        rad_rect_start = self.x_to_rad(start)
        rad_rect_end = self.x_to_rad(end)

        r_lim = (config.MIN_R, config.MAX_R) if r_lim is None else r_lim
        min_rad = min(rad_rect_start, rad_rect_end)
        max_rad = max(rad_rect_start, rad_rect_end)

        radr = (min_rad, min(r_lim))
        width = max_rad - min_rad
        height = max(r_lim) - min(r_lim)
        self._patches.append(ArcRectangle(radr, width, height, **kwargs))

    ############################################################
    # Private Method
    ############################################################

    def __str__(self):
        return (
            f"# Sector = '{self.name}'\n"
            f"# Size = {self.size} ({self.start} - {self.end})\n"
            f"# Radian size = {self.rad_size:.2f} "
            f"({self.rad_lim[0]:.2f} - {self.rad_lim[1]:.2f})\n"
            f"# Degree size = {self.deg_size:.2f} "
            f"({self.deg_lim[0]:.2f} - {self.deg_lim[1]:.2f})\n"
        )
