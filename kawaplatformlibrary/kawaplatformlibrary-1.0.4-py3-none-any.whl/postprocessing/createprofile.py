"""
To create a new profile for any raster. This does not create a new raster instead creates a profile for the new raster so that it can be written to a GeoTIFF file.
"""

import json
import rasterio

from rasterio import Affine

def createNewProfile(src_transform, src_profile, ground_sampling_distance=None, num_bands=1, dtype="float32", img_height=None, img_width=None):
    """
    Creating a function for making a new Profile with change in the Ground Sampling distance and Count of bands

    Input Parameters:
        1. src_transform             => Transformation matrix of the source raster
        2. src_profile               => Profile dictionary of the source raster
        3. ground_sampling_distance  => Ground sampling distance of the resultant profile
        4. num_bands                 => Number of bands present in the resultant profile
        5. dtype                     => Decimal type of the resultant profile. Default is set to float32.
        6. img_height                => Specify the height of the image to which the profile is to fit. Defaults to None
        7. img_width                 => Specify the width of the image to which the profile is to fit. Defaults to None

        img_height and img_width both have to be included. They do not work separately.

    Output:
        1. New and updated profile.
    """
    if ground_sampling_distance and src_transform[0] != ground_sampling_distance:
        scale = src_transform[0] // ground_sampling_distance
    else:
        scale = 1

    dst_transform = Affine(src_transform.a / scale, src_transform.b, src_transform.c, src_transform.d, 
        src_transform.e / scale, src_transform.f)

    if img_height and img_width:
        dst_height = img_height
        dst_width  = img_width
    else: 
        dst_width = int(src_profile["height"] * scale)
        dst_height = int(src_profile["width"] * scale)

    dst_profile = src_profile
    dst_profile.update(transform=dst_transform, driver="GTIFF", height=dst_height, width=dst_width, 
        count=num_bands, dtype="float32")

    return dst_profile
    pass