import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN


def cluster(df: pd.DataFrame, x_axis, y_axis, z_axis, metric, remove_noise, eps, leaf_size, min_samples):

    clusterer = DBSCAN(eps=float(eps), min_samples=min_samples, metric=metric, leaf_size=leaf_size)

    dff = df.copy()[[x_axis, y_axis, z_axis]]

    numpy_array = dff.to_numpy()

    clusterer.fit(numpy_array)

    df['cluster'] = clusterer.labels_

    if 'True' in remove_noise:
        df = df.drop(df[df.cluster == -1].index)


    return df
