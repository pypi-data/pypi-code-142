import os
import time

import cv2
import numpy as np
from openvino.inference_engine import IECore  # openvino/inference_engine/ie_api.so


class Model_SCRFD_Openvino:
    """
    性别年龄检测
    openvino==2022.2.0  openvino框架88M 测试/home/lq_07/wzs/code/综合/new_project/皮肤样本照_0 910张图片
    openvino      2.6M 运行, mean time:0.010537598421285441
    openvino_fp16 1.4M 运行, mean time:0.011047713573162372
    """
    def __init__(self, fp16=True):
        pth_dir = os.path.dirname(os.path.abspath(__file__))  # score

        if fp16 == True:
            path = os.path.join(pth_dir, 'checkpoints', 'openvino_fp16', 'scrfd_500m_kps.xml')
        else:
            path = os.path.join(pth_dir, 'checkpoints', 'openvino', 'scrfd_500m_kps.xml')
        ie = IECore()
        net = ie.read_network(model=path)
        net.batch_size = 1
        self.model = ie.load_network(network=net, device_name="CPU")
        print(f'加载人脸检测openvino模型:{path}')
        time.sleep(2)

        # self.input_blob = next(iter(net.input_info))  # <class 'str'> images
        # self.out_blob = next(iter(net.outputs))  # <class 'str'> 9个输出
        # self.n, self.c, self.h, self.w = net.input_info[self.input_blob].input_data.shape  # 1 3 640, 640

        self.inpWidth = 640
        self.inpHeight = 640
        self.confThreshold = 0.5
        self.nmsThreshold = 0.5
        self.keep_ratio = True
        self.fmc = 3
        self._feat_stride_fpn = [8, 16, 32]
        self._num_anchors = 2

        self.dry_run()

    def dry_run(self):
        dummy_input = np.ones((1, 3, 640, 640), np.float32)
        input_name = 'images'
        for i in range(10):
            print('dry_run', i)
            self.model.infer(inputs={input_name: dummy_input})

    def resize_image(self, srcimg):
        padh, padw, newh, neww = 0, 0, self.inpHeight, self.inpWidth
        if self.keep_ratio and srcimg.shape[0] != srcimg.shape[1]:
            hw_scale = srcimg.shape[0] / srcimg.shape[1]
            if hw_scale > 1:
                newh, neww = self.inpHeight, int(self.inpWidth / hw_scale)
                img = cv2.resize(srcimg, (neww, newh), interpolation=cv2.INTER_AREA)
                padw = int((self.inpWidth - neww) * 0.5)
                img = cv2.copyMakeBorder(img, 0, 0, padw, self.inpWidth - neww - padw, cv2.BORDER_CONSTANT,
                                         value=0)  # add border
            else:
                newh, neww = int(self.inpHeight * hw_scale) + 1, self.inpWidth
                img = cv2.resize(srcimg, (neww, newh), interpolation=cv2.INTER_AREA)
                padh = int((self.inpHeight - newh) * 0.5)
                img = cv2.copyMakeBorder(img, padh, self.inpHeight - newh - padh, 0, 0, cv2.BORDER_CONSTANT, value=0)
        else:
            img = cv2.resize(srcimg, (self.inpWidth, self.inpHeight), interpolation=cv2.INTER_AREA)
        return img, newh, neww, padh, padw

    def distance2bbox(self, points, distance, max_shape=None):
        x1 = points[:, 0] - distance[:, 0]
        y1 = points[:, 1] - distance[:, 1]
        x2 = points[:, 0] + distance[:, 2]
        y2 = points[:, 1] + distance[:, 3]
        if max_shape is not None:
            x1 = x1.clamp(min=0, max=max_shape[1])
            y1 = y1.clamp(min=0, max=max_shape[0])
            x2 = x2.clamp(min=0, max=max_shape[1])
            y2 = y2.clamp(min=0, max=max_shape[0])
        return np.stack([x1, y1, x2, y2], axis=-1)

    def distance2kps(self, points, distance, max_shape=None):
        preds = []
        for i in range(0, distance.shape[1], 2):
            px = points[:, i % 2] + distance[:, i]
            py = points[:, i % 2 + 1] + distance[:, i + 1]
            if max_shape is not None:
                px = px.clamp(min=0, max=max_shape[1])
                py = py.clamp(min=0, max=max_shape[0])
            preds.append(px)
            preds.append(py)
        return np.stack(preds, axis=-1)

    def run(self, srcimg):
        ori_height, ori_width = srcimg.shape[0:2]
        img, newh, neww, padh, padw = self.resize_image(srcimg)
        data = cv2.dnn.blobFromImage(img, 1.0 / 128, (self.inpWidth, self.inpHeight), (127.5, 127.5, 127.5),
                                     swapRB=True)
        # data: <class 'numpy.ndarray'> float32 (1, 3, 640, 640) rgb
        # -> dict,9个关键字, 'out0'-'out8', onnx返回9个元素的tuple
        input_name = 'images'
        # output_name = ['out0', 'out3', 'out6', 'out1', 'out4', 'out7', 'out2', 'out5', 'out8']
        results = self.model.infer(inputs={input_name: data})
        outs = [results['out0'], results['out3'], results['out6'], results['out1'], results['out4'],
                results['out7'], results['out2'], results['out5'], results['out8']]
        # (1, 12800, 1) out0
        # (1, 12800, 4) out3
        # (1, 12800, 10) out6
        # (1, 3200, 1) out1
        # (1, 3200, 4) out4
        # (1, 3200, 10) out7
        # (1, 800, 1) out2
        # (1, 800, 4) out5
        # (1, 800, 10) out8
        # inference output
        scores_list, bboxes_list, kpss_list = [], [], []
        for idx, stride in enumerate(self._feat_stride_fpn):  # [8, 16, 32]  每个点预测两个框
            scores = outs[idx * self.fmc][0]
            bbox_preds = outs[idx * self.fmc + 1][0] * stride
            kps_preds = outs[idx * self.fmc + 2][0] * stride

            height = self.inpHeight // stride
            width = self.inpHeight // stride
            anchor_centers = np.stack(np.mgrid[:height, :width][::-1], axis=-1).astype(np.float32)  # 牛
            anchor_centers = (anchor_centers * stride).reshape((-1, 2))  # （6400,2）
            if self._num_anchors > 1:
                anchor_centers = np.stack([anchor_centers] * self._num_anchors, axis=1).reshape((-1, 2))

            pos_inds = np.where(scores >= self.confThreshold)[0]
            # 　(n, 2)　(n, 4)　<class 'numpy.ndarray'> float32
            bboxes = self.distance2bbox(anchor_centers, bbox_preds)
            pos_scores = scores[pos_inds]
            pos_bboxes = bboxes[pos_inds]
            scores_list.append(pos_scores)
            bboxes_list.append(pos_bboxes)

            kpss = self.distance2kps(anchor_centers, kps_preds)
            # kpss = kps_preds
            kpss = kpss.reshape((kpss.shape[0], -1, 2))
            pos_kpss = kpss[pos_inds]
            kpss_list.append(pos_kpss)

        scores = np.vstack(scores_list).ravel()  # ravel()展平
        bboxes = np.vstack(bboxes_list)
        kpss = np.vstack(kpss_list)
        bboxes[:, 2:4] = bboxes[:, 2:4] - bboxes[:, 0:2]  # (ltx,lty,rbx,rby) -> (ltx,lty,w,h)
        ratioh, ratiow = srcimg.shape[0] / newh, srcimg.shape[1] / neww
        bboxes[:, 0] = (bboxes[:, 0] - padw) * ratiow
        bboxes[:, 1] = (bboxes[:, 1] - padh) * ratioh
        bboxes[:, 2] = bboxes[:, 2] * ratiow
        bboxes[:, 3] = bboxes[:, 3] * ratioh
        kpss[:, :, 0] = (kpss[:, :, 0] - padw) * ratiow
        kpss[:, :, 1] = (kpss[:, :, 1] - padh) * ratioh
        # -> 二维numpy, 包含人脸的索引号,一般shape都为(1,1)，当出现多人脸时返回(n,1), 当没有人脸时返回tuple元祖类型,
        # 不管是返回<class 'numpy.ndarray'>或<class 'tuple'>,都可以使用len(indices)来判断人脸的个数
        indices = cv2.dnn.NMSBoxes(bboxes.tolist(), scores.tolist(), self.confThreshold, self.nmsThreshold)
        if len(indices) == 0:
            return np.array([])
        else:
            # 当有一个或多个人脸时, 按置信度排序
            face_positions = []
            for i in range(len(indices)):
                face_position = []
                index = indices[i]

                ltx = int(bboxes[index, 0])
                lty = int(bboxes[index, 1])
                rbx = int(bboxes[index, 0] + bboxes[index, 2])
                rby = int(bboxes[index, 1] + bboxes[index, 3])

                ltx = self.clamp(0, ori_width, ltx)
                lty = self.clamp(0, ori_height, lty)
                rbx = self.clamp(0, ori_width, rbx)
                rby = self.clamp(0, ori_height, rby)
                face_position.extend([ltx, lty, rbx, rby])

                for j in range(5):
                    x = int(kpss[index, j, 0])
                    y = int(kpss[index, j, 1])
                    x = self.clamp(0, ori_width, x)
                    y = self.clamp(0, ori_height, y)
                    face_position.extend([x, y])

                face_position.append(float(scores[index]))

                face_positions.append(face_position)
            face_positions = np.array(face_positions)
            return face_positions

    def clamp(self, min_value, max_value, data):
        if data < min_value:
            data = min_value
        elif data > max_value:
            data = max_value
        return data
