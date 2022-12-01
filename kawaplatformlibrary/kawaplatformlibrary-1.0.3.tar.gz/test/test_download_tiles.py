"""

NOTE: This code runs if kawaplatformlibrary is already installed in the virtual environment. 

"""

"""
Example for downloading one Sentinel 2 tile for a specific AOI. All parameters are optional and contain default values which will be used for downloading the Sentinel 2 tile. The only parameter which is required is the destination file for storing the TIF obtained from STAC API.s

Input parameters:
    1. geojson                  => GeoJSON for the Area of Interest[AOI]. Optional with a default value
    2. start_date               => The initial date from when data should be requested from STAC API. Format maintained is YYYY-MM-DD. Optional with a default value.
    3. end_date                 => The final date before which data should be requested from STAC API. Format maintained is YYYY-MM-DD. Optional with a default value.
    4. bands                    => The bands to be requested from the STAC API for the Sentinel 2 tiles. Comma separated list. Optional with default being ["B02","B03","B04"]
    5. ground_sampling_distance => The ground sampling distance to which all bands should be resampled to. Optional with a default value of 10m.
    6. destination_file         => The file location where the obtained TIF file should be stored.

Output parameters:
    Stores the data obtained in a file specified by the user.

Example UseCase : 
python download_tiles.py --geojson ../../test_aoi.geojson --start_date 2020-02-01 --end_date 2020-02-27 --bands B02,B03,B04 --ground_sampling_distance 10 --destination_folder ../../Test_Examples_Folder_Path --num_threads 6
"""

# importing libraries
import numpy as np
import json, argparse, rasterio, os

import sys
sys.path.insert(1, "./../") # Changing the system path to root directory of the library. This is needed to actually call the Kawa Platform library

from kawaplatformlibrary.data import sentinel2dataingestion
from kawaplatformlibrary.data.preprocessing import splitgeojson
from kawaplatformlibrary.postprocessing.mosiac import mergeBands
from kawaplatformlibrary.postprocessing.createprofile import createNewProfile
from kawaplatformlibrary.postprocessing.creatememoryraster import createMemRaster
from kawaplatformlibrary.postprocessing.extractarea import (reprojectPolygon, extractArea)

from rasterio import Affine

# Optional arguments for the user
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--geojson", required=True, 
    help="Path to GEOJSON file containing the AOI.")
ap.add_argument("-s", "--start_date", required=True, 
    help="Start date in YYYY-MM-DD format")
ap.add_argument("-e", "--end_date", required=True, 
    help="End date in YYYY-MM-DD format")
ap.add_argument("-b", "--bands", required=True,
    help="Comma separated list of bands")
ap.add_argument("-d","--ground_sampling_distance", nargs="?", default=10, type=int,
    help="Ground Sampling Distance required for each band")
# This is not optional. User should input this
ap.add_argument("-f", "--destination_folder", required=True,
    help="Path to folder for storage. Use the full OS path and not relative path")
args = vars(ap.parse_args())

user_bands = [band.strip() for band in args["bands"].split(',')]

# Reading the GeoJSON of the AOI and extracting the coordinates json. {"type": "Polygon", "coordinates":[[[...], [...], ...]]]}
with open(args["geojson"], "r") as in_file:
    geojson_contents = json.load(in_file)
    geojson_coordinates = geojson_contents["features"][0]["geometry"]
    in_file.close()
    pass

# Obtaining image url from STAC API. dataCheck = [0/1, "[ERROR]/["INFO"]", {}/{<data>}]
print("[INFO] Obtianing data for the AOI")
sentinel2_data_class_obtain_data = sentinel2dataingestion.ObtainData(bands=user_bands)
sentinel2_data_aoi = sentinel2_data_class_obtain_data.getBandData(geojson=geojson_coordinates, start_date=args["start_date"], end_date=args["end_date"])
print("[INFO] Finished finding data for the AOI.")

def downloadData(rasters_href):
    """
    Downloading and storing the data in the destination folder.
    """
    print("[INFO] Downloading data for {}".format(rasters_href["img_id"]))

    destination_file = args["destination_folder"] + rasters_href["img_id"] + ".tif"

    bands_rasters_list = []
    bands_data = rasters_href["band_data"]

    # Reading the bands into memory as numpy arrays
    for j, band in enumerate(bands_data):

        band_href = bands_data[band]["href"]
        band_src = rasterio.open(band_href)
        bands_rasters_list.append(band_src)

        # Creating the destination profile for each Sentinel 2 tile. Will be used for storing the current tile.
        if j == 0:
            num_bands = len(user_bands)
            dst_profile = createNewProfile(band_src.transform, band_src.profile, ground_sampling_distance=10, num_bands=num_bands)
            pass
        pass

    # Resampling and merging the bands
    print("[INFO] Merging bands for img : {}".format(rasters_href["img_id"]))
    merged_resample_bands = mergeBands(bands_rasters_list, args["ground_sampling_distance"])
    print("[INFO] Finished merging bands for img : {}".format(rasters_href["img_id"]))

    print("[INFO] Creating merged bands raster.")
    merged_bands_raster = createMemRaster(dst_profile, merged_resample_bands)
    print("[INFO] Finished creating raster.")

    print("[INFO] Reprojecting polygon to required CRS.")
    bands_epsg = rasters_href["init"]
    geojson_coordinates_reproject = reprojectPolygon(gj=geojson_coordinates, outproj=bands_epsg, inproj="EPSG:4326")
    print("[INFO] Finished reprojecting polygon to required CRS.")

    print("[INFO] Clipping area.")
    geojson_clipped_area, geojson_clipped_area_profile = extractArea(geojson_coordinates_reproject, merged_bands_raster)
    print("[INFO] Finished clipping area.")

    print("[INFO] Storing clipping data.")
    # Storing the Sentinel 2 tile in the destination folder with tile name corresponding to the tile ID
    with rasterio.open(destination_file, "w", **geojson_clipped_area_profile) as out_file:
        out_file.write(geojson_clipped_area)
        pass

    print("[INFO] Finished downloading data for {}".format(rasters_href["img_id"]))
    pass

data = list(sentinel2_data_aoi.items())[0][1]
data_sensing_date = list(sentinel2_data_aoi.items())[0][0]
data_check = data[0]

if data_check == 1:
    downloadData(data[2])
else:
    print("[INFO] Error Code : {} Error Message : {}".format(data[0], data[1]))