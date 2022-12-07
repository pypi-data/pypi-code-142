import os
import mindspore
from mindspore import nn, Tensor, context
from mindspore import ops
import numpy as np
import troubleshooter as ts
from tests.util import delete_file, file_and_key_match

mindspore.set_context(mode=mindspore.PYNATIVE_MODE)


class Net(nn.Cell):
    def __init__(self):
        super().__init__()
        self.sqrt = ops.Sqrt()
        self.matmul = ops.MatMul()

    def construct(self, input_x):
        y = self.matmul(input_x, input_x)
        x = self.sqrt(y)
        return x


# @ts.tracking(level=1, path_bl=['context.py'])
@ts.tracking(level=2, check_nan=1)
def nan_func():
    input_x = Tensor(np.array([[0.0, -1.0], [4.0, 3.0]]))
    k = 3.0
    net = Net()
    print(net(input_x))


def test_sqrt_nan(capfd):
    mindspore.set_context(mode=mindspore.PYNATIVE_MODE)
    #os.environ['troubleshooter_log_path'] = '/tmp/'

    class Net(nn.Cell):
        def __init__(self):
            super().__init__()
            self.sqrt = ops.Sqrt()
            self.matmul = ops.MatMul()

        def construct(self, input_x):
            y = self.matmul(input_x, input_x)
            x = self.sqrt(y)
            return x

    # @ts.tracking(level=1, path_bl=['context.py'])
    @ts.tracking(level=2, check_nan=2, color=False)
    def nan_func():
        input_x = Tensor(np.array([[0.0, -1.0], [4.0, 3.0]]))
        k = 3.0
        net = Net()
        print(net(input_x))

    #delete_file("/tmp/", file_name="troubleshooter.log")
    #delete_file("/tmp/", file_name="mindspore_tracking_test.log")
    nan_func()


test_sqrt_nan()
