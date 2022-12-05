#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Torchscript.py
@Time    :   2022/11/24 17:43:35
@Author  :   Moyan 
'''
import os
import torch
import logging
import numpy as np
from abc import ABCMeta, abstractclassmethod

class TorchScriptModel(metaclass=ABCMeta):

    def __init__(self, model_path, device) -> None:
        assert os.path.exists(model_path), "model path is not exist!"
        self.device = device
        self.model = torch.jit.load(model_path, map_location=self.device)
        self.model.eval()
        logging.info("torchscript model init done!")

    @abstractclassmethod
    def preprocess(self):
        pass

    @abstractclassmethod
    def postprocess(self):
        pass

    def __forward(self, input_tensor):
        return self.model(input_tensor)

    def run(self, x:np.ndarray):
        input_tensor = self.preprocess(x)
        output_tensor = self.__forward(input_tensor)
        return self.postprocess(output_tensor)