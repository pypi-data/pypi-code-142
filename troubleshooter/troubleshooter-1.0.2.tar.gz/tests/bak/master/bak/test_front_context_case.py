from mindspore import context
import troubleshooter as ts

with ts.proposal(write_file_path="/tmp/"):
    # import pdb
    # pdb.set_trace()
    context.set_context(device_target='Ascend')