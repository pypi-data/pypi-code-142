import os
import re

import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats
import sklearn.metrics

from ..typed import Model
from .beta import Beta
from .double_triangular import DoubleTriangular
from .hoerl import Hoerl
from .inverse_gaussian import InverseGaussian
from .normal_gaussian import NormalGaussian
from .polynomial import Polynomial


def curve_fitting_numpy(model: Model, x: np.ndarray, y: np.ndarray) -> dict:
    popt, pcov = scipy.optimize.curve_fit(
        f=model.forward, xdata=x, ydata=y, p0=model.p0, bounds=model.bounds
    )
    r2_score = sklearn.metrics.r2_score(y_true=y, y_pred=model.forward(x, *popt))
    return {"popt": popt, "r2_score": r2_score}


def curve_fitting_file(model: Model, filepath: str) -> dict:
    try:
        df = pd.read_csv(filepath)
        x = df["flowTime"].to_numpy()
        y = df["frequency"].to_numpy()
        model.prepare(x=x, y=y)
        results = curve_fitting_numpy(model=model, x=x, y=y)
        res = re.fullmatch(pattern=r"(?P<id>\d+).*", string=os.path.basename(filepath))
        assert res
        return {"id": int(res.group("id")), **results}
    except Exception as e:
        raise type(e)(filepath, str(e))
