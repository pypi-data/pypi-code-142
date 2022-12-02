import math
import pandas as pd
import numpy as np
from hdbscan import HDBSCAN
from MS_visualizer.controller.func import create_table_df


class HDBSCAN_SCALED:
    def __init__(self, x_scale: float = 1, y_scale: float = 1, z_scale: float = 1, **kwargs):

        self.x_scale = float(x_scale) / 1000
        self.y_scale = float(y_scale)
        self.z_scale = float(z_scale)
        self.hdbscan = HDBSCAN(**kwargs)

    def fit(self, X):
        X = X.copy()
        X[:, 0] /= self.x_scale
        X[:, 1] /= self.y_scale
        X[:, 2] /= self.z_scale
        return self.hdbscan.fit(X)


def cluster(df: pd.DataFrame, x_axis, y_axis, z_axis, algorithm, metric, generate_tree, approx_tree, display_probability_by_pointsize,
            remove_noise, point_repetition, alpha, leaf_size, min_cluster, min_samples, cluster_selection_epsilon, x_scale, y_scale, z_scale,
            minimal_datapoints_per_cluster):
    """

    """

    if 'True' in generate_tree:
        gen_min_span_tree = True
    else:
        gen_min_span_tree = False

    if 'True' in approx_tree:
        approx_min_span_tree = True
    else:
        approx_min_span_tree = False

    # point repetition:
    if 'True' in point_repetition:
        reps = [math.floor(math.log2(intensity/10)) if (intensity > 40) else 1 for intensity in df.intensity]
        df = df.loc[np.repeat(df.index.values, reps)]

    clusterer = HDBSCAN_SCALED(
        x_scale=x_scale,
        y_scale=y_scale,
        z_scale=z_scale,
        algorithm=algorithm,
        metric=metric,
        gen_min_span_tree=gen_min_span_tree,
        approx_min_span_tree=approx_min_span_tree,
        alpha=float(alpha),
        leaf_size=int(leaf_size),
        min_cluster_size=int(min_cluster),
        min_samples=int(min_samples),
        cluster_selection_epsilon=float(cluster_selection_epsilon)
    )


    dff = df.copy()[[x_axis, y_axis, z_axis]]
    numpy_array = dff.to_numpy()
    clusterer.fit(numpy_array)

    # add cluster values to df - this column will be used to color the graph by cluster groups
    df['cluster'] = clusterer.hdbscan.labels_
    df['probability'] = clusterer.hdbscan.probabilities_

    df = df.drop_duplicates()

    cluster_size_df = create_table_df(df)

    df = pd.merge(df, cluster_size_df)

    df.loc[df.number < minimal_datapoints_per_cluster, 'cluster'] = -1


    # remove noise
    if 'True' in remove_noise:
        df = df.drop(df[df.cluster == -1].index)

    return df
