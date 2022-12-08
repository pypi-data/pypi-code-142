import torch
import tensorflow as tf

def convert_pytorch_to_tensorflow(pytorch_model: torch.nn.Module) -> tf.keras.Model:
    # Convert the PyTorch model to a TensorFlow model
    tensorflow_model = tf.keras.Sequential()
    for layer in pytorch_model.children():
        if isinstance(layer, torch.nn.Linear):
            tensorflow_model.add(tf.keras.layers.Dense(layer.out_features,
                                                       input_dim=layer.in_features,
                                                       weights=[layer.weight.data.numpy(), layer.bias.data.numpy()]))
        elif isinstance(layer, torch.nn.Conv2d):
            tensorflow_model.add(tf.keras.layers.Conv2D(layer.out_channels,
                                                        layer.kernel_size,
                                                        strides=layer.stride,
                                                        padding=layer.padding,
                                                        weights=[layer.weight.data.numpy(), layer.bias.data.numpy()]))
        elif isinstance(layer, torch.nn.ReLU):
            tensorflow_model.add(tf.keras.layers.ReLU())
        elif isinstance(layer, torch.nn.MaxPool2d):
            tensorflow_model.add(tf.keras.layers.MaxPool2D(layer.kernel_size,
                                                           strides=layer.stride,
                                                           padding=layer.padding))
        else:
            raise NotImplementedError('Unknown PyTorch layer: {}'.format(layer.__class__.__name__))

    return tensorflow_model
