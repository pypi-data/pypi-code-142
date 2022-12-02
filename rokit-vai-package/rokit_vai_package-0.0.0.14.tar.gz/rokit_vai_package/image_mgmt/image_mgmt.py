import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from .. import global_variable as gv

def display_image_n_label(display_list):
    plt.figure(figsize=(15, 15))
    title = ['Input Image', 'True Mask', 'Predicted Mask']
    
    for i in range(len(display_list)):
        plt.subplot(1, len(display_list), i+1)
        plt.title(title[i])
        plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
        plt.axis('off')
    plt.show()

def _parse_protobuf_fn(record_bytes):        
    return tf.io.parse_single_example(            
        record_bytes,            
        {"image": tf.io.FixedLenFeature([], tf.string, default_value=''),
         "segmentation_mask": tf.io.FixedLenFeature([], tf.string, default_value='')}  
    )    

def normalize(input_image, input_mask):
    input_image = tf.cast(input_image, tf.float32) / 255.0
    input_mask -= 1
    return input_image, input_mask


def _decode_image_fn(image):  
        input_image = tf.image.resize(tf.io.decode_image(image['image'], expand_animations=False, channels=3), (128, 128))
        input_mask = tf.image.resize(tf.io.decode_png(image['segmentation_mask'], channels=1), (128, 128))     
        
        input_image, input_mask = normalize(input_image, input_mask)
        return input_image, input_mask

