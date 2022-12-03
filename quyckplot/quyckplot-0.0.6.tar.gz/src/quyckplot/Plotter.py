from matplotlib import pyplot as plt
import matplotlib as mpl
from .utils import dict2formatted_string

# this function takes a plt method (e.g. plt.plot) and returns a function that takes a dataframe and plots it with the given method
def plotter_factory(method):
    def plotter(cls, data, x, y, legend=None, new=True, size=(9, 7), **kwargs):
        """
        Plots the data of the DataSet object.
        """
        if new:
            cls.new_plot(x, y, data.title, size)
        # if there is a single dataframe in data, plot it
        if len(data.dataframes) == 1:
            df = data.dataframes[0]["data"]
            if legend:
                method(
                    df[x], 
                    df[y], 
                    label=dict2formatted_string(data.dataframes[0]["params"], legend),
                    **kwargs
                )
            else:
                method(df[x], df[y], **kwargs)
        # if there are multiple dataframes in data, plot each of them
        else:
            for df in data.dataframes:
                if legend:
                    method(
                        df["data"][x], 
                        df["data"][y], 
                        label=dict2formatted_string(df["params"], legend), 
                        **kwargs
                    )
                else:
                    method(df["data"][x], df["data"][y], **kwargs)
        if legend:
            plt.legend(loc="best")
    return plotter

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