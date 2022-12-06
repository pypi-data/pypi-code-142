from batch_normalization_folding.TensorFlow.calculus import *
import tensorflow as tf
import numpy as np
from typing import Dict
import sys


def fold_leaf_forward(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    epsilon: float = 1.0e-3,
):
    """ """
    if isinstance(layer, tf.keras.layers.Conv2D):
        layer.set_weights(
            fold_leaf_forward_conv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
        layer.set_weights(
            fold_leaf_forward_depthwiseconv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.Dense):
        layer.set_weights(
            fold_leaf_forward_dense(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    else:
        print(f"folding foward leaf of type BN is not supported yet")
        sys.exit()


def fold_leaf_backward(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    epsilon: float = 1.0e-3,
):
    """ """
    if isinstance(layer, tf.keras.layers.Conv2D):
        layer.set_weights(
            fold_leaf_backward_conv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
        layer.set_weights(
            fold_leaf_backward_depthwiseconv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.Dense):
        layer.set_weights(
            fold_leaf_backward_dense(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    else:
        layer.set_weights(
            fold_leaf_backward_bn(
                epsilon=epsilon,
                gamma_=layer.weights[0].numpy(),
                beta_=layer.weights[1].numpy(),
                mu_=layer.weights[2].numpy(),
                sigma_=layer.weights[3].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )


def fold_leaf(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    forward: bool,
    epsilon: float = 1.0e-3,
):
    """ """
    if forward:
        fold_leaf_forward(
            epsilon=epsilon, gamma=gamma, beta=beta, mu=mu, sigma=sigma, layer=layer
        )
    else:
        fold_leaf_backward(
            epsilon=epsilon, gamma=gamma, beta=beta, mu=mu, sigma=sigma, layer=layer
        )


def fold_root_forward(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    epsilon: float = 1.0e-3,
):
    """ """
    if isinstance(layer, tf.keras.layers.Conv2D):
        layer.set_weights(
            fold_root_forward_conv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
        layer.set_weights(
            fold_root_forward_depthwiseconv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.Dense):
        layer.set_weights(
            fold_root_forward_dense(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    else:
        print(f"folding foward root of type BN is not supported yet")
        sys.exit()


def fold_root_backward(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    epsilon: float = 1.0e-3,
):
    """ """
    if isinstance(layer, tf.keras.layers.Conv2D):
        layer.set_weights(
            fold_root_backward_conv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.DepthwiseConv2D):
        layer.set_weights(
            fold_root_backward_depthwiseconv(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    elif isinstance(layer, tf.keras.layers.Dense):
        layer.set_weights(
            fold_root_backward_dense(
                epsilon=epsilon,
                W=layer.weights[0].numpy(),
                b=layer.weights[1].numpy(),
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
            )
        )
    else:
        new_W, new_b = fold_root_backward_bn(
            epsilon=epsilon,
            W=layer.weights[0].numpy(),
            b=layer.weights[1].numpy(),
            gamma=gamma,
            beta=beta,
            mu=mu,
            sigma=sigma,
        )
        layer.set_weights(
            [new_W, new_b, layer.weights[2].numpy(), layer.weights[3].numpy()]
        )


def fold_root(
    gamma: np.ndarray,
    beta: np.ndarray,
    mu: np.ndarray,
    sigma: np.ndarray,
    layer: tf.keras.layers.Layer,
    forward: bool,
    epsilon: float = 1.0e-3,
):
    """ """
    if forward:
        fold_root_forward(
            epsilon=epsilon, gamma=gamma, beta=beta, mu=mu, sigma=sigma, layer=layer
        )
    else:
        fold_root_backward(
            epsilon=epsilon, gamma=gamma, beta=beta, mu=mu, sigma=sigma, layer=layer
        )


def fold_weights(model: tf.keras.Model, fold_dict: Dict[str, tuple]):
    """
    performs the update of the weights to fold
    """
    for layer_name, (roots, leaves, forward) in fold_dict.items():
        bn_weights = model.get_layer(layer_name).weights
        weight_shape = bn_weights[0].numpy().shape
        epsilon = model.get_layer(layer_name).epsilon
        gamma = np.ones(weight_shape)
        beta = np.zeros(weight_shape)
        mu = np.zeros(weight_shape)
        sigma = np.ones(weight_shape)
        for theta in bn_weights:
            if "gamma:0" in theta.name:
                gamma = theta.numpy()
            elif "beta:0" in theta.name:
                beta = theta.numpy()
            elif "moving_mean:0" in theta.name:
                mu = theta.numpy()
            elif "moving_variance:0" in theta.name:
                sigma = theta.numpy()

        for leaf in leaves:
            fold_leaf(
                epsilon=epsilon,
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
                layer=model.get_layer(leaf),
                forward=forward,
            )
        for root in roots:
            fold_root(
                epsilon=epsilon,
                gamma=gamma,
                beta=beta,
                mu=mu,
                sigma=sigma,
                layer=model.get_layer(root),
                forward=forward,
            )
