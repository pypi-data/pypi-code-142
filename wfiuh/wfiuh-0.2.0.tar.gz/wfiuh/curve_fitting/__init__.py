import os
import re

import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats
import sklearn.metrics

from .models import Model


def curve_fitting_numpy(
    model: Model, x: np.ndarray, y: np.ndarray, func: str = "cdf"
) -> dict:
    if func == "cdf":
        f = model.cdf
    elif func == "pdf":
        f = model.pdf
    else:
        raise NotImplementedError()
    popt, pcov = scipy.optimize.curve_fit(
        f=f,
        xdata=x,
        ydata=y,
        p0=model.p0,
        sigma=model.sigma,
        bounds=model.bounds,
    )
    r2_score = sklearn.metrics.r2_score(y_true=y, y_pred=model.forward(x, *popt))
    return {**{chr(ord("a") + i): p for i, p in enumerate(popt)}, "r2_score": r2_score}


def curve_fitting_file(model: Model, filepath: str, func: str = "cdf") -> dict:
    res = re.fullmatch(pattern=r"(?P<id>\d+).*", string=os.path.basename(filepath))
    assert res
    id = int(res.group("id"))
    try:
        df = pd.read_csv(filepath)
        x = df["flowTime"].to_numpy()
        y = df["frequency"].to_numpy()
        if func == "cdf":
            y = y.cumsum()
        model.prepare(x=x, y=y)
        results = curve_fitting_numpy(model=model, x=x, y=y)
        return {"id": id, **results}
    except Exception as e:
        raise type(e)(id, str(e))
