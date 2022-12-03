from pathlib import Path
import pickle
import json
import os
from matplotlib import pyplot as plt

def load(path: os.PathLike, default=None):
    path = Path(path)
    
    if not path.suffix in ('.pickle', '.json'):
        raise ValueError('path must end in either .pickle or .json.')
    
    if path.exists():
        if path.suffix == '.pickle':
            with open(path, 'rb') as f:
                return pickle.load(f)
        elif path.suffix == '.json':
            with open(path) as f:
                return json.load(f)
    elif default is not None:
        return default
            
    
    raise FileNotFoundError('File not found and default=None.')


def dump(value, path: os.PathLike):
    path = Path(path)
    if path.suffix == '.pickle':
        with open(path, 'wb') as f:
            pickle.dump(value, f)
    elif path.suffix == '.json':
        with open(path, 'w') as f:
            json.dump(value, f)
    else:
        raise ValueError('path must end in either .pickle or .json.')
        

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def imshow_grid(*images, nrows=None, ncols=None, titles=None, axes_off=True, figsize=None):
    if nrows and ncols:
        assert nrows * ncols == len(images)
    elif nrows:
        assert len(images) % nrows == 0
        ncols = len(images) // nrows
    elif ncols:
        assert len(images) % ncols == 0
        nrows = len(images) // ncols
    else:
        nrows = 1
        ncols = len(images)

    if not figsize:
        k = 12
        ratio = 1  # 0.25 if titles else 0.2
        figsize = (k * nrows, k * ncols)

    figs, axes = plt.subplots(nrows=nrows, ncols=ncols, squeeze=False, figsize=figsize)

    for i, (im, ax) in enumerate(zip(images, axes.reshape(-1))):
        if im is not None:
            ax.imshow(im, interpolation='nearest')
        if axes_off:
            ax.axis('off')
        if titles:
            ax.set_title(titles[i])

    plt.tight_layout()
    plt.show()