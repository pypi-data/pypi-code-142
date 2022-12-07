import cv2
import sys
import numpy as np
from PIL import Image
from io import BytesIO
from functools import partial
import tritonclient.grpc as grpcclient
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException

from afilter_vsp.utils.transform import imnormalize

if sys.version_info >= (3, 0):
    import queue
else:
    import Queue as queue

# Callback function used for async_stream_infer()
def completion_callback(user_data, result, error):
    # passing error raise and handling out
    user_data._completed_requests.put((result, error))

class UserData:

    def __init__(self):
        self._completed_requests = queue.Queue()

user_data = UserData()

def get_img(cam_data):
    # cam = Image.frombytes(mode="RGBA", size=(cam_data.rows,cam_data.cols), data=cam_data.mat_data, decoder_name="raw")
    cam = Image.open(BytesIO(cam_data.mat_data))
    cam = cv2.cvtColor(np.asarray(cam), cv2.COLOR_RGB2BGR)
    mean=[123.675, 116.28, 103.53]
    std=[58.395, 57.12, 57.375]
    to_rgb = True
    mean = np.array(mean, dtype=np.float32)
    std = np.array(std, dtype=np.float32)
    cam = imnormalize(cam, mean, std, to_rgb)
    # cam = cam.convert("RGB")
    # cam = np.asarray(cam)
    # cam = cam / 255.0
    cam = cam.transpose(2, 0, 1)
    # cam = np.transpose(cam, axes=[0, 3, 1, 2])
    # cam = cam.astype(np.float32)

    # cad = Image.frombytes(mode="RGBA", size=(cad_data.rows,cad_data.cols), data=cad_data.mat_data, decoder_name="raw").convert('L')
    # cad = np.asarray(cad)
    # cad = cad / 255.0
    # cad = np.expand_dims(cad, axis=0)
    # cam = np.expand_dims(cam, axis=0)
    cam = np.expand_dims(cam, axis=0)
    return cam.astype(np.float32)
    

def slide_inference(protocol, triton_client, model_name, requests, out_channels=1, set_async=True):
    """Inference by sliding-window with overlap.

    If h_crop > h_img or w_crop > w_img, the small patch will be used to
    decode without padding.
    """
    preds = []
    for request in requests:
        img = get_img(request.cam_data)
        test_cfg=dict(mode='slide', crop_size=(600, 600), stride=(512, 512))
        h_stride, w_stride = test_cfg['stride']
        h_crop, w_crop = test_cfg['crop_size']
        batch_size, _, h_img, w_img = img.shape
        out_channels = out_channels
        h_grids = max(h_img - h_crop + h_stride - 1, 0) // h_stride + 1
        w_grids = max(w_img - w_crop + w_stride - 1, 0) // w_stride + 1
        pred = np.zeros((batch_size, out_channels, h_img, w_img))
        count_mat = np.zeros((batch_size, 1, h_img, w_img))
        crop_imgs = []
        img_ranges = []
        for h_idx in range(h_grids):
            for w_idx in range(w_grids):
                y1 = h_idx * h_stride
                x1 = w_idx * w_stride
                y2 = min(y1 + h_crop, h_img)
                x2 = min(x1 + w_crop, w_img)
                y1 = max(y2 - h_crop, 0)
                x1 = max(x2 - w_crop, 0)
                crop_img = img[:, :, y1:y2, x1:x2]
                crop_imgs.append(crop_img)
                img_ranges.append((y1,y2,x1,x2))
        crop_seg_logits = get_defects(protocol, triton_client, model_name, crop_imgs, set_async)
        for crop_seg_logit, img_range in zip(crop_seg_logits, img_ranges):
            y1,y2,x1,x2=img_range
            pred += np.pad(crop_seg_logit, ((int(y1), int(pred.shape[2] - y2)),
                            (int(x1), int(pred.shape[3] - x2))), 'constant', constant_values=(0, 0))
            count_mat[:, :, y1:y2, x1:x2] += 1
        assert (count_mat == 0).sum() == 0
        preds.append(pred / count_mat)
    return [Image.fromarray(np.squeeze(pred.astype('uint8')), mode='L') for pred in preds]


def get_defects(protocol, triton_client, model_name, crop_imgs, set_async):
    REQ_NUM = len(crop_imgs)
    inputs_data = []
    for crop_img in crop_imgs:
        inputs_data.append(crop_img)
    outputs_data = []
    try:
        if protocol =='grpc':
            inputs = [[grpcclient.InferInput(f'input', [1, 3, 600, 600], "FP32")] for i in range(REQ_NUM)]
            [inputs[i][0].set_data_from_numpy(inputs_data[i]) for i in range(REQ_NUM)]
            outputs = [[grpcclient.InferRequestedOutput(f'output')] for i in range(REQ_NUM)]
            if set_async:
                [triton_client.async_infer(model_name=model_name,
                                            inputs=inputs[i],
                                            callback=partial(completion_callback, user_data),
                                            outputs=outputs[i]) for i in range(REQ_NUM)]
                # outputs_data=user_data._completed_requests.get()
                processed_count = 0
                while processed_count < REQ_NUM:
                    (response, error) = user_data._completed_requests.get()
                    processed_count += 1
                    if error is not None:
                        print("Triton gRCP inference failed: " + str(error))
                        sys.exit(1)
                    outputs_data.append(response)
                # results = [output_data.as_numpy('output') for output_data in outputs_data]
            else:
                outputs_data = [triton_client.infer(model_name=model_name,
                                                    inputs=inputs[i],
                                                    outputs=outputs[i]) for i in range(REQ_NUM)]
        else:
            inputs = [[httpclient.InferInput('input', [1, 3, 600, 600], "FP32")] for i in range(REQ_NUM)]
            [inputs[i][0].set_data_from_numpy(inputs_data[i], binary_data=True) for i in range(REQ_NUM)]
            outputs = [[httpclient.InferRequestedOutput('output', binary_data=True)] for i in range(REQ_NUM)]
            if set_async:
                async_outputs = [triton_client.async_infer(model_name=model_name,
                                                        inputs=inputs[i],
                                                        outputs=outputs[i]) for i in range(REQ_NUM)]
                [outputs_data.append(async_output.get_result()) for async_output in async_outputs]
            else:
                outputs_data = [triton_client.infer(model_name=model_name,
                                                    inputs=inputs[i],
                                                    outputs=outputs[i]) for i in range(REQ_NUM)]
        results = [output_data.as_numpy('output') for output_data in outputs_data]
    except InferenceServerException as e:
            print("inference failed: " + str(e))
            sys.exit(1)

    # return [Image.fromarray(np.squeeze(result.astype('uint8')), mode='L') for result in results]
    return [np.squeeze(result.astype('uint8')) for result in results]
