from habana_frameworks.mediapipe.backend.nodes import opnode_tensor_info
from habana_frameworks.mediapipe.operators.media_nodes import MediaReaderNode
from habana_frameworks.mediapipe.media_types import dtype as dt
from habana_frameworks.mediapipe.media_types import readerOutType as ro
from habana_frameworks.mediapipe.backend.utils import array_from_ptr
import numpy as np
import os
import glob
import time
import copy
import media_numpy_reader as mnr


def round_idx_list(rng, in_list_idxs, append_cnt, pad_remainder):
    """
    Method to round up/down.
    :raises ValueError: if mismatch is seen in length of flielist and labellist
    """
    # this function works on sliced dataset only
    num_in_idxs = len(in_list_idxs)
    if(append_cnt > 0):
        if(pad_remainder == False):
            idx = rng.choice(num_in_idxs,
                             size=append_cnt,
                             replace=False)
            idx = sorted(idx)
        else:
            idx = np.zeros(shape=(append_cnt), dtype=np.uint32)
            idx = idx + num_in_idxs - 1
        list_pad_idxs = in_list_idxs[idx]
        list_idxs = np.append(in_list_idxs, list_pad_idxs)
    else:
        list_idxs = in_list_idxs[0:(num_in_idxs+append_cnt)]
    return list_idxs


def slice_idx_list(dlist, slice_index, num_slices, type):
    list_len = len(dlist)
    if(type == "mod"):
        # now we slice the dataset
        slice_len = int(list_len / num_slices)
        idx = np.arange(slice_len)
        idx = (idx * num_slices) + slice_index
        dlist = dlist[idx]
    elif(type == "cont"):
        slice_len = int(list_len / num_slices)
        start = slice_len * slice_index
        end = start + slice_len
        dlist = dlist[start:end]
    return dlist


def gen_npy_list(dir, pattern):
    return np.array(sorted(glob.glob(dir + "/{}".format(pattern))))


def get_max_file(file_list):
    return max(file_list, key=lambda x: os.stat(x).st_size)


broadcastable_params = [
    'dir', 'max_file', 'pattern',
]


