from cenfind.experiments.constants import PREFIX_REMOTE
from cenfind.core.data import Dataset
import tifffile as tf
import numpy as np



def main():
    data = tf.imread(PREFIX_REMOTE / 'data_sankaran/imgs/MDA_231/raw/1.tif')
    data_npy = np.load(PREFIX_REMOTE / 'data_sankaran/imgs/MDA_231/1.npy')
    print(0)


if __name__ == '__main__':
    main()
