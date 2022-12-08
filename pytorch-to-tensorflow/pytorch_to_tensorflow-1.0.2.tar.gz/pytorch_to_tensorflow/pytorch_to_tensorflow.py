import torch
import tensorflow as tf

def convert_pytorch_to_tensorflow(pytorch_model: torch.nn.Module) -> tf.keras.Model:
    # Convert the PyTorch model to a TensorFlow model
    tensorflow_model = tf.keras.Sequential()
    for layer in pytorch_model.children():
        if isinstance(layer, torch.nn.Linear):
            if layer.weight is not None and layer.bias is not None:
                tensorflow_model.add(tf.keras.layers.Dense(layer.out_features,
                                                       input_dim=layer.in_features,
                                                       weights=[layer.weight.data.numpy(), layer.bias.data.numpy()]))
        elif isinstance(layer, torch.nn.Conv2d):
            if layer.weight is not None and layer.bias is not None:
                tensorflow_model.add(tf.keras.layers.Conv2D(layer.out_channels,
                                                        layer.kernel_size,
                                                        strides=layer.stride,
                                                        padding=layer.padding,
                                                        weights=[layer.weight.data.numpy(), layer.bias.data.numpy()]))
        elif isinstance(layer, torch.nn.ReLU):
            tensorflow_model.add(tf.keras.layers.ReLU())
        elif isinstance(layer, torch.nn.MaxPool2d):
            padding = 'valid' if layer.padding == 0 else 'same'
            tensorflow_model.add(tf.keras.layers.MaxPool2D(layer.kernel_size,
                                                           strides=layer.stride,
                                                           padding=padding))
        elif isinstance(layer, torch.nn.BatchNorm2d):
            # Add a case for the BatchNorm2d layer
            tensorflow_model.add(tf.keras.layers.BatchNormalization())
        elif isinstance(layer, torch.nn.AdaptiveAvgPool2d):
            tensorflow_model.add(tf.keras.layers.GlobalAveragePooling2D())
        elif isinstance(layer, torch.nn.Sequential):
            # Iterate over the layers in the Sequential layer and convert each layer to a TensorFlow layer
            for sublayer in layer.children():
                if isinstance(sublayer, torch.nn.Conv2d):
                    # Check if the weight and bias attributes are defined
                    if sublayer.weight is not None and sublayer.bias is not None:
                        tensorflow_model.add(tf.keras.layers.Conv2D(filters=sublayer.out_channels,
                                                                    kernel_size=sublayer.kernel_size,
                                                                    strides=sublayer.stride,
                                                                    padding=sublayer.padding,
                                                                    weights=[sublayer.weight.data.numpy(), sublayer.bias.data.numpy()]))
                    elif isinstance(layer, torch.nn.ReLU):
                        tensorflow_model.add(tf.keras.layers.ReLU())
                    elif isinstance(layer, torch.nn.MaxPool2d):
                        padding = 'valid' if layer.padding == 0 else 'same'
                        tensorflow_model.add(tf.keras.layers.MaxPool2D(layer.kernel_size,
                                                           strides=layer.stride,
                                                           padding=padding))
                    elif isinstance(layer, torch.nn.BatchNorm2d):
                        # Add a case for the BatchNorm2d layer
                          tensorflow_model.add(tf.keras.layers.BatchNormalization())
                    elif isinstance(layer, torch.nn.AdaptiveAvgPool2d):
                         tensorflow_model.add(tf.keras.layers.GlobalAveragePooling2D())
                                                                        

        else:
            raise NotImplementedError('Unknown PyTorch layer: {}'.format(layer.__class__.__name__))

    return tensorflow_model
