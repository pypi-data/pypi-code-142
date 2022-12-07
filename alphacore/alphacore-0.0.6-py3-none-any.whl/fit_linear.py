import numpy as np
from scipy.optimize import curve_fit
from alphacore.utils import linear_models, objectConverters, removeNegativesInX, removeNaNs


class fit_linear_model:
    def __init__(self, model, xdata, ydata, method=None, guess=None):
        xmin = None
        if model.upper() == "LINEAR":
            param_names = ["a", "b"]
            func = linear_models.linear
        elif model.upper() == "2ND ORDER POLYNOMIAL":
            param_names = ["a", "b", "c"]
            func = linear_models.poly_2
        elif model.upper() == "3RD ORDER POLYNOMIAL":
            param_names = ["a", "b", "c", "d"]
            func = linear_models.poly_3
        elif model.upper() == "4TH ORDER POLYNOMIAL":
            param_names = ["a", "b", "c", "d", "e"]
            func = linear_models.poly_4
        elif model.upper() == "5TH ORDER POLYNOMIAL":
            param_names = ["a", "b", "c", "d", "e", "f"]
            func = linear_models.poly_5
        elif model.upper() == "6TH ORDER POLYNOMIAL":
            param_names = ["a", "b", "c", "d", "e", "f", "g"]
            func = linear_models.poly_6
        elif model.upper() == "LOGARITHMIC":
            param_names = ["a", "b", "c"]
            func = linear_models.logarithmic
            xdata, ydata = removeNegativesInX(xdata, ydata)
            xmin = 0
        elif model.upper() == "EXPONENTIAL":
            param_names = ["a", "b", "c"]
            func = linear_models.exponential
            if guess == None:
                guess = [1, -0.001, 0]
            xdata, ydata = removeNegativesInX(xdata, ydata)
            xmin = 0
        elif model.upper() == "POWER":
            param_names = ["a", "b"]
            func = linear_models.power
            xdata, ydata = removeNegativesInX(xdata, ydata)
            xmin = 0
        else:
            raise ValueError("model not recognised")

        fit = curve_fit(f=func, xdata=xdata, ydata=ydata, method=method, p0=guess)
        params = fit[0].tolist()

        objectConverters.list2object(
            object_to_use=self, keys=param_names, values=params
        )

        # generate suggested plotting limits
        xrange = max(xdata) - min(xdata)
        yrange = max(ydata) - min(ydata)
        if xmin is None:
            xmin = min(xdata) - xrange * 0.2
            if xrange > 5:
                xmin = np.floor(xmin)
        self.xmin = float(xmin)

        xmax = max(xdata) + xrange * 0.2
        if xrange > 5:
            xmax = np.ceil(xmax)
        self.xmax = float(xmax)

        ymin = min(ydata) - yrange * 0.2
        if yrange > 5:
            ymin = np.floor(ymin)
        self.ymin = float(ymin)

        ymax = max(ydata) + yrange * 0.2
        if yrange > 5:
            ymax = np.ceil(ymax)
        self.ymax = float(ymax)

        # generate fitted line from model parameters
        if model.upper() in ["POWER", "EXPONENTIAL", "LOGARITHMIC"]:
            xline = np.linspace(0, max(xdata) + xrange, 200)
        else:
            xline = np.linspace(min(xdata) - xrange, max(xdata) + xrange, 200)
        yline = func(*[xline, *params])

        xline, yline = removeNaNs(xline, yline)
        self.xline = xline.tolist()
        self.yline = yline.tolist()
