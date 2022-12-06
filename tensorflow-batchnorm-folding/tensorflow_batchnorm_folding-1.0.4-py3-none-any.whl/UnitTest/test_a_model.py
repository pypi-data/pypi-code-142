import tensorflow as tf
import numpy as np
from typing import Tuple


def test_model_changes(
    model: tf.keras.Model,
    folded_model: tf.keras.Model,
    input_shape: Tuple[int] = (1, 224, 224, 3),
) -> None:
    """
    Measure the difference between the original and folded model on a random input

    Args:
        model: original model before folding
        folded_model: new model after folding
    """
    err = 0
    for _ in range(100):
        x = np.random.normal(size=input_shape)
        y_original = model(x)
        y_folded = folded_model(x)
        err += np.sum(np.abs(y_folded - y_original))
    result_color = "\033[92m"
    if err > 0.01:
        result_color = "\033[91m"
    print(
        f"[\033[94mError\033[0m] model [\033[94m{model.name}\033[0m]"
        f" error = {result_color}{err:.3f}\033[0m"
    )
