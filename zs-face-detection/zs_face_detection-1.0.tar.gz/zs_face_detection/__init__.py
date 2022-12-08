import os
import sys
import copy

old_path = copy.deepcopy(sys.path)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from inference_onnx_face_detection import Model_SCRFD_ONNX
# from inference_ncnn_face_detection import Model_SCRFD_Ncnn
from inference_openvino_face_detection import Model_SCRFD_Openvino

# model_scrfd = Model_SCRFD_ONNX()
# model_scrfd = Model_SCRFD_Ncnn()
model_scrfd = Model_SCRFD_Openvino()


def get_face_position(image_bgr):
    face_position = model_scrfd.run(image_bgr)
    return face_position


sys.path = old_path
