from habana_frameworks.mediapipe.backend.nodes import opnode_tensor_info
from habana_frameworks.mediapipe.operators.media_nodes import MediaCPUNode
from habana_frameworks.mediapipe.backend.utils import get_str_dtype
from habana_frameworks.mediapipe.media_types import dtype as dt
import media_random_biased_crop as mrbc
import numpy as np
import time


class random_biased_crop(MediaCPUNode):
    """
    Class representing media random biased crop cpu node.

    """

    def __init__(self, name, guid, device, inputs, params, cparams, node_attr):
        """
        Constructor method.

        :params name: node name.
        :params guid: guid of node.
        :params guid: device on which this node should execute.
        :params params: node specific params.
        :params cparams: backend params.
        :params node_attr: node output information
        """
        super().__init__(
            name, None, device, inputs, params, cparams, node_attr)
        self.patch_size = params['patch_size'].copy()
        self.patch_size_np = self.patch_size[::-1]
        self.over_sampling = params['over_sampling']
        self.classify_uniquely = True
        self.threshold = params['threshold']
        self.num_channels = params['num_channels']
        self.seed = params['seed']
        self.num_workers = params['num_workers']
        if(self.num_workers < 1):
            raise ValueError("minimun one worker needed")
        if(self.num_workers > 8):
            raise ValueError("Num workers capped to 8")
        if len(self.patch_size) != 3:
            raise ValueError("3D patch size expected")

    def set_params(self, params):
        """
        Setter method to set mediapipe specific params.

        :params params: mediapipe params of type "opnode_params".
        """
        self.batch_size = params.batch_size
        self.rbc = mrbc.RandBalancedCrop(self.patch_size_np,
                                         self.batch_size,
                                         self.over_sampling,
                                         self.seed,
                                         self.num_workers,
                                         self.classify_uniquely,
                                         self.threshold)

    def gen_output_info(self):
        """
        Method to generate output type information.

        :returns : output tensor information of type "opnode_tensor_info".
        """
        self.img_shape = self.patch_size.copy()
        self.img_shape.append(self.num_channels)
        self.img_shape.append(self.batch_size)
        self.img_shape_np = self.img_shape[::-1]
        self.img_dtype = dt.FLOAT32
        self.lbl_shape = self.patch_size.copy()
        self.lbl_shape.append(1)  # labels channels is taken as one
        self.lbl_shape.append(self.batch_size)
        self.lbl_shape_np = self.lbl_shape[::-1]
        self.lbl_dtype = dt.UINT8
        self.coord_shape = [6, self.batch_size]
        self.coord_shape_np = self.coord_shape[::-1]
        self.coord_dtype = dt.UINT32
        out_info = []
        o = opnode_tensor_info(self.img_dtype, np.array(
            self.img_shape, dtype=np.uint32), "")
        out_info.append(o)
        o = opnode_tensor_info(self.lbl_dtype, np.array(
            self.lbl_shape, dtype=np.uint32), "")
        out_info.append(o)
        o = opnode_tensor_info(self.coord_dtype, np.array(
            self.coord_shape, dtype=np.uint32), "")
        out_info.append(o)
        return out_info

    def __call__(self, img, lbl):
        """
        Callable class method.

        :params img: image data
        :params lbl: label data
        """
        # print(">>> Random biased crop")
        # start_time0 = time.perf_counter()
        # print(">>>> rbc call")
        # start_time = time.perf_counter()
        self.rbc.call(lbl)
        coordinates = self.rbc.call_get()
        # end_time = time.perf_counter()
        # print("<<<< rbc call time  {:.6f}".format(end_time - start_time))
        img_sliced = np.empty(shape=self.img_shape_np, dtype=dt.FLOAT32)
        lbl_sliced = np.empty(shape=self.lbl_shape_np, dtype=dt.UINT8)
        coord = np.zeros(shape=self.coord_shape_np, dtype=dt.UINT32)
        """
        print("crop >>>>>>>>>>>>>>>>>>")
        for i in range(3):
            h = xxhash.xxh64(lbl[i])
            print(h.intdigest())
            h.reset()
        print("<<<<<<<<<<<<<<< crop")"""
        for i in range(self.batch_size):
            """
            img_tmp = img[i][:,
                             0:128,
                             0:128,
                             0:128]
            lbl_tmp = lbl[i][:,
                             0:128,
                             0:128,
                             0:128]
            coord[i] = [0,128,
                        0,128,
                        0,128]
            """
            coord[i] = [coordinates[i].lowX, coordinates[i].highX,
                        coordinates[i].lowY, coordinates[i].highY,
                        coordinates[i].lowZ, coordinates[i].highZ]
            # print("img {} lbl {} coord ( {} ) ".format(
            #    img[i].shape, lbl[i].shape, coord[i]))
            img_sliced[i] = img[i][:,
                                   coord[i][0]:coord[i][1],
                                   coord[i][2]:coord[i][3],
                                   coord[i][4]:coord[i][5]]
            lbl_sliced[i] = lbl[i][:,
                                   coord[i][0]:coord[i][1],
                                   coord[i][2]:coord[i][3],
                                   coord[i][4]:coord[i][5]]

        # end_time0 = time.perf_counter()
        # print("<<< Random biased crop {:.6f}".format(end_time0-start_time0))
        return img_sliced, lbl_sliced, coord
