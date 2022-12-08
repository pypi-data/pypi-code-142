import torch
import tensorflow as tf
import numpy as np

def convert_pytorch_to_tensorflow(pytorch_model: torch.nn.Module) -> tf.keras.Model:
    # Convert the PyTorch model to a TensorFlow model
    tensorflow_model = tf.keras.Sequential()
    
    for layer in pytorch_model.children():
        

        if isinstance(layer, torch.nn.Linear):
            if layer.weight is not None and layer.bias is not None:
                
                tensorflow_model.add(tf.keras.layers.Dense(layer.out_features,
                                                       input_dim=layer.in_features,
                                                       weights=[np.transpose(layer.weight.data.numpy()), layer.bias.data.numpy()]))
        elif isinstance(layer, torch.nn.Conv2d):
            if layer.weight is not None and layer.bias is not None:
               
            padding = 'valid' if layer.padding == 0 else 'same'
           
            tensorflow_model.add(tf.keras.layers.Conv2D(layer.out_channels,
                                                        layer.kernel_size,
                                                        strides=layer.stride,
                                                        padding=padding,
                                                        weights=[layer.weight, layer.bias]
                                                        ))
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
            
            tensorflow_model_seq = tf.keras.Sequential()
            # Iterate over the layers in the Sequential layer and convert each layer to a TensorFlow layer
            for sublayer in layer.children():
                if(len(list((sublayer.children()))) != 0):
                   
                    
                    for subblayer in sublayer.children():
                        
                       
                        if isinstance(subblayer, torch.nn.Conv2d):
                            # Check if the weight and bias attributes are defined
                            # if sublayer.weight is not None and sublayer.bias is not None:
                            
                            padding = 'valid' if subblayer.padding == 0 else 'same'
                            # Conv2D(64, (3, 3), strides=(1, 1), padding="same", use_bias=False)
                            tensorflow_model_seq.add(tf.keras.layers.Conv2D(subblayer.out_channels, (3, 3), strides=(1, 1), padding="same", use_bias=False))
                        elif isinstance(subblayer, torch.nn.ReLU):
                                
                                tensorflow_model_seq.add(tf.keras.layers.ReLU())
                        elif isinstance(subblayer, torch.nn.MaxPool2d):
                                
                                padding = 'valid' if subblayer.padding == 0 else 'same'
                                tensorflow_model_seq.add(tf.keras.layers.MaxPool2D(layer.kernel_size,
                                                                strides=layer.stride,
                                                                padding=padding))
                        elif isinstance(subblayer, torch.nn.BatchNorm2d):
                                # Add a case for the BatchNorm2d layer
                               
                                tensorflow_model_seq.add(tf.keras.layers.BatchNormalization())
                        elif isinstance(subblayer, torch.nn.AdaptiveAvgPool2d):
                                
                                tensorflow_model_seq.add(tf.keras.layers.GlobalAveragePooling2D())
                else:
                        if isinstance(sublayer, torch.nn.Conv2d):
                            # Check if the weight and bias attributes are defined
                            # if sublayer.weight is not None and sublayer.bias is not None:
                            padding = 'valid' if sublayer.padding == 0 else 'same'
                            
                            tensorflow_model.add(tf.keras.layers.Conv2D(filters=sublayer.out_channels,
                                                                            kernel_size=sublayer.kernel_size,
                                                                            strides=sublayer.stride,
                                                                            padding=padding,
                                                                            weights=[sublayer.weight, sublayer.bias]))
                        elif isinstance(sublayer, torch.nn.ReLU):
                                tensorflow_model.add(tf.keras.layers.ReLU())
                        elif isinstance(sublayer, torch.nn.MaxPool2d):
                                padding = 'valid' if sublayer.padding == 0 else 'same'
                                tensorflow_model.add(tf.keras.layers.MaxPool2D(layer.kernel_size,
                                                                strides=layer.stride,
                                                                padding=padding))
                        elif isinstance(sublayer, torch.nn.BatchNorm2d):
                                # Add a case for the BatchNorm2d layer
                                tensorflow_model.add(tf.keras.layers.BatchNormalization())
                        elif isinstance(sublayer, torch.nn.AdaptiveAvgPool2d):
                                tensorflow_model.add(tf.keras.layers.GlobalAveragePooling2D())
            tensorflow_model.add(tensorflow_model_seq)        
                                                                        

        else:
            raise NotImplementedError('Unknown PyTorch layer: {}'.format(layer.__class__.__name__))
        

    return tensorflow_model
