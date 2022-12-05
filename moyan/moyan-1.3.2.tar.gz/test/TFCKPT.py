#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   TFCKPT.py
@Time    :   2022/11/28 15:25:28
@Author  :   Moyan 
'''
import os
import tensorflow as tf

class TFCraph():

    def __init__(self, input_shape=[None, None, None, 1], input_name="input_images", model_define=None) -> None:
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.input_tensor = tf.placeholder(
                tf.float32, 
                shape=input_shape,
                name=input_name
            )
            self.global_step = tf.get_variable(
                'global_step',
                [],
                initializer=tf.constant_initializer(0),
                trainable=False
            )
            # self.model = model_define.model(
            #     self.input_tensor,
            #     outputs=output_kernel_num,
            # )




def main():
    pass
    
if __name__ == '__main__':
    main()