class read_numpy_from_dir(MediaReaderNode):
    """
    Class defining numpy reader node.

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
        super().__init__(name, guid, device, inputs,
                         params, cparams, node_attr)
        self.batch_size = 1
        self.seed = params['seed']
        del params['seed']
        self.drop_remainder = params['drop_remainder']
        del params['drop_remainder']
        self.pad_remainder = params['pad_remainder']
        del params['pad_remainder']
        self.num_slices = params['num_slices']
        del params['num_slices']
        self.slice_index = params['slice_index']
        del params['slice_index']
        self.shuffle = params['shuffle']
        del params['shuffle']
        self.shuffle_across_dataset = params['shuffle_across_dataset']
        del params['shuffle_across_dataset']
        self.num_readers = params["num_readers"]
        del params['num_readers']
        if(self.num_readers < 1):
            raise ValueError("minimun one reader needed")
        if(self.num_readers > 8):
            raise ValueError("Num readers capped to 8")
        if(self.num_slices < 1):
            raise ValueError("num slice cannot be less then 1")
        if(self.slice_index >= self.num_slices):
            raise ValueError("slice_index cannot be >= num_slices")
        print("num_slices {} slice_index {}".format(
            self.num_slices, self.slice_index))
        print("random seed used ", self.seed)
        self.rng = np.random.default_rng(self.seed)
        self.num_outputs = len(node_attr)
        self.dtype = []
        if(self.num_outputs > 2):
            raise ValueError("max outputs supported is two")
        for i in range(self.num_outputs):
            self.dtype.append(node_attr[i]['outputType'])
        if(self.num_outputs > 1):
            if(params['file_list'] is not None and len(params['file_list']) != self.num_outputs):
                raise ValueError(
                    "File list length should be equal to ouput operands expected but got ", len(params['file_list']))
        if(params['file_list'] is None):
            params['file_list'] = [None, None]

        bcst_params = self.broadcast_params(broadcastable_params,
                                            params,
                                            self.num_outputs)
        self.readers = []
        for i in range(self.num_outputs):
            p = copy.deepcopy(params)
            for key in bcst_params:
                p[key] = bcst_params[key][i]
            p['file_list'] = params['file_list'][i]
            self.readers.append(_numpy_unit_reader_(p,
                                                    self.dtype[i]))
        if (self.seed == None):
            # max supported seed value is 32bit so modulo
            self.seed = int(time.time_ns() % (2**31 - 1))
        num_dataset = []
        for r in self.readers:
            num_dataset.append(r.get_unique_npys_count())
        if(np.max(num_dataset) != np.min(num_dataset)):
            raise ValueError("Readers length of dataset not matching")
        self.num_unique_idxs = num_dataset[0]
        self.list_unique_idxs = np.arange(self.num_unique_idxs)

    def broadcast_params(self, key_list, dictionary, broadcast_lenght):
        bcst_dict = {}
        for key in key_list:
            if(not isinstance(dictionary[key], list)):
                dictionary[key] = [dictionary[key]]
            if len(dictionary[key]) != broadcast_lenght:
                if(len(dictionary[key]) == 1):
                    for i in range(broadcast_lenght - 1):
                        dictionary[key].append(dictionary[key][0])
            bcst_dict[key] = dictionary[key]
        return bcst_dict

    def calculate_idxs_sizes_for_round(self, round):
        """
        Method to round up/down.
        """
        # this function works on sliced dataset only
        if(self.drop_remainder == False):
            self.append_cnt = int((self.num_unique_idxs + round - 1) /
                                  round) * round - self.num_unique_idxs

        else:
            self.append_cnt = int(self.num_unique_idxs /
                                  round) * round - self.num_unique_idxs
        self.num_idxs = self.num_unique_idxs + self.append_cnt

    def set_params(self, params):
        """
        Setter method to set mediapipe specific params.

        :params params: mediapipe params of type "opnode_params".
        """
        for r in self.readers:
            r.set_params(params)
        self.batch_size = params.batch_size
        self.calculate_idxs_sizes_for_round(self.num_slices*self.batch_size)
        if(self.shuffle_across_dataset == False):
            list_rounded_idxs = round_idx_list(self.rng,
                                               self.list_unique_idxs,
                                               self.append_cnt,
                                               self.pad_remainder)
            self.list_sliced_idxs = slice_idx_list(list_rounded_idxs,
                                                   self.slice_index,
                                                   self.num_slices,
                                                   "mod")

    def __del__(self):
        for r in self.readers:
            del r

    def gen_output_info(self):
        """
        Method to generate output type information.

        :returns : output tensor information of type "opnode_tensor_info".
        """
        out_info = []
        for r in self.readers:
            out_info.append(r.gen_output_info()[0])
        return out_info

    def get_largest_file(self):
        """
        Method to get largest media in the dataset.

        returns: largest media element in the dataset.
        """
        fileList = []
        for r in self.readers:
            fileList.append(r.fileList())
        self.max_file = get_max_file(fileList)
        return self.max_file

    def get_media_output_type(self):
        return ro.BUFFER_LIST

    def __len__(self):
        """
        Method to get dataset length.

        returns: length of dataset in units of batch_size.
        """
        return int(self.num_idxs / (self.num_slices*self.batch_size))

    def __iter__(self):
        """
        Method to initialize iterator.

        """
        if(self.shuffle_across_dataset == True):
            list_rounded_idxs = round_idx_list(self.rng, self.list_unique_idxs,
                                               self.append_cnt, self.pad_remainder,)
            list_shuffled_idxs = list_rounded_idxs.copy()
            if(self.shuffle == True):
                print("Shuffling ...",  end=" ")
                self.rng.shuffle(list_shuffled_idxs)
                print("Done!")
            list_shuffled_sliced_idxs = slice_idx_list(list_shuffled_idxs,
                                                       self.slice_index,
                                                       self.num_slices,
                                                       "mod")
        else:
            list_shuffled_sliced_idxs = self.list_sliced_idxs.copy()
            if(self.shuffle == True):
                print("Shuffling ...",  end=" ")
                self.rng.shuffle(list_shuffled_sliced_idxs)
                print("Done!")
        for r in self.readers:
            r.iter(list_shuffled_sliced_idxs)
        return self

    def __next__(self):
        """
        Method to get one batch of dataset ouput from iterator.

        """
        out_bufs = []
        stopException = 0
        for r in self.readers:
            try:
                out_bufs.append(r.next())
            except StopIteration:
                stopException += 1
        if(stopException == self.num_outputs):
            raise StopIteration
        elif (len(out_bufs) == self.num_outputs):
            # print(out_bufs)
            return out_bufs
        else:
            raise RuntimeError("readers not synchronized")


class _numpy_unit_reader_():
    """
    Class defining numpy reader node.

    """

    def __init__(self, params, dtype):
        """
        Constructor method.

        :params name: node name.
        :params guid: guid of node.
        :params guid: device on which this node should execute.
        :params params: node specific params.
        :params cparams: backend params.
        :params out_info: node output information
        """
        self.batch_size = 1
        self.file_list = params['file_list']
        self.dir = params['dir']
        self.pattern = params['pattern']

        self.max_file = params['max_file']
        self.dense = params['dense']
        self.output_dtype = dtype
        if(self.file_list is None and self.dir != None):
            print("Finding images ...", end=" ")
            self.npy_unique_list = gen_npy_list(self.dir, self.pattern)
            print("Done!")
        elif(self.file_list is not None and self.dir is None):
            self.npy_unique_list = np.array(self.file_list)
        elif(self.file_list is None and self.dir is None):
            raise ValueError("Atleast file_list or dir must be shared")
        else:
            raise ValueError("Only one file_list or dir must be shared")
        self.num_unique_idxs = len(self.npy_unique_list)
        if(self.num_unique_idxs == 0):
            raise ValueError("npys list empty !!!")
        print("Total npy files {} ".format(self.num_unique_idxs))
        # print(self.num_slices)
        if(self.max_file == None):
            print("Finding largest file ...")
            self.max_file = get_max_file(self.npy_unique_list)
        print("largest file is ", self.max_file)
        self.num_outstanding_cmds = 0
        self.reader = None

    def set_params(self, params):
        """
        Setter method to set mediapipe specific params.

        :params params: mediapipe params of type "opnode_params".
        """
        self.batch_size = params.batch_size
        self.queue_depth = params.queue_depth
        if(self.dense == True):
            self.shape = np.load(self.max_file).shape
            if(not isinstance(self.shape, list)):
                self.shape = list(self.shape)
            self.shape = self.shape[::-1]
            self.shape.append(self.batch_size)
        else:
            self.shape = [0, 0, 0, self.batch_size]
        self.reader = mnr.NumpyReader(self.queue_depth, 1, self.batch_size,
                                      os.stat(self.max_file).st_size)
        self.reader.StartWorker()

    def __del__(self):
        if(self.reader != None):
            self.reader.StopWorker()
            del self.reader

    def gen_output_info(self):
        """
        Method to generate output type information.

        :returns : output tensor information of type "opnode_tensor_info".
        """
        out_info = []
        o = opnode_tensor_info(self.output_dtype,
                               np.array(self.shape, dtype=np.uint32),
                               "")
        out_info.append(o)
        return out_info

    def get_largest_file(self):
        """
        Method to get largest media in the dataset.

        returns: largest media element in the dataset.
        """
        return self.max_file

    def get_media_output_type(self):
        return ro.BUFFER_LIST

    def get_unique_npys_count(self):
        return self.num_unique_idxs

    def iter(self, list_shuffled_sliced_idxs):
        """
        Method to initialize iterator.

        """
        self.reader.flush()
        self.num_outstanding_cmds = 0
        self.npy_iter_list = self.npy_unique_list[list_shuffled_sliced_idxs]
        self.num_iter_list = len(self.npy_iter_list)

        self.iter_loc = 0
        while(self.num_outstanding_cmds < self.queue_depth):
            if self.iter_loc > (self.num_iter_list - 1):
                break
            else:
                start = self.iter_loc
                end = self.iter_loc + self.batch_size
                npy_list = self.npy_iter_list[start:end]
                self.iter_loc = self.iter_loc + self.batch_size
                self.reader.SubmitFiles(npy_list)
                self.num_outstanding_cmds = self.num_outstanding_cmds + 1
        return self

    def next(self):
        """
        Method to get one batch of dataset ouput from iterator.

        """
        if self.num_outstanding_cmds == 0:
            raise StopIteration
        output = self.reader.WaitForCompletion()
        self.num_outstanding_cmds = self.num_outstanding_cmds - 1
        if self.iter_loc > (self.num_iter_list - 1):
            pass
        else:
            start = self.iter_loc
            end = self.iter_loc + self.batch_size
            npy_list = self.npy_iter_list[start:end]
            self.iter_loc = self.iter_loc + self.batch_size
            self.reader.SubmitFiles(npy_list)
            # print(npy_list)
            self.num_outstanding_cmds = self.num_outstanding_cmds + 1
        out_bufs = []
        for o in output:
            out_bufs.append(array_from_ptr(o.pBuffer,
                                           o.typeStr,
                                           tuple(o.shape[:o.numDims])))
        for o in out_bufs:
            if(o.dtype != self.output_dtype):
                raise ValueError("Datatype mismatch file contains dtype{} reader expected dtype {}".format(
                    o.dtype, self.output_dtype))
        if(self.dense):
            output = np.stack(out_bufs)
        else:
            output = out_bufs
        return output
