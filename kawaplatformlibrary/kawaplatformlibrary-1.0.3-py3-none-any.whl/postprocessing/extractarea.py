import numpy as np

from pyproj import Transformer
from shapely.geometry import Polygon, Point
from rasterio.mask import mask

from .createprofile import createNewProfile
from .creatememoryraster import createMemRaster

def reprojectPolygon(gj, outproj, inproj):
    '''
    Reprojecting a GeoJson bounding box from one projection to another

    Input Parameters:
        1. gj      => GeoJson containing the coordinates to be reprojected
        2. outproj => Projection to be converted into
        3. inproj  => Current projection of the coordinates

    Output
        Reprojected GeoJson
    '''

    min_lat = gj['coordinates'][0][2][1]
    max_lat = gj['coordinates'][0][0][1]
    # print("Min Lat: {}, Max Lat: {}".format(min_lat, max_lat))

    max_lon = gj['coordinates'][0][2][0]
    min_lon = gj['coordinates'][0][0][0]
    # print("Min Lon: {}, Max Lon: {}".format(min_lon, max_lon))

    lat1_list = [min_lat, min_lat, max_lat, max_lat, min_lat]
    lon1_list = [min_lon, max_lon, max_lon, min_lon, min_lon]
    
    transformer = Transformer.from_crs(inproj, outproj)
    
    lon_list, lat_list = transformer.transform(lat1_list,lon1_list)
    
    polygon_reproj = Polygon(zip(lon_list, lat_list))

    polyg = polygon_reproj.exterior.coords

    coords = []
    for x,y in polyg:
        coords.append([x,y])
        pass

    gj_reproj = {"type": "Polygon", "coordinates" : [coords]}
    return gj_reproj
    pass

def extractArea(area_coordinates, raster):
    """
    Function for extracting an area from a raster and passing back a memory raster.

    Input Parameters:
        1. area_coordinates => Dictionary containing the coordinates and type of coordinates. Can also be a shapely polygon. CRS for the coordinates should be the same as the raster.
        2. raster           => Either memory raster or an opened TIF file

    Output:
        1. 
    """

    area_img, area_trans = mask(raster, [area_coordinates], crop=True)

    area_profile = createNewProfile(area_trans, raster.profile, img_height=area_img.shape[1], img_width=area_img.shape[2], num_bands=area_img.shape[0])

    return area_img, area_profile
    pass