#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tflite_ssd.py
@Time    :   2022/11/23 18:14:20
@Author  :   Moyan 
'''
import os
import sys
sys.path.insert(0, "D:\Code\AI-in-air\moyan\test")

import cv2
import numpy as np
from TFLite import TFLiteModel

class SSDTFliteModel(TFLiteModel):
    def __init__(self, 
        model_path: str, input_size=320, threshhold=0.5) -> None:
        super().__init__(model_path)
        self.origin_height=0
        self.origin_weight=0
        self.input_size=input_size
        self.threshhold=threshhold
        
    def preprocess(self, image:np.ndarray):
        self.origin_height, self.origin_weight = image.shape[:2]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im = cv2.resize(image, (self.input_size, self.input_size), interpolation=cv2.INTER_LINEAR)
        im = im.astype("float32")
        im = im*(1.0/127.5)-1.0
        im = im[None,:,:,:]
        return im 

    def postprocess(self, output_tensor):
        '''
        output_tensor: [[bbox], [class], [score], [num_output]]
            bbox:   (1, 10, 4)
            class:  (1, 10)
            score:  (1, 10)
            num_output: (1,)
        '''
        predict_bboxes = output_tensor[0].squeeze() # (10, 4)
        predict_classes = output_tensor[1].squeeze() # (10,)
        predict_scores = output_tensor[2].squeeze() # (10,)
        select_index = predict_scores>self.threshhold
        predict_bboxes = predict_bboxes[select_index]
        predict_classes = predict_classes[select_index]
        predict_scores = predict_scores[select_index]
        # rescale to origin size
        predict_bboxes[:, 0] *= self.origin_height
        predict_bboxes[:, 2] *= self.origin_height
        predict_bboxes[:, 1] *= self.origin_weight
        predict_bboxes[:, 3] *= self.origin_weight
        # y1, x1, y2, x2 -> x1, y1, x2, y2
        predict_bboxes[:, [0, 1, 2, 3]] = predict_bboxes[:, [1, 0, 3, 2]]
        # index 0 is background
        predict_classes = predict_classes.astype(np.int32) + 1
        assert len(predict_bboxes) == len(predict_classes) == len(predict_scores)
        return predict_bboxes, predict_classes, predict_scores


def main():

    model_path = r"D:\Code\AI-in-air\moyan\ssd_mobilenet_v3_float.tflite"
    model = SSDTFliteModel(model_path)
    
    img_path = r"D:\Code\AI-in-air\moyan\od_test.jpg"
    im = cv2.imread(img_path)
    bbox, label, score = model.run(im)
    print(bbox)

    from PIL import Image, ImageDraw
    image = Image.open(img_path)
    draw = ImageDraw.Draw(image)

    for box in bbox:
        print(box)
        draw_bbox = box.astype(np.int32).tolist()
        print(draw_bbox)
        draw.rectangle(draw_bbox, outline=(0,0,255))
    image.show()

if __name__ == '__main__':
    main()