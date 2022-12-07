#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   WarpUtil.py
@Time    :   2022/12/07 11:27:13
@Author  :   Moyan 
'''
import cv2
import math
import logging
import numpy as np

class WarpUtil:
    """
    input size type: (w, h)
        output_size: (1000, 800)
        expand_ratio: (0.12, 0.05) 
            expand_w = w * expand_ratio[0]
            expand_h = h * expand_ratio[1]
    min_size: mask的最小面积
    max_size: mask的最大面积
    epsilon_ratio
    """
    def __init__(
        self,
        output_size=None,
        expand=False,
        expand_ratio=(1./8, 1./20),
        min_size=0,
        max_size=np.inf,
        epsilon_ratio=0.05,
        ) -> None:
        self.origin_w = 0
        self.origin_h = 0        
        self.expand=expand
        self.expand_ratio=expand_ratio
        self.min_size=min_size
        self.max_size=max_size
        self.epsilon_ratio=epsilon_ratio
        self.output_size=output_size
        # 获取cv版本
        (cv_major, _, _) = cv2.__version__.split(".")
        self.cv_major = int(cv_major)
    
    def get_max_contour(self, mask):
        # 根据面积选取最大mask的contour
        if self.cv_major==4:
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)          
        if not contours:
            logging.info("mask findContours is None!")
            return None
        max_area = [cv2.contourArea(cn) for cn in contours]
        if max(max_area) > self.max_size:
            logging.info("mask max contours area>mask_size !")
            return None
        max_contour = contours[max_area.index(max(max_area))]
        return max_contour

    def get_max_rect_bbox(self, max_contour):
        xmin, ymin, w, h = cv2.boundingRect(max_contour)
        return [xmin, ymin, xmin+w, ymin+h]

    def sort_point_top_left_corner(self, points):
        #因为approxPolyDP得到的四个点是逆时针排序的，可以基于四个点到原点的距离将顺序转换成从左上角开始1234的顺序
        #                  1-----4
        # convert to:     |     |
        #                 2-----3
        L2_distance = [np.sqrt(np.sum(np.square(bb))) for bb in points]
        top_left_index = L2_distance.index(min(L2_distance))
        if top_left_index == 0:
            new_point = points.copy()
        elif top_left_index == 1:
            new_point = [points[1], points[2], points[3], points[0]]
        elif top_left_index == 2:
            new_point = [points[2], points[3], points[0], points[1]]
        elif top_left_index == 3:
            new_point = [points[3], points[0], points[1], points[2]]
        else:
            raise Exception("top_left_index erro!")
        return np.array(new_point)

    def get_max_polygon_point(self, max_contour):
        # 从最大的contour里得到四边形的四个点
        epsilon = self.epsilon_ratio * cv2.arcLength(max_contour, True)
        approx = cv2.approxPolyDP(max_contour, epsilon, True)
        points = approx.reshape((-1, 2)).astype(np.float32)
        if points.shape[0] != 4:
            logging.info("from max contour get polygon points shape is not 4!")
            return None
        sort_points = self.sort_point_top_left_corner(points)
        return sort_points

    def get_polygon_wh_from_distance(self, points):
        # 计算point3和point0之间的距离记作: polygon_w
        # 计算point2和point9之间的距离记作: polygon_h
        # |AB| = sqar((x1-x2)**2 + (y1-y2)**2) 
        polygon_w = math.sqrt((points[3][0]-points[0][0])**2 + (points[3][1]-points[0][1])**2)
        polygon_h = math.sqrt((points[1][0]-points[0][0])**2 + (points[1][1]-points[0][0])**2)
        return (polygon_w, polygon_h)

    def get_polygon_wh_from_minmax(self, point):
        # 将四个点最小x和最大x之间的距离记作: ploygon_w
        # 将四个点最小y和最大y之间的距离记作: ploygon_h
        min_x = np.min(point[:, 0])
        max_x = np.max(point[:, 0])
        min_y = np.min(point[:, 1])
        max_y = np.max(point[:, 1])
        polygon_w = max_x - min_x
        polygon_h = max_y - min_y
        return (polygon_w, polygon_h)

    def get_expand_point(self, points: np.ndarray, origin_size: tuple, ploygon_wh: tuple):
        ploygon_w, ploygon_h = ploygon_wh
        origin_w, origin_h = origin_size
        expend_w = ploygon_w * self.expand_ratio[0]
        expend_h = ploygon_h * self.expand_ratio[1]
        # 扩边+越界判断
        points[0][0] = (points[0][0]-expend_w) if (points[0][0]-expend_w>0) else 0
        points[0][1] = (points[0][1]-expend_h) if (points[0][1]-expend_h>0) else 0
        points[1][0] = (points[1][0]-expend_w) if (points[1][0]-expend_w>0) else 0
        points[1][1] = (points[1][1]+expend_h) if (points[1][1]+expend_h<origin_h) else origin_h
        points[2][0] = (points[2][0]+expend_w) if (points[2][0]+expend_w<origin_w) else origin_w
        points[2][1] = (points[2][1]+expend_h) if (points[2][1]+expend_h<origin_h) else origin_h
        points[3][0] = (points[3][0]+expend_w) if (points[3][0]+expend_w<origin_w) else origin_w
        points[3][1] = (points[3][1]-expend_h) if (points[3][1]-expend_h>0) else 0
        return points

    def do_warp(self, image: np.ndarray, source_points: np.ndarray, target_points: np.ndarray):
        M = cv2.getPerspectiveTransform(source_points, target_points)
        return cv2.warpPerspective(image, M, self.output_size)

    def run(self, image:np.ndarray, mask: np.ndarray):
        assert image.shape[:2] == mask.shape[:2], "image shape not equal mask shape!"
        origin_size = (image.shape[1], image.shape[0])
        max_contour = self.get_max_contour(mask.copy())
        if max_contour is None:
            return None
        polygon_point = self.get_max_polygon_point(max_contour)
        if polygon_point is None:
            return None
        if self.expand:
            polygon_wh = self.get_polygon_wh_from_distance(polygon_point)
            polygon_point = self.get_expand_point(polygon_point, origin_size, polygon_wh)
        if self.output_size is None:
            polygon_wh = self.get_polygon_wh_from_minmax(polygon_point)
            self.output_size = (int(polygon_wh[0]), int(polygon_wh[1]))
        target_points = np.array([
            [0, 0],
            [0, self.output_size[1]-1],
            [self.output_size[0]-1, self.output_size[1]-1],
            [self.output_size[0]-1, 0]
            ], dtype=np.float32
        )
        return self.do_warp(image.copy(), polygon_point, target_points)