import time
import warnings
warnings.filterwarnings('ignore')
import os
import pickle
import glob
import json

from typing import Tuple, List
from multiprocessing import Pool
#import multiprocess as mp
import concurrent.futures
import multiprocessing as mp
from pathlib import Path
from sklearn.metrics.pairwise import euclidean_distances

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm

from h_add import get_optimal_sequence_add
from h_nrm import get_optimal_sequence_nrm
from estimate_scenes_count import estimate_scenes_count
#from evaluation import calculate_interval_metric

import torch
from img2vec_pytorch import Img2Vec
from PIL import Image
import pandas as pd
import cv2
from numpy import dot
from numpy.linalg import norm
img2vec = Img2Vec(cuda=False)
from os.path import isfile, join
from video_multiprocess import save_shots, compute_feature_vectors

from scenedetect import VideoManager
from scenedetect import SceneManager

# For content-aware scene detection:
from scenedetect.detectors import ContentDetector

class VideoSceneDetect:
    def __init__(self, videopath, shots_threshold = 30.0):
        self.video_path = videopath
        self.shots_threshold = shots_threshold

    def find_shots(self):
        # Create our video & scene managers, then add the detector.
        video_manager = VideoManager([self.video_path])
        scene_manager = SceneManager()
        scene_manager.add_detector(ContentDetector(threshold=self.shots_threshold))
        # Base timestamp at frame 0 (required to obtain the scene list).
        base_timecode = video_manager.get_base_timecode()
        # Improve processing speed by downscaling before processing.
        video_manager.set_downscale_factor()
        # Start the video manager and perform the scene detection.
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        # Each returned scene is a tuple of the (start, end) timecode.
        #self.shots = scene_manager.get_scene_list(base_timecode)
        return scene_manager.get_scene_list(base_timecode)

    def find_and_save_shots(self):
        shots = self.find_shots() 
        with Pool(os.cpu_count()) as p:
            p.map(save_shots, (shots))       
    
    # def save_videos():
    #     scene_name = folder_name + f'scene_{start_time}_{end_time}.avi'
    #     print(folder_name)
    #     convert_frames_to_video(folder_name,scene_name,fps = 24.0)
    #     currentFrame = end_frame

    def shots_to_features(self):
        folders = os.listdir('shots/')
        #folders.sort(key = lambda x: x[:-4])
        with Pool(os.cpu_count()) as p:
            p.map(compute_feature_vectors, (folders))

    def compute_similarity_matrix(self):
        distance_matrix = np.zeros((len(os.listdir('shots_embeddings')), len(os.listdir('shots_embeddings'))))
        data = {}
        for f in tqdm(glob.glob("shots_embeddings/*.json")): 
            with open(f,) as infile:
                data.update(json.load(infile))
        for i, (ke_1, val_1) in tqdm(enumerate(data.items())):
            for j, (ke_2, val_2) in enumerate(data.items()):
                #print(ke_1, val_1, ke_2, val_2)
                distance_matrix[i,j] = euclidean_distances(val_1, val_2).item()
        folder_name = 'distance_matrix'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        pd.DataFrame(distance_matrix).to_csv(os.path.join(str(os.getcwd()) + '/' + folder_name + '/', 'distance_matrix.csv'), index = False)
        return distance_matrix

    def get_optimal_scene(self, dist_mat):
        distances = dist_mat
        K = estimate_scenes_count(distances)
        print('optimal_scenes_count:', K)
        return get_optimal_sequence_add(distances, K)

    def save_scenes(self, f, video_path):
        start_index = 0
        scenes = os.listdir('shots_embeddings')
        for indx, end_index in tqdm(enumerate(f)):
            print(start_index, end_index)
            get_time = scenes[start_index: end_index]
            #print(get_time)
            start_time = str(get_time[0]).replace('.json', '').replace('scene_', '').split('_to_')[0].replace('_',':')
            end_time = str(get_time[-1]).replace('.json', '').split('_to_')[1].replace('_',':')
            start_time_ = list(start_time)
            end_time_ = list(end_time)
            start_time_[-4] = '.'
            end_time_[-4] = '.'
            #end_time_[-3:] = '000'
            #start_time_[-1] = '1'
            final_start_time = ''.join(start_time_)
            final_end_time = ''.join(end_time_)
            print(f'final start time is {final_start_time} and endtime is {final_end_time}')
            folder_name = 'scenes_output'
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            start_index = end_index
            os.system(f'ffmpeg -i {video_path} -ss {final_start_time} -to {final_end_time} -c copy scenes_output/scene_{indx}.mp4')
    
    def convert_frames_to_video(self, pathIn, pathOut, fps):
        self.shots = self.find_shots()
        frame_array = []
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
        #for sorting the file names properly
        # files = sorted(files)
        # print(files)
        files.sort(key = lambda x: int(x[5:-4]))
        for i in range(len(files)):
            filename=pathIn + files[i]
            #reading each files
            img = cv2.imread(filename)
            height, width, _ = img.shape
            size = (width,height)
            #print(filename)
            #inserting the frames into an image array
            frame_array.append(img)
        out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i in range(len(frame_array)):
            # writing to a image array
            out.write(frame_array[i])
        out.release()
