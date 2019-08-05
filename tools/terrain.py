# tools for importing dem
# Michael Holmes 2019
# mkhlib@outlook.com

import rasterio as rio
from rasterio.plot import show
from rasterio.mask import mask
import pycrs
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import sys

class terrain:

    def __init__(self, path_to_raster):
        self.__raw = self.__load_raster(path_to_raster)

    def __load_raster(self, ras):
        if ras is not None:
            return  rio.open(ras)

    def plot(self):
        show((self.__raw), cmap='terrain')


test = terrain(sys.argv[1])
test.plot()

