import pandas as pd
import numpy as np
from hdbscan import HDBSCAN


def cluster(df: pd.DataFrame, x_axis, y_axis, z_axis, algorithm, metric, generate_tree, approx_tree, display_probability_by_pointsize, remove_noise, alpha, leaf_size, min_cluster, min_samples, cluster_selection_epsilon):
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


    clusterer = HDBSCAN(algorithm=algorithm,
                        metric=metric,
                        gen_min_span_tree=gen_min_span_tree,
                        approx_min_span_tree=approx_min_span_tree,
                        alpha=float(alpha),
                        leaf_size=leaf_size,
                        min_cluster_size=min_cluster,
                        min_samples=min_samples,
                        cluster_selection_epsilon=cluster_selection_epsilon
                        )


    dff = df.copy()[[x_axis, y_axis, z_axis]]
    numpy_array = dff.to_numpy()

    clusterer.fit(numpy_array)


    # add cluster values to df - this column will be used to color the graph by cluster groups
    df['cluster'] = clusterer.labels_
    df['probability'] = clusterer.probabilities_

    # remove noise
    if 'True' in remove_noise:
        df = df.drop(df[df.cluster == -1].index)

    return df

