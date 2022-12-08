"""
This file contains the Plotter class.
The purpose of this class is to provide a simple interface for plotting data from a DataSet instance.
"""

from matplotlib import pyplot as plt
import matplotlib as mpl
from .utils import plotter_factory

class Plotter:
    nth_plot = 0
    plot = classmethod(plotter_factory(plt.plot))
    scatter = classmethod(plotter_factory(plt.scatter))

    @staticmethod
    def set_theme():
        mpl.rcParams["mathtext.fontset"] = "cm"
        plt.rcParams["font.family"] = "serif"
        plt.rcParams["figure.autolayout"] = True
        mpl.rcParams.update({'font.size': 22})
    
    @classmethod
    def start_session(cls):
        cls.set_theme()
        cls.nth_plot = 0

    @staticmethod
    def end_session():
        plt.show()

    @classmethod
    def new_plot(cls, xlabel, ylabel, title, size):
        cls.nth_plot += 1
        fig = plt.figure(cls.nth_plot, figsize=size)
        fig.suptitle(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)