from pathlib import Path

import numpy as np
from rasterio import DatasetReader
from rasterio.merge import merge

from digitalarztools.raster.rio_raster import RioRaster


class RioProcess:
    def __init__(self):
        pass

    @staticmethod
    def mosaic_images(img_folder: str) -> RioRaster:
        ds_files: [DatasetReader]
        path = Path(img_folder)
        # test = [str(p) for p in path.iterdir() if p.suffix == ".tif"]
        ds_files = [RioRaster(str(p)).get_dataset() for p in path.iterdir() if p.suffix == ".tif"]
        mosaic, out_trans = merge(ds_files)
        crs = ds_files[0].crs
        raster = RioRaster.raster_from_array(mosaic, crs=crs, transform=out_trans)
        return raster

    def classify_ndwi(self, band=8) -> np.ndarray:
        classes = {
            "vegetation": (('lt', 0.1), 3),
            "built-up": ((-0.1, 0.4), 1),
            "water": (('gt', 0.4), 4),
        }
        img_arr = self.stack_raster.get_data_array(band)
        res = self.classify_based_on_ranges(img_arr, classes)
        return res.astype(np.uint8)

    @staticmethod
    def classify_based_on_ranges(img_arr: np.ndarray, classes: dict):
        res = np.empty(img_arr.shape)
        res[:] = np.NaN
        for key in classes:
            if classes[key][0][0] == 'lt':
                res = np.where(img_arr <= classes[key][0][1], classes[key][1], res)
            elif classes[key][0][0] == 'gt':
                res = np.where(img_arr >= classes[key][0][1], classes[key][1], res)
            else:
                con = np.logical_and(img_arr >= classes[key][0][0], img_arr <= classes[key][0][1])
                res = np.where(con, classes[key][1], res)
        return res

    @classmethod
    def classify_ndwi(cls, rio_raster: RioRaster, band=1) -> np.ndarray:
        classes = {
            "vegetation": (('lt', 0.1), 3),
            "built-up": ((-0.1, 0.4), 1),
            "water": (('gt', 0.4), 4),
        }
        img_arr = rio_raster.get_data_array(band)
        res = cls.classify_based_on_ranges(img_arr, classes)
        return res.astype(np.uint8)

    @classmethod
    def classify_ndvi(cls, rio_raster: RioRaster, band=1) -> np.ndarray:
        classes = {
            "water": (('lt', 0.015), 4),
            "built-up": ((0.015, 0.02), 1),
            "barren": ((0.07, 0.27), 2),
            "vegetation": (('gt', 0.27), 3)
        }
        print("no of bands", rio_raster.get_spectral_resolution())
        img_arr = rio_raster.get_data_array(band)
        res = cls.classify_based_on_ranges(img_arr, classes)
        return res.astype(np.uint8)

    def combine_indices(self):
        # values = np.unique(pc_classification)
        # for val in values:
        ndvi_classification = self.classify_ndvi(7)
        ndwi_classification = self.classify_ndwi(8)
        x = np.where(ndwi_classification == 1, ndwi_classification, ndvi_classification)
        x = np.where(ndwi_classification == 4, ndwi_classification, x)
        return x
