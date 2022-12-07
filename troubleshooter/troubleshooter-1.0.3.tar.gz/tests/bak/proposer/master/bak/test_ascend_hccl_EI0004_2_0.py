#!/usr/bin/env python3
# coding=utf-8

"""
This is a python code template
"""
from mindspore import Tensor, nn, ops
import mindspore
import numpy as np
import troubleshooter as ts


@ts.proposal(write_file_path="/tmp/")
def main():
    error = """
Traceback (most recent call last):
  File "train.py", line 380, in <module>
    train_net()
  File "/opt/nvme2n1/m00256308/models-master/official/cv/resnet/scripts/train_parallel6/src/model_utils/moxing_adapter.py", line 104, in wrapped_func
    run_func(*args, **kwargs)
  File "train.py", line 307, in train_net
    set_parameter()
  File "train.py", line 154, in set_parameter
    init()
  File "/opt/nvme0n1/root/miniforge3/envs/miaoym/lib/python3.7/site-packages/mindspore/communication/management.py", line 151, in init
    init_hccl()
RuntimeError: Ascend collective communication initialization failed.

----------------------------------------------------
- Ascend Error Message:
----------------------------------------------------
EI0004: The ranktable is invalid,Reason:[Use a rank ID that exceeds the rank size in the ranktable.]. Please check the configured ranktable. [{"server_count":"1","server_list":[{"device":[{"device_id":"6","device_ip":"192.168.102.112","rank_id":"0"},{"device_id":"7","device_ip":"192.168.103.112","rank_id":"1"}],"host_nic_ip":"reserve","server_id":"10.90.42.160"}],"status":"completed","version":"1.0"}]
        Solution: Try again with a valid cluster configuration in the ranktable file. Ensure that the configuration matches the operating environment.

(Please search "Ascend Error Message" at https://www.mindspore.cn for error code description)

----------------------------------------------------
- Framework Error Message: (For framework developers)
----------------------------------------------------
Init hccl graph adapter failed.

----------------------------------------------------
- C++ Call Stack: (For framework developers)
----------------------------------------------------
mindspore/ccsrc/plugin/device/ascend/hal/hardware/ascend_collective_comm_lib.cc:112 Initialize
mindspore/ccsrc/plugin/device/ascend/hal/hccl_adapter/hccl_adapter.cc:402 InitKernelInfoStore
           """
    raise ValueError(error)


if __name__ == '__main__':
    from tests.util import delete_file, file_and_key_match
    delete_file("/tmp/")
    main()
    assert file_and_key_match("/tmp/", "vm_id_4")
