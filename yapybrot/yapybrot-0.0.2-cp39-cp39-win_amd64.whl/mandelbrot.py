from _yapybrot import _mandelbrot
import matplotlib as mpl
import numpy as np


class Mandelbrot:
    def __init__(self, **kwargs):
        self.width = 500
        self.height = 500
        self.xmin = -2
        self.xmax = .5
        self.ymin = -1.12
        self.ymax = 1.12
        self.max_iter = 256
        self.pallette = np.empty([self.max_iter, 3])
        self.pallette_name = 'jet'

        self.set_pallette(self.pallette_name)
        self._set_args(**kwargs)

    def set_pallette(self, name):
        cmap = mpl.colormaps[name]
        self.pallette = (cmap(np.linspace(0, 1, self.max_iter))[:, :3] * 255)\
            .astype(int)

    def _set_args(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError

        if 'pallette_name' in kwargs.keys():
            self.set_pallette(self.pallette_name)

    def calculate(self, **kwargs):
        self._set_args(**kwargs)
        return _mandelbrot(
            self.width,
            self.height,
            self.xmin,
            self.xmax,
            self.ymin,
            self.ymax,
            self.max_iter,
            self.pallette
        )
