import os

url_map_dep = "https://github.com/otmaneelallaki/HAX712X-DOS/blob/main/Project/Map/DataSet/departements_consumption.csv"
url_map_reg = "https://github.com/otmaneelallaki/HAX712X-DOS/blob/main/Project/Map/DataSet/regions_consumption.csv"


path_target_dep = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data_map", "departements_consumption.csv"
)

path_target_reg = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data_map", "regions_consumption.csv"
)