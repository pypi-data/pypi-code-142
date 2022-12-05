#
#   Lightnet optional dependencies
#   Copyright EAVISE
#
import warnings
import logging


__all__ = [
    'bb',
    'cv2',
    'Image',
    'ImageOps',
    'onnx',
    'onnx_numpy_helper',
    'pgpd',
    'pygeos',
    'tqdm',
]
log = logging.getLogger(__name__)


try:
    import brambox as bb
except ModuleNotFoundError:
    warnings.warn('Brambox is not installed and thus all data functionality related to it cannot be used', category=ImportWarning)
    bb = None

try:
    import cv2
except ModuleNotFoundError:
    warnings.warn('OpenCV is not installed and cannot be used', category=ImportWarning)
    cv2 = None

try:
    from PIL import Image, ImageOps
except ModuleNotFoundError:
    warnings.warn('Pillow is not installed and cannot be used', category=ImportWarning)
    Image, ImageOps = None, None

try:
    import onnx
    from onnx import numpy_helper as onnx_numpy_helper
except ModuleNotFoundError:
    warnings.warn('ONNX is not installed and thus no pruning functionality will work', category=ImportWarning)
    onnx = None
    onnx_numpy_helper = None

try:
    import pygeos
    import pgpd
except ModuleNotFoundError:
    warnings.warn('PyGEOS and PyGEOS-Pandas are not installed and thus no instance segmentation functionality will work', category=ImportWarning)
    pygeos = None
    pgpd = None

try:
    from tqdm.auto import tqdm
    tqdm.pandas()
except ModuleNotFoundError:
    tqdm = None
