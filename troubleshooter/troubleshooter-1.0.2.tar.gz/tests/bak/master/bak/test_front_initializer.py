import numpy as np
import mindspore
from mindspore import Tensor
from mindspore.common import initializer
import troubleshooter as ts
data = Tensor(np.zeros([1, 2, 3]), mindspore.float32)
with ts.proposal(write_file_path="/tmp/"):
    tensor1 = initializer(data, [1, 2, 3], mindspore.float32)