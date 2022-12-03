import warnings
warnings.filterwarnings('ignore')
import cv2
import os
from tqdm import tqdm, tqdm_notebook
import json
from PIL import Image
import numpy as np 
from img2vec_pytorch import Img2Vec
img2vec = Img2Vec(cuda=False) 
import codecs
import re

video_path = 'D:/Projects/zee5-datascience/scene_detection/data/Kumkum_Bhagya.mp4'
def save_shots(shots):
    currentFrame = shots[0].get_frames()
    #print(f'current frame is:', currentFrame)
    end_frame = shots[1].get_frames()
    start_time = shots[0].get_timecode()
    end_time = shots[1].get_timecode()  
    cap = cv2.VideoCapture(video_path)
    cap.set(1, currentFrame)
    frame_ = currentFrame

    for j in range(frame_, end_frame):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Saves image of the current frame in jpg file
        folder_name = f'shots/shots_{start_time}_to_{end_time}/'
        folder_name = str(folder_name.replace(':', '_').replace('.', '_'))
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # Saves image of the current frame in jpg file
        name = folder_name + 'frame' + str(j) + '.jpg'           
        #print ('Creating...' + name)
        cv2.imwrite(name, frame)

def compute_feature_vectors(folder):
    vec_1 = []
    shots_dict = {}
    for i, img in tqdm(enumerate(os.listdir(os.path.join(str(os.getcwd()) + '/shots/', folder)))):
        if '.jpg' in img:
            img_1 = Image.open(os.path.join(str(os.getcwd()) + '/shots/' + folder, img))
            vec_1.append(img2vec.get_vec(img_1, tensor=True).squeeze(2).squeeze(2).detach().numpy())
    vec_1 = np.array(vec_1, dtype = float) 
    vec_1 = vec_1.mean(axis = 0)
    print(f'vector 1 shape is {vec_1.shape}')
    vec = vec_1.tolist()
    shots_dict[str(folder)] = vec
    folder_name = 'shots_embeddings'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = f"{str(folder).replace('shots_', 'scene_')}.json" ## your path variable
    json.dump(shots_dict, codecs.open(os.path.join(str(os.getcwd() + '/shots_embeddings/' + file_path)), 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format

def load_images_from_folder(folder):
    images = []
    files = os.listdir(folder)
    files.sort(key=lambda f: int(re.sub('\D', '', f)))
    #print(files)
    for filename in files:
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images