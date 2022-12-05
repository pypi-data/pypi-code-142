#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   TFLite.py
@Time    :   2022/11/23 16:08:02
@Author  :   Moyan 
'''
import os
import numpy as np
import tensorflow as tf
from abc import ABCMeta, abstractclassmethod


class TFLiteModel(metaclass=ABCMeta):

    def __init__(self, model_path: str) -> None:
        assert os.path.exists(model_path), "model_path is not exists!"
        self.interpreter = tf.lite.Interpreter(model_path)
        self.interpreter.allocate_tensors()
        self._input_details = self.interpreter.get_input_details()
        self._output_details = self.interpreter.get_output_details()

    @abstractclassmethod
    def preprocess(self):
        pass

    @abstractclassmethod
    def postprocess(self):
        pass
    
    def __forward(self, input_tensor):
        assert len(self._input_details)==1, "only one input accept!"
        assert tuple(self._input_details[0]["shape"])==input_tensor.shape, "input_tensor shape is wrong!"

        self.interpreter.set_tensor(self._input_details[0]['index'],  input_tensor)
        self.interpreter.invoke()

        results = []
        for i in range(len(self._output_details)):
            output = self.interpreter.get_tensor(self._output_details[i]["index"])
            results.append(output)
        return results

    def run(self, x:np.ndarray):
        input_tensor = self.preprocess(x)
        output_tensor = self.__forward(input_tensor)
        return self.postprocess(output_tensor)

    def get_input_detais(self):
        return self._input_details
    
    def get_output_details(self):
        return self._output_details
