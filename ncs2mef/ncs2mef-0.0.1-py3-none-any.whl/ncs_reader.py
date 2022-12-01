# Copyright 2022-present, Mayo Clinic Department of Neurology - Bioelectronics Neurophysiology and Engineering Laboratory
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
import numpy as np

def read_ncs_channel(path):
    """
    Reads NCS file.

    :param path:
    :return x: numpy array of raw data read from the NCS file
    :return fs: Sampling rate
    :return hdr: File header
    """
    bytes_to_read = os.path.getsize(path)
    fid = open(path, 'rb')
    hdr = fid.read(16384) # header size
    hdr = str(hdr).split('\\r\\n')[:-1]
    hdr = dict([(h.replace('-', '').replace("\\xb5", 'u').split(' ')[0], ' '.join(h.replace('-', '').replace("\\xb5", 'u').replace("\\xbf\\xbd", "N/A ").replace("\"", '').split(' ')[1:])) for idx, h in enumerate(hdr) if h.__len__() and idx > 0])
    for k in hdr.keys():
        if hdr[k].replace('.', '').isnumeric():
            if '.' in hdr[k]: hdr[k] = float(hdr[k])
            else: hdr[k] = int(hdr[k])
        elif hdr[k] in ['True', 'Enabled']:
            hdr[k] = True
        elif hdr[k] in ['False',  'Disabled']:
            hdr[k] = False

    fs = []
    timestamps = []
    data = []

    run = True
    while run:
        timestamp = fid.read(8)
        skip_bytes = fid.read(4)
        fs_ = fid.read(4)
        valid_samples = fid.read(4)

        if timestamp.__len__() and skip_bytes.__len__() and fs_.__len__() and valid_samples.__len__():
            timestamp = np.frombuffer(timestamp, dtype=np.uint64)[0]
            skip_bytes = np.frombuffer(skip_bytes, dtype = np.uint32)[0]
            fs_ = np.frombuffer(fs_, dtype = np.uint32)[0]
            valid_samples = np.frombuffer(valid_samples, dtype = np.uint32)[0]

            x = fid.read(valid_samples * 2)
            if x.__len__() * 2:
                x = np.frombuffer(x, dtype = np.int16)

                data += [x]
                timestamps += [timestamp]
                fs += [fs_]
            else:
                print('Data block has been corrupted. The data block does not match header. Terminating data reading.')
                run = False
        else:
            run = False

    if fs.__len__():
        fs = fs[0]
        timestamps = np.array(timestamps)
        x = np.concatenate(data).astype(np.float) * hdr['ADBitVolts']
        if hdr['InputInverted']:
            x = -x
    else:
        fs = None
        x = np.array([])

    return x, fs, hdr




