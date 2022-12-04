import geopandas as gpd


class GPDVector():
    gdf: gpd.GeoDataFrame

    def __init__(self, gdf: gpd.GeoDataFrame):
        self.gdf = gdf

    @classmethod
    def from_shp(cls, src):
        gdf = gpd.read_file(src)
        return cls(gdf)

    def get_srs(self)->str:
        return self.gdf.crs.srs

    def get_crs(self):
        return self.gdf.crs
