import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
pd.set_option('display.max_columns', None)

from opentimspy import OpenTIMS

import pathlib
import hashlib


# path = pathlib.Path("E:\\Work\\MS_visualizer\\data\\data.d")

def get_hash(path):
    with open(path, "rb") as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()


# print(get_hash(path / "analysis.tdf"))
# print("930ccbbf518edcd58698f360b96c405de9b26eb88389544c9b51d48759253f2b")
# print(get_hash(path / "analysis.tdf_bin"))
# print("7f5eaae8576799b49df5999880b402d8864e34de8c9793d2db761eacb0400b13")

exemplary_rawdata_path = pathlib.Path("E:\\Work\\MS_visualizer\\data\\data.d")
if exemplary_rawdata_path.exists():
    print("Data is where it should.")
else:
   print("Data missing")


data = OpenTIMS(exemplary_rawdata_path)
print(data)
X = pd.DataFrame(data.query(frames=data.ms1_frames[:100]))


multiply_charged = "inv_ion_mobility <= 0.4467452 + 0.00101627*mz and inv_ion_mobility <= 0.5301116 + 0.000849*mz"
X.query(multiply_charged)

print(X.columns)


# Some variables are correlated:
#     # physical
# x -> mz or tof
# z -> inv_ion_mobility or scan
# y -> retention_time or frame
#                         # cyber
# plt.scatter(Y.retention_time, Y.frame)
# plt.show()

# plt.scatter(X.mz, X.tof)
# plt.show()

# plt.scatter(X.scan, X.inv_ion_mobility)
# plt.show()
# so we should not map them together


